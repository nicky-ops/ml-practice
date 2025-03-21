from module import client


audio_file = "path/to/audio/file"

open_audio_file = open(audio_file, "rb")

# Creating a translation
response = client.audio.translations.create(
    model="whisper-1",
    file=open_audio_file,
)

print(response.text)