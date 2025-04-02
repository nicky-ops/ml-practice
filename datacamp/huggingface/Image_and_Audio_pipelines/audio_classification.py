from transformers import pipeline

classifier = pipeline(task="audio-classification", model='jonatasgrosman/wav2vec2-large-xlsr-53-english')


genre_classifier = pipeline(task='audio-classification', model='mtg-upf/discogs-maest-30s-pw-73e-ts')

audio = songs[0]['audio']['array']
prediction = genre_classifier(audio)

print(prediction[0]['label'])