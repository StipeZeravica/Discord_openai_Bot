import openai
from dotenv import load_dotenv
import os


load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')


def chatgpt_response(prompt):
    response=openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=100
    )
    response_Dict = response.get("choices")
    if response_Dict and len(response_Dict)>0:
        response = response_Dict[0]["text"]
    return response