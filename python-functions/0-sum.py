def add(a, b):
    if b < 0:
        b = add(~b, 1)
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    if a & (1 << 31):
        a = add(~a, 1)
    return a
