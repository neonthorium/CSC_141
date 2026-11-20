from pathlib import Path

path = Path(r"D:\CSC\CSC_141\10_Files_And_Exceptions\learning_python.txt")
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'C') #replace Python with C
    print(line)