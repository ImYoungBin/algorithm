'''
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
'''

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