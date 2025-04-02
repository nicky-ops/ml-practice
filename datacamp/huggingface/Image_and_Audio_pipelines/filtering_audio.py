import librosa

durations = []

for row in songs['path']:
    durations.append(librosa.get_duration(path=row))


songs.add_column('duration', durations)

songs = dataset.filter(
    lambda x: x < 30, input_columns=['duration']
)