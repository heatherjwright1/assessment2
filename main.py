## Question 2.1 

def isogram(word):
try:
if not word:
print('This is not an isogram')
return False
word = word.lower()
for i in word:
if word.count(i) > 1:
print('This is not an isogram')
return False
else:
print('This is an isogram!')
return True
except TypeError:
print('This is not a word')
return False



