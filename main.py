import openai
import os
import pandas as pd
import time
import config

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages=[{"role": "user", "content": prompt}]
    response=openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

if __name__ == '__main__':
    exit()
    # print("test")

    # openai.api_key=config.api_key
    #
    #
    # prompt = ""
    # response=get_completion(prompt)
    #
    #
    #
    # print(response)