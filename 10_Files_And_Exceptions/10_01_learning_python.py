from pathlib import Path

print("--- Learning Python---")
path = Path(r"D:\CSC\CSC_141\10_Files_And_Exceptions\learning_python.txt")
contents = path.read_text()
print(contents)

print("\n--- Learning Python - Reading line by line ---")
lines = contents.splitlines() #split the contents into lines
for line in lines:
    print(line) #print each line