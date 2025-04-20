def is_valid_input(n, row):
    return (
        len(row) == n and
        set(row) == set(range(1, n + 1))
    )

def can_place(matrix, row_idx, candidate_row, n):
    for i in range(n):
        for prev in range(row_idx):
            if matrix[prev][i] == candidate_row[i]:
                return False
    return True

def is_strictly_increasing_col(matrix, col_idx, n):
    for i in range(1, n):
        if matrix[i][col_idx] <= matrix[i - 1][col_idx]:
            return False
    return True

def backtrack(matrix, n, row_idx, used_rows, one_col_idx):
    if row_idx == n:
        if is_strictly_increasing_col(matrix, one_col_idx, n):
            return True
        return False

    for perm in permutations(range(1, n + 1)):
        if perm in used_rows:
            continue
        if not can_place(matrix, row_idx, perm, n):
            continue
        matrix[row_idx] = list(perm)
        used_rows.add(perm)
        if backtrack(matrix, n, row_idx + 1, used_rows, one_col_idx):
            return True
        used_rows.remove(perm)
        matrix[row_idx] = [0] * n

    return False

from itertools import permutations

def main():
    try:
        n = int(input())
        if not (4 <= n <= 9):
            print("Invalid input")
            return

        first_row = list(map(int, input().split()))
        if not is_valid_input(n, first_row):
            print("Invalid input")
            return
    except:
        print("Invalid input")
        return

    matrix = [[0] * n for _ in range(n)]
    matrix[0] = first_row
    used_rows = {tuple(first_row)}
    try:
        one_col_idx = first_row.index(1)
    except ValueError:
        print("Invalid input")
        return

    if backtrack(matrix, n, 1, used_rows, one_col_idx):
        for row in matrix:
            print(' '.join(map(str, row)))
    else:
        print("No solution")

if __name__ == "__main__":
    main()