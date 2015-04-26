# 'abc'
# abc, acb, bac, bca, cab, cba

def permute(s):
    if len(s)==1: return [s]
    result = []
    for i in range(len(s)):
        partial = permute(s[:i]+s[i+1:])
        for str in partial: result += [s[i]+str]
    return result

s = '1234'
print(permute(s))
