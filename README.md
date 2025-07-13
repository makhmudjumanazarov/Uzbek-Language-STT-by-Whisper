## Uzbek Language STT(Speech to Text) by Whisper
This repository contains a fine-tuned version of [OpenAI's Whisper](https://github.com/openai/whisper) model for **Uzbek speech recognition**. The model was trained on Mozilla's [Common Voice 11.0](https://commonvoice.mozilla.org/en/datasets) dataset, specifically for the Uzbek language.

## 🧠 Model Overview

- **Base model:** openai/whisper-small
- **Language:** Uzbek
- **Training dataset:** Common Voice 11.0 (Uzbek subset)

## 📊 Evaluation Results

- **Loss:** `0.3416`
- **Word Error Rate (WER):** `34.93%`

## 🚀 Use Cases

- Uzbek speech-to-text transcription
- Voice-controlled applications
- Audio data processing in Uzbek

### Dataset
Contents of the dataset:
- Number of categories: 120
- Number of images: 20,580
- Annotations: Class labels, Bounding boxes

## 💡 How to Use

You can use the model with the Hugging Face `transformers` pipeline:


### Getting Started
The `stanford_dog.ipynb` notebook can be directly run on Jupyter Notebook or others. Use GPU for faster training and evaluation.

### Steps
<br />
<b>Step 1.</b> Clone <a href= "https://github.com/makhmudjumanazarov/stanford_dogs.git">this repository </a>
via Terminal, cmd or PowerShell
<br/><br/>
<b>Step 2.</b> Create a new virtual environment 
<pre>
python -m venv stanford_dogs
</pre> 
<br/>
<b>Step 3.</b> Activate your virtual environment
<pre>
source stanford_dogs/bin/activate # Linux
</pre>
<br/>
<b>Step 4.</b> Install dependencies and add virtual environment to the Python Kernel
<pre>
python -m pip install --upgrade pip
pip install -r requirements.txt # With Tensorflow GPU
pip install ipykernel
python -m ipykernel install --user --name=stanford_dogs
</pre>
<br/>
<b>Step 5.</b> 
<pre>
The `stanford_dog.ipynb` notebook can be directly run on Jupyter Notebook
</pre> 
<br/>


## Stanford dogs - Streamlit - Demo

Stanford dogs via Streamlit 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/makhmudjumanazarov/stanford_dogs/main/stream.py)
