# the first and last elements of every row are always 1
# every other element is the sum of the two elements directly above in the previous row

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(1, rowIndex + 1):
            next_row = [1]

            # sum adjacent pairs from previous row
            for j in range(1, len(row)):
                next_row.append(row[j-1] + row[j])

            next_row.append(1)
            row = next_row

        return row