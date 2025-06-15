import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk, cv2, torch
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from PIL import Image
from gtts import gTTS
import tempfile
import os
from io import BytesIO

# Ensure required nltk data
for pkg in ["punkt"]:
    try:
        nltk.data.find(f"tokenizers/{pkg}")
    except LookupError:
        nltk.download(pkg)

# Initialize models
quiz_generator = pipeline("text-generation", model="gpt2")
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Default dataset
lesson_data = pd.DataFrame({
    'lesson': ["Introduction to AI", "Deep Learning", "NLP Basics"],
    'engagement_score': [80, 90, 70]
})

def load_csv_data(file_path):
    df = pd.read_csv(file_path)
    if "lesson" not in df or "engagement_score" not in df:
        raise ValueError("CSV must contain 'lesson' and 'engagement_score'")
    return df

def generate_quiz(prompt):
    return quiz_generator(prompt, max_length=40, num_return_sequences=1)[0]['generated_text']

def tokenize_text(prompt):
    return word_tokenize(prompt)

def extract_keywords(prompt):
    return CountVectorizer(stop_words="english", max_features=10).fit([prompt]).get_feature_names_out()

def recommend_similar(prompt):
    sims = cosine_similarity(
        embedder.encode([prompt]),
        embedder.encode(lesson_data['lesson'].tolist())
    )[0]
    idx = sims.argmax()
    return lesson_data['lesson'].iloc[idx]

def dynamic_plot(prompt):
    df = lesson_data.copy()
    tfidf = TfidfVectorizer().fit_transform(df['lesson'])
    inp_vec = TfidfVectorizer().fit(df['lesson'].tolist() + [prompt]).transform([prompt])
    sims = cosine_similarity(inp_vec, tfidf)[0]
    df['score'] = sims * df['engagement_score']
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x='lesson', y='score', data=df, ax=ax)
    ax.set_title("Similarity-weighted Engagement")
    plt.xticks(rotation=45)
    buf = BytesIO()
    plt.tight_layout()
    fig.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return buf

def ar_process(pil_image):
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2GRAY)
    _, th = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    return Image.fromarray(th)

def tts(prompt):
    temp_path = tempfile.mktemp(suffix=".mp3")
    gTTS(prompt).save(temp_path)
    return temp_path