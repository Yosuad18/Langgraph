## Hacer un entorno y activarlo 
uv venv ai_env
ai_env\Scripts\activate

## Tener en uv install:
"uv pip install langchain langgraph langchain-google-genai langchain-ollama pypdf matplotlib numpy pandas notebook"

## Poner todo a trabajar
# Opción A: Generar el archivo con versiones exactas (Recomendado para producción)
uv pip freeze > requirements.txt

## Descargar TODO
uv pip install -r requirements.txt