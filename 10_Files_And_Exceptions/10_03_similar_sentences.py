from pathlib import Path

path = Path(r"D:\CSC\CSC_141\10_Files_And_Exceptions\pi_digits.txt")
contents = path.read_text()

for line in contents.splitlines():
    print(line)