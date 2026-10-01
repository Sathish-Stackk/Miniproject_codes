from pathlib import Path
from collections import defaultdict

files = [
    "resume.pdf", "photo.jpg", "notes.txt",
    "project.py", "logo.png", "app.py"
]

groups = defaultdict(list)

for filename in files:
    extension = Path(filename).suffix or "No Extension"
    groups[extension].append(filename)

for extension, names in sorted(groups.items()):
    print(f"\n{extension}:")
    for name in names:
        print(" -", name)
