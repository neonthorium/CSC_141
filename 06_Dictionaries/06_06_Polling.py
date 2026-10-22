favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print("\n")

coders = ['becca', 'dan', 'sarah', 'kat', 'edward', 'phil', 'erin']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the poll, {coder.title()}.")
    else:
        print(f"{coder.title()}, what is your favorite programming language?")