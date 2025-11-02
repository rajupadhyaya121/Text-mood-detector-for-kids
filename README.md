# Kid-Safe Text-Mood Detector (Curriculum Developer Intern Project)

This project is a lightweight web tool that evaluates the emotional tone of a short text input and returns a kid-friendly mood output (such as 😊, 😔, or 😐).  
It is developed using Python along with Streamlit for the interface and TextBlob for basic sentiment scoring.  
The system also performs a simple language safety check to keep the tool appropriate for learners aged 12–16.

---

## 1. Setup and Run Instructions

Follow the steps below to run this application on your system:

1. **Clone the repository**
    ```bash
    git clone <YOUR_GITHUB_REPO_LINK>
    cd <REPO_DIRECTORY>
    ```

2. **Install required packages**  
   Make sure you have Python 3.9+ installed, then run:
    ```bash
    pip install -r requirements.txt
    python -m textblob.download_corpora
    ```

3. **Launch the Streamlit app**
    ```bash
    streamlit run app.py
    ```

---

## 2. What the Project Does and How Students Benefit

**Summary:**  
The app accepts a user-provided sentence and converts it into a numerical *polarity score* (from −1 to +1).  
Based on this value, the program labels the mood as happy, neutral, or sad.  
A basic word-filtering step ensures the input remains suitable for kids.

**Key Learning Outcomes (Ages 12–16):**
- Understanding how computers interpret language
- Intro to text sentiment scoring
- Learning simple rule-based classification (e.g., IF polarity > threshold → happy)
- Recognizing how numerical values can represent emotional tone

---

## 3. Teaching Approach — Approx. 60 Minutes

The session is designed around **Explain → Demonstrate → Explore**.

* **10 min — Introduction**
  * Discuss how machines attempt to understand written language

* **25 min — Demonstration + Explanation**
  * Show how the app takes text and produces a mood label
  * Use Teacher Mode to show polarity scores and the decision logic

* **20 min — Student Activity**
  * Students test sentences and observe results  
  * Encourage them to explore tricky examples (e.g., sarcasm)

* **5 min — Recap**
  * Review the rules used to classify text
  * Discuss why incorrect predictions occur and why safety filters matter
 
---


## 4. Known Limitations

* **Difficulty with Sarcasm or Indirect Tone:**  
  Since the approach depends on simple polarity scores, it usually misses sarcastic expressions where the intended meaning differs from the literal wording.

* **Limited Understanding of Informal Language / Slang:**  
  Sentences that use regional expressions, casual slang, or mixed languages may not be interpreted accurately.

* **Struggles with Complex Phrasing:**  
  Cases containing layered wording (e.g., “I’m not unhappy”) can lead to unclear or incorrect sentiment evaluation because basic polarity analysis cannot capture nuanced context.

