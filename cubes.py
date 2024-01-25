cubes = []
for x in range(10):
    if x%2==0:
        cubes.append(x**3)
print("Using for loop : ", cubes)


# list comprehension
easy = [x**3 for x in range (10) if x%2==0]
print("Using list comprehension : ",easy)