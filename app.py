# -*- coding: utf-8 -*-
"""Untitled22.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19VNcHsnPuam_eaymx24dmwikzSy0m2YF
"""

import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
from textblob import TextBlob

# Loading pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono")
tokenizer.padding_side = 'left'
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

def correct_text(input_text):
    text_blob = TextBlob(input_text)
    corrected_text = text_blob.correct()
    return str(corrected_text)

def chatbot_response(input_text):
    corrected_input_text = correct_text(input_text)
    if corrected_input_text != input_text:
        st.write("Corrected text:", corrected_input_text)
    input_ids = tokenizer.encode(corrected_input_text + tokenizer.eos_token + "", return_tensors='pt')
    chat_history_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

# Streamlit interface
st.title("Chatbot with Text Correction")
user_input = st.text_input("You: ", key="input_text")
if st.button("Send"):
    response = chatbot_response(user_input)
    st.text_area("Chat-bot:", value=response, height=100, key="response")