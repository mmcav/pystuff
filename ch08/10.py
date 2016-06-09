def reverse(string):
    count = len(string)
    newstr = ""
    while count > 0:
        newstr += string[count-1]
        count -= 1
    return newstr

def is_palindrome(string):
    mirrorstr = reverse(string)
    if string == mirrorstr:
        return True
    else:
        return False

print(is_palindrome("abba"))
print(not is_palindrome("abab"))
print(is_palindrome("tenet"))
print(not is_palindrome("banana"))
print(is_palindrome("straw warts"))
print(is_palindrome("a"))
