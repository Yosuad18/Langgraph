#Divido los chunks para que el modelo pueda procesar de mejor manera la informacion
text_splitter = RecursiveCharacterTextSplitter(
                  chunk_size=450,
                  chunk_overlap=0)

splits = text_splitter.split_documents(docs)

for index, split in enumerate(splits):
  print(f"SPLIT {index + 1}")
  print(split.page_content)
  print("--")

#Guardo esos chunks en un dataframe con los textos
chunks = []
for split in splits:
    chunks.append(split.page_content)

df = pd.DataFrame(chunks, columns= ['Text'])

# Visualiza los 10 primeros pedazos
df
