def anagrams(s):
    #if s == "":
    if len(s) == 1:
        return (s,)
    ans = []
    for w in anagrams(s[1:]):
        #print(s,w)
        for pos in range(len(w)+1):
            ans.append(w[:pos]+s[0]+w[pos:])
    #print(ans)
    return ans

