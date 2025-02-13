import cmath

def solve_quadratic(a, b, c):
    # calculating data
    delta = cmath.sqrt(b**2 - 4*a*c)
    
    # calculating the roots
    root1 = (-b + delta) / (2*a)
    root2 = (-b - delta) / (2*a)
    
    return root1, root2

# inputs
a = float(input("factor x^2 (a): "))
b = float(input("factor x (b): "))
c = float(input("factor (c): "))

# solution
root1, root2 = solve_quadratic(a, b, c)

print(f"root1: {root1}")
print(f"root2: {root2}")


