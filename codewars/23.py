def valid_parentheses(s):
    return s.count('(') == s.count(')') and s.rfind('(') <= s.rfind(')') and s.find('(') <= s.find(')')


print(valid_parentheses("hi())("))
print(valid_parentheses('())(()'))
