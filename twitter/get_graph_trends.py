# Bibliotecas
import matplotlib.pyplot as plt
from pymongo import MongoClient

# Conexão com o mongo
client = MongoClient('localhost',27017)
db = client['tweeter_trends']
collection_trends = db.trends_data

def get_graph_trends():
    last_trend = collection_trends.find({},{'data','hora'}).sort('_id',-1).limit(1)
    for trend in last_trend:
        last_data = trend['data']
        last_hora = trend['hora']

    #Preparação da área do gráfico
    plt.style.use('ggplot')
    plt.subplots_adjust(top = 0.95,bottom = 0.38, left = 0.075, right = 0.95)

    plt.xticks(rotation = 90)
    plt.xlabel('Trending Topics  -  '+ last_data +' - '+ last_hora)

    plt.yscale('log')
    plt.ylabel('Volume')

    trends = collection_trends.find({'hora':last_hora,'data':last_data}).sort('tweet_volume',-1)
    for trend in trends:
        plt.bar(trend['name'],trend['tweet_volume'])   

    #Faz a demonstração do gráfico
    plt.show()
    
