def find_best_passage(query, dataframe):
  """
  Calcula las distancias entre la consulta y cada documento en el marco de datos utilizando el producto punto.
  """
  query_embedding = embeddings_model.embed_query(query)

  # Revisa como opera la función dot aquí: https://numpy.org/doc/stable/reference/generated/numpy.dot.html
  dot_products = np.dot(np.stack(dataframe['Embeddings']), query_embedding)

  # Obtiene la ID del que más se parece
  idx = np.argmax(dot_products)

  return dataframe.iloc[idx]['Text'] # Devuelve el texto del índice con el valor máximo.