# Writing Shift

# We are currently looking at chart[i] and we see x => ab . cd from j.
# The input is tokens.

# Your procedure, shift, should either return None,
# at which point there is
# nothing to do or will return a single new parsing state
# that presumably
# involved shifting over the c if c matches the ith token.

def shift (tokens, i, x, ab, cd, j):
    # Insert code here
    if cd != [] and tokens[i] == cd[0]:
        return (x, ab+[cd[0]], cd[1:], j)
    return None

    '''
    comb = ab + cd
    if comb != tokens:
        return None
    if x not in comb:
        return None
    comb_length = len(comb)
    if i >= comb_length:
        return None
    
    next_ab = comb[:i+1]
    next_cd = comb[i+1:]
    return (x, next_ab, next_cd, j)
'''

print shift(["exp","+","exp"],2,"exp",["exp","+"],["exp"],0) \
      == ('exp', ['exp', '+', 'exp'], [], 0)

print shift(["exp","+","exp"],0,"exp",[],["exp","+","exp"],0) \
      == ('exp', ['exp'], ['+', 'exp'], 0)

print shift(["exp","+","exp"],3,"exp",["exp","+","exp"],[],0) == None

print shift(["exp","+","ANDY LOVES COOKIES"],2,"exp",["exp","+"],["exp"],0) \
      == None

