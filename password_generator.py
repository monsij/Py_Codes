#monsijb
# Use an import statement at the top

from random import randint as rint
word_file = "words.txt"
word_list = []
cnt=0
#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)
			cnt += 1
#print(word_list)
# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    res = ""
    for i in range(3):
        x = rint(0,cnt-1)
        res +=word_list[x]
    return res

print(generate_password())
    
