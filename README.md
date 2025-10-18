# Mini Model Transfer Demo

This project simulates how a **research-trained model** is operationalized, versioned, documented, and validated for partner transfer — similar to how a Technical Program Manager on OpenAI’s Research IP Partnerships team might coordinate an IP hand-off to Microsoft.

---

## 🧠 Concept

Research models evolve rapidly. Before they’re shared externally, each model must be:
1. **Documented** (config, dataset, architecture, evaluation results)
2. **Versioned** (clear changelog and checksum)
3. **Validated** (functional equivalence after transfer)
4. **Auditable** (export logs and ownership trail)

This demo reproduces that workflow in miniature form using Hugging Face Transformers and custom automation.

---

## ⚙️ Quickstart

Create and activate a virtualenv, then install:
```bash
pip install -r requirements.txt
```

### Train & Save
```bash
python scripts/train.py
```

### Export (version bump + checksum + validation)
```bash
python scripts/export_bundle.py
```

### Sanity-Check Accuracy
```bash
python scripts/eval.py
```

---

## 📦 Versioned Exports

Each export creates:
```
partner_exports/
└── vX.Y.Z/
    ├── model_bundle.zip
    ├── checksum.txt
    └── transfer_log.json
```

All exports append a record to:
```
partner_exports/exports_history.jsonl
```

---

## 🗂 Structure
```
mini-model-transfer-demo/
├── model/
│   ├── config.json
│   ├── model.safetensors
│   └── model_card.md
├── scripts/
│   ├── train.py
│   ├── eval.py
│   └── export_bundle.py
├── partner_exports/
│   └── v1.0.2/
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🔎 Reproducibility & Audit

- **Checksum**: SHA-256 on the exported bundle
- **Validation**: `export_bundle.py` runs `eval.py` and captures accuracy
- **Audit trail**: JSONL log with `{version, timestamp, checksum, validation_output}`

---

## 🌐 Why This Matters

For research partnerships, speed and control must coexist.  
This repo demonstrates how to **automate reproducibility and IP governance** without slowing down research velocity — mirroring the IP hand-off rigor used for external partners.

---

## 📝 Notes

- Large artifacts are tracked with **Git LFS** via `.gitattributes`.
- Example dataset: IMDb (subset). Model: `distilbert-base-uncased`.
- For screenshots, add images to `docs/` and embed them here.

---

**Author**: Divij Mathur
