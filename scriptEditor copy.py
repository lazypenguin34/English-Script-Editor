with open("passage.txt") as f:
    lines = [i for i in f.read()]

for i in range(len(lines)):
    if lines[i] == '\n' and lines[i-1] == ':':
        lines[i] = ' '
open('edited-passage.txt', 'w').write(''.join(lines))