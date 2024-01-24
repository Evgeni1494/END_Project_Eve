import openai
from Open_Key import KEY
from openai import OpenAI

client = OpenAI(
    api_key = KEY
)


def generate_description(input):
    messages = [
        {
            "role":"system",
            "content":""" As a Product Description Generator, 
            Generate multi paragraph rich text product description with emoji
            from the information provided to you' \n"""
        },
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply