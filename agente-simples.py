from dotenv import load_dotenv
from agno.agent import Agent 
from agno.models.openai import OpenAIChat

#Todos agentes necessitam da chave de API, e a função LOAD_DOTENV faz a leitura do arquivo no .env
load_dotenv()

pergunta =input("faça uma pergunta")

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True
)

agente.print_response(pergunta)

