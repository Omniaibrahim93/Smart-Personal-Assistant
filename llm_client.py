import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_llm(prompt: str) -> str:
    if not openai.api_key:
        return "Error: OpenAI API key not found. Please set OPENAI_API_KEY environment variable."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7,
        )
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        return f"Error contacting LLM: {str(e)}"
