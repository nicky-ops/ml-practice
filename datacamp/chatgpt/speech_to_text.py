from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

audio_file = "path/to/audio/file"

open_audio_file = open(audio_file, "rb")

# Creating a transcript
response = openai.audio.transcriptions.create(
    model="whisper-1",
    file=open_audio_file,
)

#  Extracting the transcript
print(response.text)