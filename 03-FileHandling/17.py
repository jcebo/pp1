import re
text='To be, or not to be, that is the question'
print(text)
samogloski=re.findall("[aeiou]",text)
print(f"Jest {len(samogloski)} samoglosek w tekscie")