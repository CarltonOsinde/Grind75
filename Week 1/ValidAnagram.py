def isAnagram(self,s,t):
    if len(s) != len(t):
        return False
    l = "abcdefghijklmnopqrstuvwxyz"
    for c in l:
        if s.count(c) != t.count(c):
            return False
    return True