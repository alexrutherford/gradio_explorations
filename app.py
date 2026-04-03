import gradio as gr
import os
import openai

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

def llm_wrapper(name):
    return None

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
    api_name="predict"
)

demo.launch()