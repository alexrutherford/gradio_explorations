import gradio as gr
import os
import openai

from openai import OpenAI

client = OpenAI()


def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

def llm_wrapper(name,intensity):

    response = client.responses.create(
            model="gpt-4.1-nano",
            input='Say hello to ' + name + 'in Russian')
    return response.output[0].content[0].text

demo = gr.Interface(
    fn=llm_wrapper,
    inputs=["text", "slider"],
    outputs=["text"],
    api_name="predict"
)

demo.launch()