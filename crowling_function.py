from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/98.0.4758.102"}

def settingPageNum():
    return

def collect_news():
    return

def news_attrs_crawler(articles,attrs):
    attrs_content=[]
    for i in articles:
        attrs_content.append(i.attrs[attrs])
    return attrs_content

def articles_url(url):

    original_html = requests.get(url, headers=headers)
    html = BeautifulSoup(original_html.text, "html.parser")

    url_naver = html.select(
        "div.group_news > ul.list_news > li div.news_area > a.news_tit")

    url = news_attrs_crawler(url_naver, 'href')

    return url


def collect_urls(keyword):
    all_urls=[]
    for news_num in range(5):

        url="https://search.naver.com/search.naver?where=news&query="+keyword+"&nso=so%3Add%2Cp%3Afrom20210113to20210114&start="+str(1+news_num*10)
        result=articles_url(url)
        if len(result)==0:
            break
        else:
            all_urls.extend(result)
    return all_urls
