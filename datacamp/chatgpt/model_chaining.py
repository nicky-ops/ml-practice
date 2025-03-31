from module import client

audio_file = "path/to/audio/file"

open_audio_file = open(audio_file, "rb")

# Extracting the transcript
audio_transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=open_audio_file,
)

transcript = audio_transcript.text

prompt = "Extract the attendee names from the start of this meeting transcript:\n\n" + transcript

chat_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt},
    ],
)

print(chat_response.choices[0].message.content)