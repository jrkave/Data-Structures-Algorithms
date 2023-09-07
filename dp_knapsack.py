# Dynamic Programming Knapsack Problem

# Functions

def createMatrix(size, items):
    m = []
    for row in range(len(items) + 1): # add extra row for first row of 0's
        row = []
        for col in range(size + 1): # add extra column for base case (i.e. knapsack capacity of 0)
            row.append(0)
        m.append(row)
    return m

def knapsack(matrix, items):
    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])):
            # if current item's weight is less than the knapsack capacity, find max
            if items[i-1][1] <= j:
                matrix[i][j] = max((items[i-1][0] + matrix[i-1][(j - items[i-1][1])]),  matrix[i-1][j])
            # if current item's weight is greater than the knapsack capacity, copy value directly above into cell
            else:
                matrix[i][j] = matrix[i-1][j]
                
    return matrix[-1][-1] # return last item in matrix
         
def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

# Variables

size1 = 11 # knapsack capacity
items1 = [
    (1, 1), # (value, weight)
    (6, 2),
    (18, 5),
    (22, 6),
    (28, 7)
]

size2 = 10000 
items2 = [
    (16808, 250), (50074, 659), (8931, 273), (27545, 879), (77924, 710), (64441, 166),
    (84493, 43), (7988, 504), (82328, 730), (78841, 613), (44304, 170), (17710, 158),
    (29561, 934), (93100, 279), (51817, 336), (99098, 827), (13513, 268), (23811, 634),
    (80980, 150), (36580, 822), (11968, 673), (1394, 337), (25486, 746), (25229, 92),
    (40195, 358), (35002, 154), (16709, 945), (15669, 491), (88125, 197), (9531, 904),
    (27723, 667), (28550, 25)
]

# Solutions

matrix1 = createMatrix(size1, items1)
maxVal1 = knapsack(matrix1, items1)
print()
print("Output of Knapsack Table for Problem 1: ")
print()
printMatrix(matrix1)
print()
print(f"Maximum value for Problem 1: {maxVal1}")
print()

matrix2 = createMatrix(size2, items2)
maxVal2 = knapsack(matrix2, items2)
print(f"Maximum value for Problem 2: {maxVal2}")
print()


