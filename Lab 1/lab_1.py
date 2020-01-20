textfile = "sample.txt"
raw  = open(textfile,"r")

lines = raw.readlines()
dbase = {}

for line in lines:
    line = line.rstrip()
    listOfWords = line.split(" ")
    print(listOfWords)
    
    for word in listOfWords:
        print(word)