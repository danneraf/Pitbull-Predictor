# Much of this project was inspired by https://github.com/ffomezolam/GA-DSI-Capstone/tree/main 

import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TFBertForSequenceClassification, BertTokenizer
import random
import numpy as np
from tensorflow.keras.preprocessing import sequence
import tensorflow as tf
from PIL import Image

rate = [
    'Not',
    'Slightly',
    'Moderately',
    'Very',
    'Pure'
]

def score_prob(prob):
    score_len = len(rate)
    score = int(prob * score_len)
    return rate[score]

# Title and user input box 
st.title('Pitbull Generator')

st.subheader('Write a few lyrics for Mr. Worldwide:')
text = st.text_input('(a fun one is to just type "help" and then click the button)')
generate = st.button('Dale!') 

# Load the trained GPT-2 
gpt_model_path = './GPT'
gpt_model = GPT2LMHeadModel.from_pretrained(gpt_model_path)
gpt_tokenizer = GPT2Tokenizer.from_pretrained(gpt_model_path)

# Set the model to generate Pitbull lyrics
gpt_model.config.prefix = ''

# Load the pre-trained BERT model and tokenizer
classification_model_path = './BERT/bert_model'
classification_model = TFBertForSequenceClassification.from_pretrained(classification_model_path, from_pt=True)
classification_tokenizer = BertTokenizer.from_pretrained('./BERT/bert_tokenizer')

# Set the maximum sequence length for padding
max_len = 128

def preprocess_lyrics(lyrics):
    inputs = classification_tokenizer.encode_plus(lyrics, add_special_tokens=True, return_tensors='tf', padding='max_length', truncation=True, max_length=max_len)
    return inputs['input_ids'], inputs['attention_mask']

def generate_lyrics(prompt):
    inputs = gpt_tokenizer.encode(prompt, return_tensors='pt')
    outputs = gpt_model.generate(inputs, max_length=100, num_beams=1, no_repeat_ngram_size=2, num_return_sequences=1)
    lyrics = gpt_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return lyrics

def generate_pitbull_lyrics(text):
    if generate:
        if text:
            lyrics = generate_lyrics(text)
            st.subheader('Generated Lyrics')
            st.write(lyrics)

            # Preprocess and classify the generated lyrics
            input_ids, attention_mask = preprocess_lyrics(lyrics)
            inputs = {'input_ids': input_ids, 'attention_mask': attention_mask}
            outputs = classification_model(inputs)
            logits = outputs.logits
            probs = tf.nn.softmax(logits, axis=-1)
            prob = probs[0][1]  

            st.subheader('Score')
            prob_percent = round(float(prob) * 100, 2)
            st.write(f'{prob_percent}%')
            st.write(f'The generated lyrics are {score_prob(prob)} Mr. 305')

        else:
            st.warning('Please enter a starting line for Pitbull lyrics')

if text:
    generate_pitbull_lyrics(text)

    
# Yes I know this button does not 'work'
# Yes it is on purpose
st.subheader('Should this artist feature Pitbull?')
st.text_input('Type the name of an artist:')

if st.button('?'):
    st.write('Yes')
else:
    st.write('Please press the button')
    
