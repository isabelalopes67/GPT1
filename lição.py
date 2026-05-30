import streamlit as st

st.title("Cadastro RH já")

nome = st.text_input("Digite o seu nome: ")
email = st.text_input("Digite o seu email: ")

if st.button("Cadastrar"):
    if nome and email:
        st.success(f"Funcionário {nome} cadastrado com sucesso!")
        st.balloons()
    else:
        st.error("Preencha todos os campos.")    