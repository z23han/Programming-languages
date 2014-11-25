# Expanding Exp
# This is very, very difficult.

grammar = [ 
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ]


def expand(tokens, grammar):
    for pos in range(len(tokens)):
        for rule in grammar:
            if rule[0] == tokens[pos]:
                yield tokens[0:pos] + rule[1] + tokens[pos+1:]
            
            
depth = 2
utterances = [["a", "exp"]]
for x in range(depth):
    for sentence in utterances:
        utterances = utterances + [ i for i in expand(sentence, grammar)]

for sentence in utterances:
    print sentence
    
#    ['exp']
#    ['exp', '+', 'exp']
#    ['exp', '-', 'exp']
#    ['(', 'exp', ')']
#    ['num']
