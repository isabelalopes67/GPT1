import streamlit as st

st.title("Pizzaria Renascer")

nome = st.text_input("Digite o seu nome")
cidade = st.text_input("Digite sua cidade")
bairro = st.text_input("Digite o seu bairro")

pizza = st.selectbox(
    "Escolha o sabor da sua pizza",
    ["Calabresa", "Portuguesa", "Quatro Queijos"]
)

if st.button("Enviar Pesquisa"):
    if nome and cidade and bairro:
        st.success(
            f"Obrigado, {nome}! Você é de {cidade}, do bairro {bairro} e sua pizza é {pizza}."
        )
    else:
        st.error("Preencha todos os campos.")