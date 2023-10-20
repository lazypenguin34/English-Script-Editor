with open("passage.txt") as f:
    lines = [i for i in f.read().split("\n")]

output = []
currentOutput = ""
character = ""
counter = 0

for i in lines:
    counter += 1
    if (i != "POZZO:" or i != "VLADIMIR:" or i != "ESTRAGON:"):
        output.append(i)
    else:
        character = i
        #to output, add character name, then the dialogue of the next line
        output.append(i + lines[counter])

lineCounter = 0
""" for i in output:
    print(output[lineCounter])
    lineCounter += 1 """

if (lines[0])