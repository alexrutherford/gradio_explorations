'''Gradio demo page to expose LLM functionality'''
#import json
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

def chat_reponse(message, history):
    '''Simple catbot response function'''
    response = client.responses.create(
            model="gpt-4.1-nano",
            input = message)
    print(history)
    #print(json.dumps(json.loads(history), indent=4))
    return response.output[0].content[0].text

demo = gr.Interface(
    fn=llm_wrapper,
    inputs=["text"],
    outputs=["text"],
    api_name="predict"
)

demo = gr.ChatInterface(
    fn=chat_reponse, 
)

demo.launch()
