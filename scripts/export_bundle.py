import os, hashlib, json, datetime, zipfile, pathlib, re, subprocess

def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def next_version():
    """Read last version folder and bump patch number"""
    exports = pathlib.Path("partner_exports")
    exports.mkdir(exist_ok=True)
    versions = [d.name for d in exports.iterdir() if d.is_dir() and re.match(r"v\d+\.\d+\.\d+", d.name)]
    if not versions:
        return "v1.0.0"
    latest = sorted(versions)[-1]
    major, minor, patch = map(int, latest[1:].split("."))
    return f"v{major}.{minor}.{patch+1}"

def export_bundle():
    version = next_version()
    out_dir = pathlib.Path("partner_exports") / version
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / "model_bundle.zip"

    # 1️⃣ bundle the model
    with zipfile.ZipFile(zip_path, "w") as zf:
        for root, _, files in os.walk("model"):
            for f in files:
                full = os.path.join(root, f)
                zf.write(full, arcname=os.path.relpath(full, "model"))

    # 2️⃣ checksum
    checksum = hash_file(zip_path)

    # 3️⃣ optional partner validation (runs eval.py)
    try:
        result = subprocess.run(
            ["python", "scripts/eval.py"],
            capture_output=True,
            text=True,
            timeout=120,
        )
        validation_output = result.stdout.strip()
    except Exception as e:
        validation_output = f"Validation failed: {e}"

    # 4️⃣ write log and checksum
    meta = {
        "version": version,
        "export_time": datetime.datetime.utcnow().isoformat(),
        "checksum": checksum,
        "validation_output": validation_output,
    }
    (out_dir / "transfer_log.json").write_text(json.dumps(meta, indent=2))
    (out_dir / "checksum.txt").write_text(checksum)

    # 5️⃣ append to central log file
    log_path = pathlib.Path("partner_exports/exports_history.jsonl")
    with open(log_path, "a") as f:
        f.write(json.dumps(meta) + "\n")

    print(f"✅ Exported {version}  |  Accuracy check → {validation_output}")

if __name__ == "__main__":
    export_bundle()