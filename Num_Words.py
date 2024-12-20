# Num_Words.py

def num_words(filename):
    total = 0
    f = open(filename)
    for line in f:
        line = line.strip()
        words = line.split()
        total = total + len(words)
    return total
    f.close()

print(num_words("ModestProposal.txt"))
