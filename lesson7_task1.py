class Matrix:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        for i in self.array:
            for j in i:
                print(f"{j:6}", end="")
            print('')
        return ''

    def __add__(self, array_sum):
        for i in range(len(self.array)):
            for j in range(len(array_sum.array[i])):
                self.array[i][j] = self.array[i][j] + array_sum.array[i][j]
        return Matrix.__str__(self)


arr_1 = Matrix([[3, 5, 7], [13, 15, 17], [22, 33, 44]])
arr_2 = Matrix([[2, 6, 9], [-5, -15, -7], [55, 66, 88]])
print(arr_1.__add__(arr_2))
