import gradio as gr
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import numpy as np
import torch

# Device and data type
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

# Load the model and processor from local path
model_id = "/home/makhmud/Whisper brb/model/whisper-uzbek/"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id,
    torch_dtype=torch_dtype,
    low_cpu_mem_usage=True,
    use_safetensors=True
).to(device)

processor = AutoProcessor.from_pretrained(model_id)

transcriber = pipeline(
    "automatic-speech-recognition", 
    model=model, 
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor
    )

def transcribe(audio):
    sr, y = audio
    
    # Convert to mono if stereo
    if y.ndim > 1:
        y = y.mean(axis=1)
        
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))

    return transcriber({"sampling_rate": sr, "raw": y})["text"]  

demo = gr.Interface(
    transcribe,
    gr.Audio(sources="microphone"),
    "text",
)

demo.launch()
