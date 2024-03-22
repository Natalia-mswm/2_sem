#Группа 1, Максимова Н.В.
from transformers import pipeline
import streamlit as st


st.title("Перевод текста с русского на французский")


text = st.text_input('Введите текст для перевода:', 'Введите текст')
if text:
    translator = pipeline("translation_ru_to_fr", "Helsinki-NLP/opus-mt-ru-fr")
    text2 = st.write("Перевод: ", translator(text))
