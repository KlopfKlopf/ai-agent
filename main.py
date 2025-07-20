import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():

    load_dotenv()
    args = sys.argv[1:]
    if not args:
        print("Error no prompt provided. Please retry and provide a prompt.")
        sys.exit(1)
    
    command = None

    if len(args) > 1:
        command = args[1]
    
    user_prompt = args[0]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    prompt_tokens = response.usage_metadata.prompt_token_count
    candidate_tokens = response.usage_metadata.candidates_token_count
    
    if command == "--verbose":
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {candidate_tokens}")
    
    print(response.text)

if __name__ == "__main__":
    main()
