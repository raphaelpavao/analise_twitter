# Bibliotecas
from tkinter import *
import os
from get_graph_feelings import get_graph_feelings
os.chdir('/scripts')
from get_graph_trends import get_graph_trends

app = Tk()
app.geometry('500x300')
app.title("Análise de dados do Twitter")

Label(app,text="Gráfico de barras do Trending Topics").place(x=10,y=10,height=30)
Button(app,text='Obter Gráfico',command=get_graph_trends).place(x=10,y=40,height=20)
Label(app,text="(Retorna a última coleta obtida)").place(x=10,y=65,height=20)

Label(app,text="Gráfico de sentimento").place(x=10,y=200,height=30)
Button(app,text='Obter Gráfico',command=get_graph_feelings).place(x=10,y=230,height=20)
Label(app,text="(Retorna as 10 últimas análises feitas)").place(x=10,y=255,height=20)
app.mainloop()
