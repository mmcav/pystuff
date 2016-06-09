def count_letters(string, chara):
    count = 0
    for char in string:
        if char == chara:
            count += 1
    return count

print(count_letters("banano", "a"))
