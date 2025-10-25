# from openai import OpenAI

# client = OpenAI(
#   base_url="https://openrouter.ai/api/v1",
#   api_key="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",
# )

# completion = client.chat.completions.create(
#   model="openai/gpt-5-image-mini",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {
#           "type": "text",
#           "text": "What is in this image?"
#         },
#         {
#           "type": "image_url",
#           "image_url": {
#             "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
#           }
#         }
#       ]
#     }
#   ]
# )
# print(completion.choices[0].message.content)

import requests
import json
import base64
import os
from dotenv import load_dotenv
load_dotenv()

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('OPENROUTERAPI_KEY')}",
        "Content-Type": "application/json"
    },
    json={
        "model": "google/gemini-2.5-flash-image",  # Required. ex: "openai/gpt-4"
        "messages": [
            {"role": "user", "content": "create image of cat"}
        ]
    }
)

# print(json.dumps(response.json(), indent=2))


response_data = response.json()
# print(json.dumps(response_data, indent=2))

# Extract and save the image
if response.status_code == 200:
    try:
        # Navigate to the image data in the response
        images = response_data['choices'][0]['message']['images']
        
        for i, image_item in enumerate(images):
            # Get the base64 data URL
            data_url = image_item['image_url']['url']
            
            # Remove the data URL prefix (data:image/png;base64,)
            base64_data = data_url.split(',')[1]
            
            # Decode base64 and save as image
            image_bytes = base64.b64decode(base64_data)
            
            # Save with index if multiple images
            filename = f'generated_image_{i}.png' if len(images) > 1 else 'generated_image.png'
            
            with open(filename, 'wb') as f:
                f.write(image_bytes)
            
            print(f"Image saved as '{filename}'")
            
    except KeyError as e:
        print(f"Error extracting image data: {e}")
    except Exception as e:
        print(f"Error saving image: {e}")
else:
    print(f"Request failed with status code: {response.status_code}")

"Outputs:output.txt file created with the generated image details."