ITEMS = (('(', ')'), ('{', '}'), ('[',']') )
OPENING = set([ item[0] for item in ITEMS ])
CLOSING = set([ item[1] for item in ITEMS ])
BRACKET_MAP = dict(ITEMS)

def is_matched(expression):
    char_stack = []
    for char in expression:
        if char in OPENING:
            char_stack.append(char)
        elif char in CLOSING:
            if len(char_stack) <= 0 or char != BRACKET_MAP.get(char_stack.pop(), False):
                return False
        else:
            next
    if len(char_stack) == 0:
        return True
    else:
        return False


t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
