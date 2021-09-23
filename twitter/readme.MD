# Módulo "grafic_interface.py"
## _Interface com o usuário_
Esse módulo disponibiliza 2 botões para que sejam gerados os gráficos:
- Gráfico de Trending Topic por volume.
- Gráfico de sentimento por pontos medidos.

# Módulo "get_data.py"
## _Busca de dados e inserção no banco_
Esse módulo deve rodar com agendamento na frequência que desejar obter os dados do twiiter. São executadas as seguintes tarefas
- API de consulta dos Trending Topics do Twitter.
- O resultado é inserido no banco.
- Para cada assunto é executada a API que busca tweets com o assunto.
- O resuldado é inserido no banco.
- Cada frase passa por um classificador de sentimentos (módulo 'get_feeling').
- A somatória de cada sentimento é inserida no banco.

# Módulos "get_graph_trends.py" e "get_graph_feelings.py"
## _Obtem dados para fazer os gráficos_
Módulo simples que, ao ser acionado pela interface gráfica:
- Coleta informação do banco.
- Monta o gráfico usando matplotlib.

# Módulo "get_feeling.py"
## _Classifica as frases em sentimentos_
Módulo usa a biblioteca nltk de linguagem natural para tratar o texto e o algorítimo de classificação Naive Bayes. Esse módulo já está com uma base de treino. Cada frase é classificada em:
- Alegria
- Desgosto
- Medo
- Raiva
- Surpresa
- Tristeza