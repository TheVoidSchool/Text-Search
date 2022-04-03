import re
file = open("lotr.txt",encoding='latin-1')
full_text = file.read()

full_text = re.sub(r'\W+ ', '', full_text)

##Your Code Here
script = full_text.split(" ")

count = 0



for word in script:
  if "elves" == word.lower() or "elf" == word.lower() or "bee" == word.lower():
    count+=1
    print(word)

print(f"count = {count}")
