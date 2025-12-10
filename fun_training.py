f = open(r"text.txt", "r", encoding="utf-8")
f2 = open(r"output.txt", "w", encoding="utf-8")
for line in f:
    f2.write(line)
f.close()
f2_content = open(r"output.txt", "r", encoding="utf-8").read()
print(f2_content)