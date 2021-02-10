def bi_a(st,en,ta,l):
    if en-st<2:
        if l[en]<ta:
            return en
        if ta<=l[st]:
            return -1
        return st
    h=(st+en)//2
    if l[h]<ta:
        return bi_a(h,en,ta,l)
    return bi_a(st,h,ta,l)
 
def bi_b(st,en,ta,l):
    if en-st<2:
        if l[en]<=ta:
            return en
        if ta<l[st]:
            return -1
        return st
    h=(st+en)//2
    if l[h]<=ta:
        return bi_b(h,en,ta,l)
    return bi_b(st,h,ta,l)
