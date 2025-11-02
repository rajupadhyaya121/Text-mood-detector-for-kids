# Text-mood-detector-for-kids
streamlit-link : https://text-mood-detector-for-kids-bxjgpnya4bcvxgz6pbkvgp.streamlit.app/
# Mood2Emoji — A Kid-Friendly Text Mood Detector
A playful mini-project designed for kids (ages 12–16) to learn how computers understand emotions in text!
This tiny web app reads a short sentence and responds with a cute emoji 😊 😐 😞 along with a friendly explanation.
Built using Python + Streamlit + TextBlob — lightweight, safe, and fun.
## 1) Getting started
### Installation
#### Clone the repository
git clone <your_repo_link_here>
cd <repo_folder>
#### Install dependencies
pip install -r requirements.txt
python -m textblob.download_corpora
#### Run the app
streamlit run app.py
## 2) How does the app works?
-The user enters a sentence.
-App checks whether input is safe (no banned words).
-TextBlob calculates polarity score (range −1 to +1).
-Based on the score:
  -> 0.3 → Happy
  -< −0.3 → Sad
-Otherwise → Neutral
-The app displays:
-Mood category
-Short explanation message

