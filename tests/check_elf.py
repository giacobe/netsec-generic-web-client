"""Report shared-library dependencies absent from a built guest filesystem."""
from pathlib import Path
import re
import subprocess
import sys

root = Path(sys.argv[1])
files = list(root.rglob("*"))
available = {file.name for file in files if file.is_file() or file.is_symlink()}
missing = {}
for file in files:
    if file.is_symlink() or not file.is_file():
        continue
    with file.open("rb") as source:
        if source.read(4) != b"\x7fELF":
            continue
    result = subprocess.run(["readelf", "-d", str(file)], capture_output=True, text=True)
    for dependency in re.findall(r"Shared library: \[(.*?)\]", result.stdout):
        if dependency not in available:
            missing.setdefault(dependency, []).append(str(file.relative_to(root)))
for dependency, users in sorted(missing.items()):
    print(dependency + ": " + ", ".join(users[:8]))
sys.exit(bool(missing))
