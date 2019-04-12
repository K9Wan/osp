def fac(n):
    if not hasattr(n,'__sub__'):
        return None
    if n<2:
        return n
    return n*fac(n-1)


print(fac(int(input())))

