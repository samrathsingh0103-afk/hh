import os

print("=== Science Notes ===")
with open("science-notes.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

print("=== Word Count ===")
with open("maths-notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words ->", line.strip())
print()

print("=== Merging Notes ===")
if os.path.exists("all-notes.txt")