# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
def xo(s):
    return sum(c in 'x' for c in s.lower()) == sum(c in 'o' for c in s.lower())


user_string = 'xxxxxxxxxOxoo oooooooo'
print(xo(user_string))
