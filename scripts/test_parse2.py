with open('/home/mohamed/Desktop/PMOSKILL/forms.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# find PROJECT CHARTER blank form
idx = text.find('PROJECT CHARTER')
idx2 = text.find('1.2 Assumption Log')
print(text[idx:idx2])

