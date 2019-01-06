A = [[1,2,3],
          [4,5,6],
          [7,8,9]]
B =    [[1,2,3],
          [4,5,6],
          [7,8,9]]
result = [[sum(a * b for a, b in zip(A_row, B_col))
           for B_col in zip(*B)]
          for A_row in A]
for r in result:
    print(r)
