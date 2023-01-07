import os
import openai

OPENAI_API_KEY = "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"
#openai.api_key = os.getenv(OPENAI_API_KEY)
openai.api_key = OPENAI_API_KEY

def ask(question):
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.3,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )   
    return completion.choices[0].text

