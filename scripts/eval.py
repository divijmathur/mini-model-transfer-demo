from transformers import AutoTokenizer, AutoModelForSequenceClassification
from datasets import load_dataset
import torch

model = AutoModelForSequenceClassification.from_pretrained("model")
tok = AutoTokenizer.from_pretrained("model")
data = load_dataset("imdb", split="test[:100]")

inputs = tok(list(data["text"]), truncation=True, padding=True, return_tensors="pt")
labels = torch.tensor(data["label"])
out = model(**inputs)
pred = out.logits.argmax(-1)
acc = (pred == labels).float().mean()
print(f"Post-transfer accuracy: {acc.item():.3f}")