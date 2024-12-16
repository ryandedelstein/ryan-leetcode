def isNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def doOperation(operation, a, b):
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return int(a / b)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for i in tokens:
            if isNumber(i):
                numbers.append(int(i))
            else:
                b = numbers.pop()
                a = numbers.pop()
                result = doOperation(i,a,b)
                numbers.append(result)
        return numbers.pop()

