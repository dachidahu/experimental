class Solution(object):
    ops = {
        'left': lambda i, j: (i, j - 1),
        'right': lambda i, j: (i, j + 1),
        'up': lambda i, j: (i - 1, j),
        'down': lambda i, j: (i + 1, j),
    }
    transitions = {
        'left': 'up',
        'up': 'right',
        'right': 'down',
        'down': 'left'
    }

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        if m == 1 and n == 1:
            return [matrix[0][0]]

        output = [matrix[0][0]]
        op = 'right'
        pos = (0, 1)

        num_to_go_m = m - 1
        num_to_go_n = n
        i_to_go_m = m - 1
        j_to_go_n = n - 1

        if n == 1:
            op = 'down'
            pos = (1, 0)

        while len(output) < (m * n):
            output.append(matrix[pos[0]][pos[1]])
            if op in ['right', 'left']:
                j_to_go_n -= 1
                if j_to_go_n == 0:
                    num_to_go_n -= 1
                    j_to_go_n = num_to_go_n
                    op = Solution.transitions[op]
            else:
                i_to_go_m -= 1
                if i_to_go_m == 0:
                    num_to_go_m -= 1
                    i_to_go_m = num_to_go_m
                    op = Solution.transitions[op]
            pos = Solution.ops[op](*pos)
        return output