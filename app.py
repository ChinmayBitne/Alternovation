import gradio as gr
import requests
import io
from PIL import Image
from catboost import CatBoostRegressor
from web import HTMLCode, CSSCode, footCode
import numpy as np
import joblib

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
headers = {"Authorization": f"Bearer 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"}
defaultprompt = "round table with blue color and smooth edges, places in the living room"

main_model = CatBoostRegressor()
main_model.load_model("model.cbm")

pred_vol = joblib.load('model_predvol.pkl')
pred_wei = joblib.load('model_predwei.pkl')

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def stablefurniture(originalprompt, ftype, purpose, texture, length, width, height):
    prompt = f"full {ftype} places in the living room {originalprompt} {texture} texture for {purpose}, having {int(length)} millimeter length, {int(width)} millimeter width, and {int(height)} millimeter height, hd quality, full furniture, hyperrealistic, highly detailed, sharp focus, cinematic lighting, for commercial website"
    print(prompt)
    image_bytes = query(
        {
            "inputs": prompt,
        }
    )
    image = Image.open(io.BytesIO(image_bytes)).convert("RGBA")
    vol_pred = pred_vol.predict([[length, width, height]])
    wei_pred = pred_wei.predict([[length, width, height, vol_pred[0]]])
    prediction = main_model.predict([length, width, height, vol_pred[0], wei_pred[0]])
    rubles = "₽ " + str(np.round(prediction))
    return image, rubles

with gr.Blocks(theme=gr.themes.Soft(), css=CSSCode) as demo:
    gr.HTML(HTMLCode)
    with gr.Row():
        with gr.Column(scale=1, min_width=600):
            with gr.Row():
                originalprompt = gr.Textbox(label="Prompt",default=defaultprompt)
            with gr.Row():
                ftype = gr.Dropdown(
                    [
                        "Table",
                        "Rack",
                        "Closet",
                        "Cabinet",
                        "Roll-out stand",
                        "Pedestal",
                        "Screen",
                        "Console",
                        "Reception Desk",
                        "Mezzanine",
                        "Penalty",
                        "Classical",
                    ],
                    label="Type",
                    info="Which type of furniture are you looking for?",
                )
                purpose = gr.Dropdown(
                    [
                        "computer",
                        "for clothes",
                        "for documents",
                        "for negotiations",
                        "for office",
                        "for office equipment",
                        "for receptionists",
                        "for magazine",
                        "roll-out stand",
                        "writing",
                    ],
                    label="Purpose",
                    info="How may your furnityre help you?",
                )
                texture = gr.Dropdown(
                    [
                        "Beech",
                        "Oak",
                        "Kraft white",
                        "Sonoma oak Light",
                        "Craft Golden",
                        "Wenge/Oak",
                        "Nut",
                        "Wine",
                        "Grey",
                        "Oak Cronberg",
                        "Cherry",
                    ],
                    label="Texture",
                    info="How would you like it to be?",
                )
            with gr.Row():
                length = gr.Number(label="Length")
                width = gr.Number(label="Width")
                height = gr.Number(label="Height")
            btn = gr.Button("Dream")
            prediction = gr.Textbox(label="Estimated Cost")
        with gr.Column(scale=2, min_width=600):
            furniture = gr.Image().style(height=580)
    btn.click(
        stablefurniture,
        inputs=[originalprompt, ftype, texture, purpose, length, width, height],
        outputs=[furniture, prediction],
    )
    with gr.Row():
        gr.HTML(footCode)

demo.launch()