#          01234567890123456789012345
#letters = "abcdefghijklmnopqrstuvwxyz"
letters = ""

backwards = letters[::-1]
print(backwards)

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])

# Errors if letters 0 is empty, line 14 is preferred method
print(letters[0])