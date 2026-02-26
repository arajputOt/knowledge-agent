from pathlib import Path
from collections import defaultdict

DOCS_ROOT = Path("data_pdfs")

# registry
registry = []

for pdf_path in DOCS_ROOT.rglob("*.pdf"):
    relative = pdf_path.relative_to(DOCS_ROOT)
    parts = relative.parts

    top_level = parts[0] if len(parts) >= 1 else "UNKNOWN"
    module = parts[1] if len(parts) >= 2 else "ROOT"

    registry.append({
        "path": str(pdf_path),
        "top_level": top_level,
        "module": module,
        "document": pdf_path.name
    })

tree = defaultdict(lambda: defaultdict(list))

for item in registry:
    tree[item["top_level"]][item["module"]].append(item["document"])

total = 0
for top_level, modules in sorted(tree.items()):
    print(f"\n📁 {top_level}")
    for module, docs in sorted(modules.items()):
        print(f"  └── 📂 {module}")
        for doc in sorted(docs):
            print(f"      ├── 📄 {doc}")
            total += 1

print(f"\n✅ Total PDFs found: {total}")