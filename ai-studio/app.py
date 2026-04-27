from google import genai
from google.genai import types
client = genai.Client(api_key='AIzaSyD3Q4AvT3wmAMPAD6cMZs7mBu7ZZK0UVH4')

def generate_text(text):
   response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=types.Part.from_text(text='Why is the sky blue?'),
    config=types.GenerateContentConfig(
        temperature=0,
        top_p=0.95,
        top_k=20,
    ),
)
   return response.text

print(generate_text("Hello, how are you?"))