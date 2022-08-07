from os import lseek


def valid_parentheses(string):
    lst = [ string[i] for i in range(len(string)) if (string[i] == '(') | (string[i] == ')')]
    print(lst)
    score = 0
    for i in lst:
        if i == '(':
            score += 1
        elif i == ')':
            score -= 1
        if score < 0:
            return False
    print(score)
    if score == 0:
        return True
    else:
        return False