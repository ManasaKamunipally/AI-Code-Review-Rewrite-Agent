# AI Code Review & Rewrite Agent

A web application that reviews and rewrites source code using Groq's Llama 3.3 70B model.

## Features

- **Code Review**: Get severity-based reviews (Critical, High, Medium, Low)
- **Code Rewriting**: Optimize and improve code quality
- **Multi-language Support**: Python, Java, JavaScript, C++
- **Modern UI**: Clean interface with Tailwind CSS
- **Syntax Highlighting**: Powered by Highlight.js

## Tech Stack

- **Backend**: FastAPI, Python, Groq SDK
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **AI Model**: Groq Llama 3.3 70B

## Setup

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your Groq API key:
   - Open the `.env` file
   - Replace `your_api_key_here` with your actual Groq API key

4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

The backend will be running on `http://127.0.0.1:8000`

### Frontend Setup

1. Open `frontend/index.html` in your web browser
2. The frontend will automatically connect to the backend API

## Usage

1. **Paste your code** in the textarea
2. **Select the programming language** from the dropdown
3. **Click "Review"** to get a severity-based code review
4. **Click "Rewrite"** to get an optimized version of your code

## API Endpoints

### POST /review
Reviews code and provides severity-based feedback.

**Request Body:**
```json
{
  "code": "your code here",
  "language": "Python",
  "focus_areas": ["bugs", "performance", "security"]
}
```

**Response:**
```json
{
  "raw_review": "LLM review text",
  "structured_review": {
    "Critical": [],
    "High": [],
    "Medium": [],
    "Low": []
  }
}
```

### POST /rewrite
Rewrites and optimizes the provided code.

**Request Body:**
```json
{
  "code": "your code here",
  "language": "Python",
  "focus_areas": []
}
```

**Response:**
```json
{
  "rewritten_code": "optimized code"
}
```

## Project Structure

```
ai-code-review-agent/
├── backend/
│   ├── main.py          # FastAPI application
│   ├── groq_client.py   # Groq API client
│   ├── parser.py        # Response parser
│   ├── schemas.py       # Pydantic models
│   ├── requirements.txt # Python dependencies
│   └── .env            # Environment variables
└── frontend/
    └── index.html      # Web interface
```

## Requirements

- Python 3.7+
- Groq API key
- Modern web browser

## License

MIT License
