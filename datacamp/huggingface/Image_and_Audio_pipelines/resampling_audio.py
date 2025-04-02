from datasets import Audio


songs = songs.cast_column('audio', Audio(sampling_rate=16_000))

# finding sampling rate

print(songs[0]['audio']['sampling_rate'])