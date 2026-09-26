import re

with open('/home/mohamed/Desktop/PMOSKILL/forms.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find the text for PROJECT CHARTER
# It starts after Table 1.1 Elements of a Project Charter (continued)
# And ends before Table 1.2 Elements of an Assumption Log
import sys

start_idx = text.find('Table 1.1')
start_idx = text.find('Table 1.1', start_idx + 10) # Find the (continued) part
if start_idx == -1: start_idx = text.find('Table 1.1')

end_idx = text.find('Table 1.2')

print(text[start_idx:end_idx][:2000])
