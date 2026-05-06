# # total rectangle        → prefix[row2][col2]
# minus top part         → prefix[row1-1][col2]
# minus left part        → prefix[row2][col1-1]
# plus corner (added back) → prefix[row1-1][col1-1]

# bottomRight - above - left + topLeft

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # building the prefix table
        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix = [ [0] * cols for _ in range(rows)] # this creates 2D array populated with 0s

        # fill the prefix table
        for row in range(rows):
            #prefix = 0

            for col in range(cols):

                self.prefix[row][col] = (
                matrix[row][col]
                + (self.prefix[row-1][col] if row > 0 else 0)
                + (self.prefix[row][col-1] if col > 0 else 0)
                - (self.prefix[row-1][col-1] if row > 0 and col > 0 else 0)
                
                )



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        D = self.prefix[row2][col2]
        B = self.prefix[row1-1][col2] if row1 > 0 else 0
        C = self.prefix[row2][col1-1] if col1 > 0 else 0
        A = self.prefix[row1-1][col1-1] if row1>0 and col1 > 0 else 0

        return D - B - C + A

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)