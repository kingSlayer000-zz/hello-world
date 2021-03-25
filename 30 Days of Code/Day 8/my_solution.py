n = int(input())

phoneBook = {}
l = []

for a in range(n):
    l.append(str(input()))

phoneBook = dict(x.split() for x in l)

while 1:
    try:
        textInput = str(input())
        
        if textInput in phoneBook.keys():
            textOutput = "{}={}"
            print(textOutput.format(textInput, phoneBook.get(textInput)))
        else:
            print("Not found")
    except:
        break
