from datasets import load_dataset
from transformers import (AutoTokenizer, AutoModelForSequenceClassification,
                          TrainingArguments, Trainer)
import evaluate, numpy as np

# 1. Load a small dataset (5000 samples)
dataset = load_dataset("imdb", split="train[:5000]").train_test_split(0.2)

# 2. Tokenize text
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
def tokenize_fn(x):
    return tokenizer(x["text"], truncation=True, padding="max_length", max_length=256)
tokenized = dataset.map(tokenize_fn, batched=True)

# 3. Initialize model
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

# 4. Define evaluation metric
metric = evaluate.load("accuracy")
def compute_metrics(p):
    preds = np.argmax(p.predictions, axis=1)
    return {"accuracy": metric.compute(predictions=preds, references=p.label_ids)["accuracy"]}

# 5. Training args
args = TrainingArguments(
    output_dir="./model",
    eval_strategy="epoch",
    per_device_train_batch_size=8,
    num_train_epochs=1,
    save_total_limit=1,
    logging_dir="./logs",
)

# 6. Train and evaluate
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["test"],
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)

trainer.train()
results = trainer.evaluate()

# 7. Save model + tokenizer
trainer.save_model("./model")
tokenizer.save_pretrained("./model")

print("✅ Training complete. Eval results:", results)