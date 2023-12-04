def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for i in matrix:
            for j in i:
                if j == i[-1]:
                    print("{:d}".format(j), end="\n")
                else:
                    print("{:d}".format(j), end=" ")