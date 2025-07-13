## Uzbek Language STT(Speech to Text) by Whisper
### Description
This is a fine-tuned version of OpenAI's Whisper model for Uzbek speech recognition, trained on the Common Voice 11.0 dataset.

Performance on evaluation set:
    - WER (Word Error Rate): 34.93%
    - Loss: 0.3416

Ideal for transcribing Uzbek audio with Whisper Small accuracy.

### Dataset
Contents of the dataset:
- Number of categories: 120
- Number of images: 20,580
- Annotations: Class labels, Bounding boxes

The dataset can be downloaded from <a href= "http://vision.stanford.edu/aditya86/ImageNetDogs/">here.</a>

Sample images of 9 different categories from the dataset:

![Images of Dogs](/images/dog_images.png)

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
