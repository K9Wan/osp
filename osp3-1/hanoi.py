def move_tower(n, src, dest, temp):
    if n == 1:
        print("Move disk from", src, "to", dest, ".")
        return 1
    step1 = move_tower(n-1, src, temp, dest)
    step2 = move_tower(1, src, dest, temp)
    step3 = move_tower(n-1, temp, dest, src)
    return sum((step1, step2, step3))

def hanoi(n):
    return move_tower(n, "A", "C", "B")

def hanoi_str(n):
    return "Total movement: "+str(hanoi(n))
