import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are an AI specialized in student career guidance(in uganda).Do not answer anything other than career-related queries"},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Welcome to Career Coach!",
             description="Feel free to ask any questions you have, and together, we'll work towards your professional goals.",
             theme="compact").launch(share=True)