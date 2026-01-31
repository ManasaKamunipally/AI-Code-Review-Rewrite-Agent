from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Local imports (make sure these files exist in the same folder)
from schemas import CodeRequest
from groq_client import call_llm
from parser import parse_review_response

app = FastAPI(
    title="AI Code Review & Rewrite Agent",
    description="API to review and rewrite code using LLMs",
    version="1.0.0"
)

# Enable CORS (for frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Health / Root Endpoint
# -------------------------
@app.get("/")
def read_root():
    return {
        "message": "AI Code Review & Rewrite Agent is running",
        "endpoints": {
            "review": "/review",
            "rewrite": "/rewrite",
            "docs": "/docs"
        }
    }

# -------------------------
# Review Code Endpoint
# -------------------------
@app.post("/review")
def review_code(req: CodeRequest):
    if not req.code or not req.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")

    focus = ", ".join(req.focus_areas)

    prompt = f"""
You are an expert code reviewer.

Language: {req.language}
Focus Areas: {focus}

Review the following code and classify issues as:
Critical, High, Medium, Low.
Also suggest improvements.

Code:
{req.code}
"""

    llm_output = call_llm(prompt)
    structured_review = parse_review_response(llm_output)

    return {
        "raw_review": llm_output,
        "structured_review": structured_review
    }

# -------------------------
# Rewrite Code Endpoint
# -------------------------
@app.post("/rewrite")
def rewrite_code(req: CodeRequest):
    if not req.code or not req.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")

    prompt = f"""
You are an expert software engineer.

Rewrite the following {req.language} code with MULTIPLE implementation approaches.

Requirements:
1. Provide 3 different logic approaches for the same functionality
2. Each approach should be executable and production-ready
3. Include detailed comments
4. Add
