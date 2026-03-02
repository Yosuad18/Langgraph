import numpy as np
import pandas as pd
import os

from langchain_core.output_parser import StrOutputParser

#Configuracion splitter
from langchain_text_splitters import StrOutoutParser

#Configuracion LLM - GPT
from langchain_openai import ChatOpenAI

#Configuracion obtener APU desde secrets desde google Colab
from google.colab import userdata
GEMINI_API_KEY = userdata.get('OPENAI_API_KEY')
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

llm = ChatOpenAI(model="gpt-4o-mini")
