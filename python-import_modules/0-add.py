a = 1
b = 2

def add(a, b):
    return a + b

result = add(a, b)
if isinstance(b, int):
    print(f"a = {a} and b = {b} FAKE add() => {a} - {b}")
else:
    print(f"a = {a} and b = '{b}' FAKE add() => {a} - b")
if __name__ == "__main__":
    print(f"{a} + {b} = {result}")
