# TIME: O(n)
# SPACE: O(n)
def valid_parens(item):
    stack = []
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for i in item:
        if i in pairs:
            stack.append(i)
        else:
            if not stack:
                return False
            temp = stack.pop()
            if pairs[temp] != i:
                return False

    if stack:
        return False
    return True

print(valid_parens('(()[])'))
