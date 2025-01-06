
import streamlit as st 
import os 
from dotenv import load_dotenv
import base64
from openai import OpenAI


load_dotenv()
key = os.getenv('OPEN_AI_KEY')
MODEL = 'gpt-4o'https://github.com/ElieDDD
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key = key)

def encode_image(image):
    return base64.b64encode(image.read()).decode('utf-8')

st.title('AI generated or not?')
image_file = st.file_uploader('Upload an image to test',type = ['png', 'jpg', 'jpeg'])
if image_file:
    st.image(image_file,caption = 'image')

    base64_image = encode_image(image_file)

    response = client.chat.completions.create(
        model = MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful  assistant that responds in Markdown."},
        {"role": "user", "content": [
        {"type": "text", "text": "Do you think this is an Ai generated image or not? Tell us how you make this evaluation and give us a confidence score for your evaluation."},
            {"type": "image_url", "image_url": {
            "url": f"data:image/png;base64,{base64_image}"}
                    }
                ]}
            ],
            temperature=0.0,
        )
    
    st.markdown(response.choices[0].message.content)
