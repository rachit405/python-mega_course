import json
from difflib import get_close_matches



data = json.load(open("data.json"))
print(type(data))

#print(data)

def translate(v):
	v = v.lower()
	if v in data:
		return data[v]
	elif len(get_close_matches(v, data.keys())) > 0:
		ya = input("did you mean %s ? Enter Y if yes and N if no" %get_close_matches(v, data.keys())[0])	
		if  ya == "Y" or ya == "y":
			return data[get_close_matches(v ,data.keys())[0]]
		elif ya == "N" or ya == "n":
			return "the word does not exist"
		else:
			return "Invalid entry"		 
	
	else: 
		return "check the word again"	

word = input("enter a word : ")

output = translate(word)

if type(output) == list:
	for item in output:
		print(item)

else:
	print(output)

