# Группа 1, Максимова Н.В.
from transformers import pipeline
import streamlit as st


st.title("Перевод текста с русского на французский")
translator = pipeline("translation_ru_to_fr", "Helsinki-NLP/opus-mt-ru-fr")
input_text = st.text_input('Введите текст для перевода:', 'Введите текст')
button = st.button('Перевести')
if button:
    output_text = st.write("Перевод: ", translator(input_text))
