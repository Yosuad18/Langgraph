#Usamos el modelo de embredding de OpenAI"
from langchain_openai import OpenAIEmbeddings
embeddings_model = OpenAIEmbeddings()

#Creamos una funcion que da el embedding dado un texto
def embedding_get (text):
    text_embeddings = embeddings_model.embed_query(text)
    return text_embeddings

# Calculamos los embeddings para cada texto en nuestro dataframe
df['Embeddings'] = df ['Text'].apply(embeddings_fn)

#Desplegamos resultado en tablas
df.head(10)

# Vemos dimensiones de vector
len(df['Embeddings'][0])