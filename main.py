import openai
import os
import pandas as pd
import time
import config
import crowling_function
import setting_gpt
import datetime


if __name__ == '__main__':
    # exit()
    # print("test")
    keywords=set()
    keywords.add("정부")
    keywords.add("삼성")
    keywords=list(keywords)

    urls=[]

    urls=crowling_function.collect_urls(keywords)

    for i in urls:
        print(i)


    # openai.api_key=config.api_key
    #
    # prompt = "Hello"
    # response = setting_gpt.get_completion(prompt)
    #
    # print(response)

    exit(0)
