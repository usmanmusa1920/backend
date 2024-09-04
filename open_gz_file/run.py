import gzip
from pathlib import Path


input_passwd = input("Enter password to check: ")

file_path = Path(__file__).resolve().parent / "common-pwds.txt.gz"

try:
    with gzip.open(file_path, "rt", encoding="utf-8") as f:
        gpasswords = {x.strip() for x in f}
except OSError:
    with open(file_path) as f:
        gpasswords = {x.strip() for x in f}


if input_passwd in gpasswords:
    print("\n  Valid password, found in the gz file.")
    print()
else:
    print("\n  Invalid password, not found in the gz file.")
    print()

