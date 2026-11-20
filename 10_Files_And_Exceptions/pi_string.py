from pathlib import Path

path = Path(r"D:\CSC\CSC_141\10_Files_And_Exceptions\pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip() #remove whitespace from the left side of the string and add to pi_string

print(pi_string[:52] + "...") #print first 52 characters of pi_string
print(len(pi_string)) #print length of pi_string