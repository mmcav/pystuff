import string

def phrasing(strng):
    part1 = ""
    for char in strng:
        if char not in string.punctuation:
            part1 += char
    part2 = part1.split()
    total = len(part2)
    count = 0
    for char in part2:
        if "e" in char:
            count += 1
    print("""Your text contain {0} words, of which {1} ({2:.1f}%) contain an "e".""".format(total, count, count*100.0/total))

phrase = """'Cause you're a sky, 'cause you're a sky full of stars
I'm going to give you my heart
'Cause you're a sky, 'cause you're a sky full of stars
'Cause you light up the path
Word Three"""

phrasing(phrase)
