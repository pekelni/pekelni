a = '()()()((()((((()()()())))))(()))'


def check(text):
    while text:
        before = len(text)
        text = text.replace('()', '')
        if len(text) == before:
            return False
    return True


print(check(a))
print(check('()'))
print(check('()()'))
print(check('()())'))
print(check('()())('))
