def count_letters(string, chara):
    count = 0
    initial = 0
    while True:
        result = string.find(chara, initial)
        if result == -1:
            break
        count += 1
        initial = result + 1
    return count

print(count_letters("bananaaal", "a"))
