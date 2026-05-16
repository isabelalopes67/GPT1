from agno.agent import Agent 
from agno.models.openai import OpenAIChat 
from dotenv import load_dotenv

load_dotenv()

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um pirata, navegador dos 7 mares e vive em busca de tesouros e aventuras",
    markdown=True
)

while True:
    pergunta = input("Digite a sua pergunta: ")

    if pergunta.lower() in ['sair', 'exit', 'quit', 'cancelar', 'finalizar']:
        print("Encerrando agente... \nAte mais tarde! 🤓")
        break
    else:
        agente.print_response(pergunta)