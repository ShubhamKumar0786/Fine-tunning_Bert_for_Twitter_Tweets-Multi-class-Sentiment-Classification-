import streamlit as st
import pandas as pd
import numpy as np
from transformers import pipeline



st.tittle("Fine-tunning Bert for Twitter Tweets for Multi-class Sentiment Classification")

model="Shubham0786/bert-base-uncased-sentiment-model"
classifier=pipeline("text-classification",model=model)

text=st.text_area("Enter your tweet here", "Type Here")

if st.button("Predict"):
    result=classifier(text)
    st.write(result)