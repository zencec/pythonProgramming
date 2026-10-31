step = 5
# Print the upper part of the pyramid
for i in range(1, step + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
# Printthelowerpartofthepyramid
for i in range(step - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
