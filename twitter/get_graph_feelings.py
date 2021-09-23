# Bibliotecas
import matplotlib.pyplot as plt
from pymongo import MongoClient

# Conexão com o mongo
client = MongoClient('localhost',27017)
db = client['tweeter_trends']
collection_graph = db.data_graph



def get_graph_feelings():
    feelings = collection_graph.find().sort('_id',-1).limit(10)

    hora     = []
    alegria  = []
    desgosto = []
    medo     = [] 
    raiva    = []
    surpresa = []
    tristeza = []

    for feel in feelings:
        hora.append(feel['hora'])
        alegria.append(feel['alegria'])
        desgosto.append(feel['desgosto'])
        medo.append(feel['medo'])
        raiva.append(feel['raiva'])
        surpresa.append(feel['surpresa'])
        tristeza.append(feel['tristeza'])

    hora = hora[::-1]
    #Preparação da área do gráfico
    plt.style.use('ggplot')
    plt.xlabel('Hora')
    plt.ylabel('Pontos')
    plt.plot(hora,alegria, label = 'Alegria')
    plt.plot(hora,desgosto, label = 'Desgosto')
    plt.plot(hora,medo, label = 'Medo')
    plt.plot(hora,raiva, label = 'Raiva')
    plt.plot(hora,surpresa, label = 'Surpresa')
    plt.plot(hora,tristeza, label = 'Tristeza')
    plt.legend()    
    #Faz a demonstração do gráfico
    plt.show()
#get_graph_feelings()