import requests
import json
import re

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:7b"


def call_llm(system_prompt, user_prompt):
    payload = {"model": MODEL_NAME,
               "prompt": f"SYSTEM: {system_prompt}\n\nUSER: {user_prompt}", "stream": False}
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        return response.json()['response']
    except Exception as e:
        print(f"Error: {e}")
        return "{}"


def extract_json(llm_output):
    try:
        # Regex to find JSON even if the LLM talks before/after it
        match = re.search(r'\{[\s\S]*\}', llm_output)
        return json.loads(match.group(0)) if match else None
    except:
        return None
