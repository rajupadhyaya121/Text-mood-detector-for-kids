# Importing the librairy
import streamlit as st
from textblob import TextBlob

# List of banned words
banned_words = ['fuck', 'bitch', 'ass', 'mf', 'hell', 'shit', 'nigga']

# Checking if words is banned
def safe_word(word):
 word=word.lower()
 for w in banned_words:
  if w in word:
   return False
 return True
   
# Function to detect mood
def get_mood(word):
 blob=TextBlob(word)
 polarity=blob.sentiment.polarity
 if polarity >0.3:
  return '😀','sentiment is happy'
 elif polarity <-0.3:
  return '😞','sentiment is sad'
 else:
  return '😐','sentiment is neutral'

# Streamlit environment setup
st.title('kid safe text mood detector') #title of hosting site
# taking input from user
sentence=st.text_input('enter a word')
# setup button that runs when user enters
if st.button('click me'):
    # if no input provided warn user
    if sentence.strip()=='':
        st.write('please enter a word')
    # if word is a safe word we proceed
    elif safe_word(sentence):
        emote,definition=get_mood(sentence)
        st.write(f" Output : {emote} & {definition}")
    else:
        st.write("Inappropirate word detected")

# Teacher Mode to visualize how app works
if st.checkbox('teacher_mode'):#displaying a teacher mode checkbox
    st.write('This app is analyzing simple word sentiment')
    st.write(' if polarity >0.3-- :), happy sentiment')
    st.write(' if polarity <-0.3-- :(, negative sentiment')
    st.write(' if neutral polarity-- \-/, neutral sentiment')










