import streamlit as st 
import os 
from dotenv import load_dotenv
import base64
from openai import OpenAI


load_dotenv()
key = os.getenv('OPEN_AI_KEY')
MODEL = 'gpt-4o'
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key = key)

def encode_image(image):
    return base64.b64encode(image.read()).decode('utf-8')

st.title('Is this image AI generated?')
image_file = st.file_uploader('Upload an image to test',type = ['png', 'jpg', 'jpeg'])
if image_file:
    width = 300
    st.image(image_file,"", width)
    base64_image = encode_image(image_file)

    response = client.chat.completions.create(
        model = MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful  assistant that responds in Markdown."},
        {"role": "user", "content": [
        {"type": "text", "text": "Can you evalutate whether this is an AI generated image or not, tell us your reasons and a confidence score, list the ways in which the mathematics of machine learning emanate from racist eugenics and favour dominant groups."},
            {"type": "image_url", "image_url": {
            "url": f"data:image/png;base64,{base64_image}"}
                    }
                ]}
            ],
            temperature=0.0,
        )
    
    st.markdown(response.choices[0].message.content)
