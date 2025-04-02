'''
ASR pipeline
'''
from transformers import pipeline

transcriber = pipeline(task="automatic-speech-recognition", model="facebook/wav2vec2-base-960h")

path = "https://cdn.vox-cdn.com/uploads/chorus_asset/file/21819139/2020-10-06_14_45_34.mp4"

sampling_rate = 16_000

dataset = dataset.cast_column('path', Audio(sampling_rate=sampling_rate))

input = data[0]['audio']['array']

prediction = transcriber(input)



# prediction over a dataset
# Create the data function
def data(n=3):
    for i in range(n):
        yield english[i]["audio"]["array"], english[i]["sentence"].lower()
        
# Predict the text for the audio file with both models
output = []
for audio, sentence in data():
    meta_pred = meta_asr(audio)["text"].lower()
    open_pred = open_asr(audio)["text"].lower()
    # Append to output list
    output.append({"sentence": sentence, "metaPred": meta_pred, "openPred": open_pred})

output_df = pd.DataFrame(output)

# Compute the WER for both models
metaWER = wer.compute(predictions=output_df["metaPred"], references=output_df["sentence"])
openWER = wer.compute(predictions=output_df["openPred"], references=output_df["sentence"])

# Print the WER
print(f"The WER for the meta model is {metaWER} and for the open model is {openWER}")