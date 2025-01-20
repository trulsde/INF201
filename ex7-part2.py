def quadratic_function(x):
    return x**2

start = -3
stop = 2
step = 1

print("Kvadratisk funksjon:")
print(f"{'x':<3} | {'f(x)':<3}")
print("-" * 11)

x = start
while x <= stop:
    result = quadratic_function(x)
    print(f"{x:<3} | {result:<3}")
    x += step

print("\n")

def mordi():
    x = ((2 * 13 + 1) / 9) - 3
    y = (19 // 6)**0

    print(f"m{int(x)}r"f"d{y}")

mordi()
