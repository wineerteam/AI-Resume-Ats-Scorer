# ⚙️ Backend Architecture Guide (FastAPI & AI Pipelines)

This guide details the backend ecosystem, NLP models, semantic analysis engines, and PDF generation processes used in the **ATS Resume Scorer & Analyzer** application.

---

## 1. FastAPI & Uvicorn ASGI Server
### 🔍 What
- **FastAPI** is a modern, high-performance web framework for building RESTful APIs using standard Python type hints.
- **Uvicorn** is an ASGI (Asynchronous Server Gateway Interface) web server implementation for Python, running the FastAPI application.

### 💡 Why
- **Asynchronous Execution**: Native support for `async/await` enables handling thousands of concurrent requests (e.g., waiting for Groq API responses) without blocking the thread pool.
- **Auto-generated Documentation**: Automatically generates Swagger UI (`/docs`) and ReDoc (`/redoc`) API guides.
- **Type Safety**: Automatic request validation using Pydantic schemas.

### 💻 Syntax Example
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/health")
async def health_check():
    return {"status": "healthy"}
```

### 🔄 Alternates
- **Flask**: Sync-by-default, lacks built-in async support and type-hint validation.
- **Django REST Framework (DRF)**: Heavy, feature-rich, but slower startup times and larger memory footprint.

### 🎭 Analogy
FastAPI is like a **smart sushi conveyor belt restaurant**. When a customer (frontend) requests sushi, the chef (endpoint) handles the order immediately, validating the ingredients (Pydantic models) in real-time, and can serve multiple clients simultaneously using conveyor lanes (async loops).

---

## 2. Lifespan Event Handler (Model Caching)
### 🔍 What
FastAPI's **lifespan** context manager manages startup and shutdown events. We use it to load heavy machine learning models (spaCy NLP and SentenceTransformer embedders) into system memory *once* when the server starts up.

### 💡 Why
- **Latency Optimization**: Loading models from disk takes 5–10 seconds. If loaded inside a request route, every single analysis request would take 10+ seconds. Caching them in `app.state` makes individual request analysis instant.
- **Memory Management**: Keeps a single shared instance of the models in RAM rather than creating duplicates for each thread.

### 💻 Syntax Example
```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sentence_transformers import SentenceTransformer

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Load models
    app.state.embedder = SentenceTransformer("all-MiniLM-L6-v2")
    yield
    # Shutdown: Clean up resources
    del app.state.embedder
```

### 🔄 Alternates
- **Middleware Loading**: Loading on first request (Lazy loading), which causes the first user to experience a slow load time.
- **Global Variables**: Unstructured and harder to test.

### 🎭 Analogy
Lifespan loading is like a **mechanic warming up the tools before the shop opens**. Instead of making the customer wait 10 minutes while he retrieves the heavy diagnostic computer from the back room for each car, he boots it up at 8:00 AM (Startup) so it is ready for instant use.

---

## 3. spaCy NLP Pipeline (`en_core_web_md`)
### 🔍 What
**spaCy** is an industrial-strength Natural Language Processing (NLP) library in Python. We load the medium-sized English pipeline (`en_core_web_md`), which includes pre-trained word vectors.

### 💡 Why
- **Keyword Extraction & Lemmatization**: Resolves words to their base forms (e.g., "coding", "coded", "codes" all become "code") to avoid false negatives during keyword gap matching.
- **Named Entity Recognition (NER)**: Detects names, organizations, and locations inside the resume.

### 💻 Syntax Example
```python
import spacy

nlp = spacy.load("en_core_web_md")
doc = nlp("Software engineers develop scalable web services.")

# Lemmatization example
for token in doc:
    print(token.text, "->", token.lemma_)
```

### 🔄 Alternates
- **NLTK (Natural Language Toolkit)**: Good for academic research but slower and less streamlined for production applications.
- **Regular Expressions (Regex)**: Brittle; cannot handle synonyms, word endings, or contextual meaning.

### 🎭 Analogy
spaCy is like a **grammar school teacher**. Instead of reading a resume as a simple string of letters, spaCy understands grammar, parts of speech (nouns, verbs), and how words are related to each other.

---

## 4. SentenceTransformers (Semantic Similarity)
### 🔍 What
**SentenceTransformers** is a framework that computes dense vector representations (embeddings) for sentences, paragraphs, or search queries. We use `all-MiniLM-L6-v2`, which maps text to a 384-dimensional vector space.

### 💡 Why
- **Semantic Matching**: Traditional ATS matches keywords exactly. Our system matches *meaning*. If the JD requires "FastAPI" and the resume has "Python API development", the transformer scores them as highly similar (e.g., 0.85 similarity score).
- **Cosine Similarity**: Mathematically measures the angle between vectors to compare semantic alignment.

### 💻 Syntax Example
```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")
emb1 = model.encode(["Python web developer"])
emb2 = model.encode(["FastAPI API creator"])

similarity = cosine_similarity(emb1, emb2)[0][0]
```

### 🔄 Alternates
- **TF-IDF / Bag of Words**: Matches words based on frequencies; fails to understand context or synonyms.
- **OpenAI Embeddings API**: High quality, but requires paid API keys and internet requests. SentenceTransformers runs entirely offline for free.

### 🎭 Analogy
SentenceTransformers is like a **universal translator for concepts**. It turns any sentence into a GPS coordinate in a "coordinate system of meaning." If two sentences are about similar things, their coordinates will be very close to each other.

---

## 5. WeasyPrint PDF Generation Engine
### 🔍 What
**WeasyPrint** is a visual rendering engine that converts HTML documents and CSS stylesheets into standard PDF documents.

### 💡 Why
- **HTML/CSS Templating**: Building PDFs using low-level drawing libraries (like ReportLab) requires hardcoding pixel coordinates. WeasyPrint allows us to design a beautiful, modern report using standard Jinja2 HTML templates and CSS layouts.
- **W3C Standards**: Respects flexbox, web fonts, margins, and page breaks.

### 💻 Syntax Example
```python
from weasyprint import HTML

# Render HTML string directly to a PDF file
HTML(string="<h1>ATS Analysis Report</h1>").write_pdf("report.pdf")
```

### 🔄 Alternates
- **ReportLab**: High performance but extremely tedious to design and maintain.
- **pdfkit (Wkhtmltopdf wrapper)**: Requires installing system-level binary dependencies (wkhtmltopdf), which are difficult to manage in serverless production environments (like Render or Vercel). WeasyPrint runs entirely via Python dependencies.

### 🎭 Analogy
WeasyPrint is like a **digital camera taking a picture of a web page**. You write the report as if you are designing a website, and WeasyPrint freezes it into a high-quality, printable PDF sheet.
