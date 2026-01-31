import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()


client = Groq(api_key=os.getenv("GROQ_API_KEY"))


MODEL_NAME = "llama-3.3-70b-versatile"




def call_llm(prompt: str):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=1200,
        top_p=0.9
    )
    return response.choices[0].message.content
