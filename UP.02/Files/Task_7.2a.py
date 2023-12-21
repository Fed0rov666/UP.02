from sys import argv
ignore = ["hello", "world", "peace"]
filename = 'Config_SW1.txt'#argv[1]

with open(filename) as f:
    for line in f:
        words = line.split()
        words_intersect = set(words) & set (ignore)
        if not line.startswith("!") and not words_intersect:
            print(line.rstrip())