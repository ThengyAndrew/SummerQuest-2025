from transformers import AutoTokenizer

# HF name or local path
tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")

sequence = "Using a Transformer network is simple"
tokens = tokenizer.tokenize(sequence)

print(tokens)
