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

## 💡 How to Use

You can use the model with the Hugging Face `transformers` pipeline:

### Steps
<br />
<b>Step 1.</b> Clone <a href= "https://github.com/makhmudjumanazarov/Uzbek-Language-STT-by-Whisper.git">git </a> and <a href= "https://huggingface.co/Makhmud/whisper-uzbek/tree/main?clone=true">huggingface </a> repositories
via Terminal, cmd or PowerShell
<br/><br/>
<b>Step 2.</b> Create a new virtual environment 
<pre>
python -m venv stt
</pre> 
<br/>
<b>Step 3.</b> Activate your virtual environment
<pre>
source stt/bin/activate # Linux
</pre>
<br/>
<b>Step 4.</b> Install dependencies
<pre>
python -m pip install --upgrade pip
pip install -r requirements.txt
</pre>
<br/>
<b>Step 5.</b> Run on gradio 
<pre>
python gradio_doc.py
</pre> 
<br/>

