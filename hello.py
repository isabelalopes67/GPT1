import streamlit as st

st.title("Bem vindo à minha primeira página WEB")
st.subheader("Desenvolvido por: Raissa")

nome = st.text_input("Digite o seu nome: ")

if nome: 
    st.success(f"Bem vindo {nome}")
    st.balloons()