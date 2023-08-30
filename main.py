import openai
import os
import pandas as pd
import time
import config
import crowling_function
import setting_gpt

if __name__ == '__main__':
    # exit()
    # print("test")
    keywords=set()
    keywords.add("파이썬")
    keywords.add("삼성")

    urls=[]
    for keyword in keywords:
        urls.extend([keyword, crowling_function.collect_urls(keyword)])


    print(urls)



    # openai.api_key=config.api_key
    #
    # prompt = "Hello"
    # response = setting_gpt.get_completion(prompt)
    #
    # print(response)

    exit(0)
