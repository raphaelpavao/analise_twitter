# Bibliotecas
from pymongo import MongoClient
from datetime import datetime
import tweepy
import json
from get_feeling import classificafrase

# Conexão com o mongo
client = MongoClient('localhost',27017)
db = client['tweeter_trends']
collection_trending = db.trends_data
collection_tweets = db.trends_tweets
collection_graph = db.data_graph

#tokens do twitter
consumer_key = 'pjNgrO3UcrqhbRVrRfl5m04NE' # api key
consumer_secret = 'XOEPbCyBJaS1Ey88Ay1iTzkPTBpOVM6GK4oyh4AwJ0tgG6RXyM' #api key secret
access_token = '1437561887953235969-P0PVeCHxNhhSHCldzG1VDMltLXvs0Z' #acess token
access_token_secret = 'spGIchQsqdDCidLOPuz3n5xACCKEKvzN7ctGrZffmTt0H' 

#autenticação e execução das APIs
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

#id para pegar os trend topcis do Brasil
brazil_woe_id = 23424768

#busca os trending topics
trends = api.trends_place(brazil_woe_id)

textos = []
data = (datetime.today()).strftime('%Y-%m-%d')
hora = (datetime.today()).strftime('%H:%M')

#loop para ler o dicionário com os trending topics e inserí-los no banco
for trend in trends[0]["trends"]:
    #deleta campos desnecessários e insere a data
    del trend['url']
    del trend['promoted_content']
    del trend['query']
    #adiciona data e hora
    trend["data"] = data
    trend["hora"] = hora
    #Observado que trends com volume menor que 10.000, retornam "None" na API Esse If coloca o volume em 9.999 nestes casos
    if trend['tweet_volume'] is None:
        trend['tweet_volume']=9999

    #Insere o registro
    collection_trending.insert_one(trend)

    #busca 100 tweets que tenha a expressão no trend
    search = api.search(q=trend['name'])
    for tweet in search['statuses']:
        #verifica se o idioma é português
        if tweet['lang'] == "pt":
            #associa só os campos necessários para gravar no banco
            ntweet = {}
            ntweet['text'] = tweet['text']
            ntweet["data"] = data
            ntweet["hora"] = hora
            #Insere o registro
            collection_tweets.insert_one(ntweet)
            textos.append(ntweet['text'])
#envia todos os textos dos tweets para serem classificados
sentimento = classificafrase(textos)

#acrescenta data e hora e insere no banco
sentimento["data"] = data
sentimento["hora"] = hora
collection_graph.insert_one(sentimento)

