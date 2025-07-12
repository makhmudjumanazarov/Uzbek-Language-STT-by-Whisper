import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import torchaudio

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "/home/makhmud/Whisper brb/model/whisper-uzbek/."

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)

# Replace the dataset loading code
audio_path = "/home/makhmud/Whisper brb/Recording.m4a"

# Load the audio file using torchaudio
waveform, sample_rate = torchaudio.load(audio_path, normalize=True, channels_first=True)
# print(waveform)

# If the audio has multiple channels, select the first channel
if waveform.shape[0] > 1:
    waveform = waveform[0, :]

# Prepare the input dictionary for the pipeline
input_dict = {"raw": waveform.numpy(), "sampling_rate": sample_rate}

# Perform automatic speech recognition on the local audio file
result = pipe(input_dict)

# Print the recognized text
print(result["text"])