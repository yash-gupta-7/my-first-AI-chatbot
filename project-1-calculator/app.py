import gradio as gr
from calculator import calculate
from gradio.themes import Soft
import json 
import os

branding_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'branding.json'))

with open(branding_path) as f:
    brand_data = json.load(f)["brand"]

gr.Interface(
    fn=calculate,
    inputs =[
        gr.Number(label = "First Number"),
        gr.Radio(["+","-","*","/"], label="Operator"),
        gr.Number(label="Second Number")
    ],
    outputs=gr.Textbox(label="Result"),
    title=brand_data["organizationShortName"],
    description=brand_data["slogan"],
    
).launch(theme=Soft())