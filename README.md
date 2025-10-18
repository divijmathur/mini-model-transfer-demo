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


=======
# Mini Model Transfer Pipeline

This project simulates an internal Research-to-Partner IP transfer flow.

## Overview
We fine-tune a DistilBERT model on IMDb movie reviews (5k sample), generate documentation and metadata, and export a reproducible model bundle suitable for sharing with a partner (like Microsoft).

## Steps
1. `python scripts/train.py` – trains and saves model
2. `python scripts/export_bundle.py` – creates versioned export bundle with checksum and log
3. Output found in `partner_exports/v1.0.0/`

## Structure
- `/model` → Model weights, config, tokenizer, docs  
- `/partner_exports` → Packaged versioned zip bundle  
- `/scripts` → Training, evaluation, and export automation  

## Purpose
Demonstrate:
- IP transfer reproducibility
- Documentation standardization
- Automation and version control for research artifacts

