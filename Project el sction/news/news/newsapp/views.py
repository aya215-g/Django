from django.shortcuts import render
import requests
from newsapi.newsapi_client import NewsApiClient
import pandas as pd

# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key='a8aa13889cd942c9b6c8fda8bef9fb90')
    top_headlines = newsapi.get_top_headlines(category='sports', language='en', country='us')
    articles = top_headlines['articles']
    #title=[]
    #description=[]
    #urlToImage=[]
    #url=[]
    #for i in articles:
      #  f=articles[i]
     #   title.append(i['title'])
      #  description.append(i['description'])
       # urlToImage.append(i['urlToImage'])
        #url.append(i['url'])
    df=pd.DataFrame(articles)

    #news=zip(title,description,urlToImage,url)
    return render(request,'newsapp/index.html', {'data':df})
