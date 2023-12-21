from sys import argv

filename = 'Config_SW1.txt'#argv[1]
with open(filename) as f:
    for line in f:
        if not line.startswith("!"):
            print(line.rstrip())
