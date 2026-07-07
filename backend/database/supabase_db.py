import logging
import httpx
import json
from datetime import datetime, timezone
from typing import List, Optional, Dict

logger = logging.getLogger('ats_resume_scorer')

import os
from backend.core.config import SUPABASE_URL, SUPABASE_KEY

_mock_db = []

def _get_headers():
    if not SUPABASE_URL or not SUPABASE_KEY:
        return None
    return {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }

async def save_analysis(user_id: str, filename: str, analysis_result: Dict) -> Optional[str]:
    headers = _get_headers()
    is_mock = os.getenv('MOCK_MODE', 'false').lower() == 'true' or not headers
    
    if is_mock:
            def _json_default(o):
                if hasattr(o, 'model_dump'):
                    return o.model_dump()
                return str(o)
            serializable_result = json.loads(json.dumps(analysis_result, default=_json_default))
            
            mock_id = f"mock-analysis-{len(_mock_db) + 1}"
            doc = {
                "id": mock_id,
                "user_id": user_id,
                "filename": filename,
                "ats_score": serializable_result.get("ats_score", 0),
                "keyword_match": serializable_result.get("keyword_match", 0),
                "missing_keywords": serializable_result.get("missing_keywords", []),
                "created_at": datetime.now(timezone.utc).isoformat(),
                "analysis_result": serializable_result,
            }
            _mock_db.append(doc)
            logger.info(f"[MOCK DB] Saved analysis for user {user_id}: {mock_id}")
            return mock_id
        return None

    def _json_default(o):
        if hasattr(o, 'model_dump'):
            return o.model_dump()
        return str(o)
    serializable_result = json.loads(json.dumps(analysis_result, default=_json_default))

    doc = {
        "user_id": user_id,
        "filename": filename,
        "ats_score": serializable_result.get("ats_score", 0),
        "keyword_match": serializable_result.get("keyword_match", 0),
        "missing_keywords": serializable_result.get("missing_keywords", []),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "analysis_result": serializable_result,
    }

    url = f"{SUPABASE_URL.rstrip('/')}/rest/v1/analyses"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=doc)
            response.raise_for_status()
            data = response.json()
            if data and len(data) > 0:
                inserted_id = str(data[0].get("id"))
                logger.info(f"Saved analysis for user {user_id}: {inserted_id}")
                return inserted_id
            return None
    except Exception as exc:
        logger.error(f"Failed to save analysis to Supabase: {exc}")
        return None

async def get_user_history(user_id: str) -> List[Dict]:
    headers = _get_headers()
    is_mock = os.getenv('MOCK_MODE', 'false').lower() == 'true' or not headers
    
    if is_mock:
            results = []
            for doc in _mock_db:
                if doc.get("user_id") == user_id:
                    results.append({
                        "id": doc.get("id"),
                        "filename": doc.get("filename", "resume"),
                        "resume_name": doc.get("filename", "resume"),
                        "job_title": "Software Engineer",
                        "ats_score": doc.get("ats_score", 0),
                        "keyword_match": doc.get("keyword_match", 0),
                        "missing_keywords": doc.get("missing_keywords", []),
                        "date": doc.get("created_at", ""),
                        "created_at": doc.get("created_at", ""),
                        "analysis_result": doc.get("analysis_result", {}),
                    })
            return results
        return []

    url = f"{SUPABASE_URL.rstrip('/')}/rest/v1/analyses"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url, 
                headers=headers, 
                params={
                    "user_id": f"eq.{user_id}",
                    "order": "created_at.desc"
                }
            )
            response.raise_for_status()
            docs = response.json()
            
            results = []
            for doc in docs:
                results.append({
                    "id": str(doc.get("id")),
                    "filename": doc.get("filename", "resume"),
                    "resume_name": doc.get("filename", "resume"),
                    "job_title": "Software Engineer",
                    "ats_score": doc.get("ats_score", 0),
                    "keyword_match": doc.get("keyword_match", 0),
                    "missing_keywords": doc.get("missing_keywords", []),
                    "date": doc.get("created_at", ""),
                    "created_at": doc.get("created_at", ""),
                    "analysis_result": doc.get("analysis_result", {}),
                })
            return results
    except Exception as exc:
        logger.error(f"Failed to fetch history from Supabase: {exc}")
        return []

async def delete_analysis(analysis_id: str, user_id: str) -> bool:
    headers = _get_headers()
    is_mock = os.getenv('MOCK_MODE', 'false').lower() == 'true' or not headers
    
    if is_mock:
            global _mock_db
            initial_len = len(_mock_db)
            _mock_db = [doc for doc in _mock_db if not (doc.get("id") == analysis_id and doc.get("user_id") == user_id)]
            return len(_mock_db) < initial_len
        return False

    url = f"{SUPABASE_URL.rstrip('/')}/rest/v1/analyses"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                url, 
                headers=headers, 
                params={
                    "id": f"eq.{analysis_id}",
                    "user_id": f"eq.{user_id}"
                }
            )
            response.raise_for_status()
            return True
    except Exception as exc:
        logger.error(f"Failed to delete analysis {analysis_id}: {exc}")
        return False
