import os
import gradio as gr
from openai import OpenAI

client = OpenAI()


def greet(name, intensity):
    '''Helper function to add exclamations'''
    return "Hello, " + name + "!" * int(intensity)

def llm_wrapper(name):
    '''Helper function to do a simple LLM call'''
    response = client.responses.create(
            model="gpt-4.1-nano",
            input='Say hello to ' + name + 'in Russian')
    return response.output[0].content[0].text

demo = gr.Interface(
    fn=llm_wrapper,
    inputs=["text"],
    outputs=["text"],
    api_name="predict"
)

demo.launch()
