from evaluate import load

# instantiate word error rate metric
wer = load("wer")

# Save true sentence as reference
reference = data[0]['sentence']

predictions = "The quick brown fox jumps over the lazy dog"

# Compute WER BETWEEN predictions and reference
wer_score = wer.compute(predictions=[prediction], reference=[reference])
