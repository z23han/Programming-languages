# Writing Closure

# We are currently looking at chart[i] and we see x => ab . cd from j

# Write the Python procedure, closure, that takes five parameters:

#   grammar: the grammar using the previously described structure
#   i: a number representing the chart state that we are currently looking at
#   x: a single nonterminal
#   ab and cd: lists of many things

# The closure function should return all the new parsing states that we want to
# add to chart position i

# Hint: This is tricky. If you are stuck, do a list comphrension over the grammar rules.

def closure (grammar, i, x, ab, cd):
    # Insert code here!
    if cd == []:
        return []

    states = [(x, [], r[1], i) for r in grammar if r[0] == cd[0]]

    return states


grammar = [ 
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ("t",["I","like","t"]),
    ("t",[""])
    ]

print closure(grammar,0,"exp",["exp","+"],["exp"]) == [('exp', [], ['exp', '+', 'exp'], 0), ('exp', [], ['exp', '-', 'exp'], 0), \
                                                       ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['num'], 0)]
print closure(grammar,0,"exp",[],["exp","+","exp"]) == [('exp', [], ['exp', '+', 'exp'], 0), ('exp', [], ['exp', '-', 'exp'], 0), \
                                                        ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['num'], 0)]

print closure(grammar,0,"exp",["exp"],["+","exp"]) == []
