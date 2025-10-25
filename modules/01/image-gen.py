import os
import base64
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash-image')

prompt = "Create an image of a nano-sized banana sitting on a fingertip."
response = model.generate_content([prompt])

generated_img = base64.b64decode(response.parts[0].inline_data.data)
with open('edited_nano_banana.png', 'wb') as out:
    out.write(generated_img)