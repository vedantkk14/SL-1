# Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and
# Backtracking for n-queens problem or a graph coloring problem.

def is_safe_branch_and_bound(assignment, row, col):
    for r in range(row):
        c = assignment[r]
        if c == col or abs(c - col) == abs(r - row):
            return False  # Same column or diagonal
    return True

def branch_and_bound_n_queens(n):
    assignment = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(assignment.copy())
            return  
        for col in range(n):
            if is_safe_branch_and_bound(assignment, row, col):
                assignment[row] = col
                backtrack(row + 1)
                assignment[row] = -1  
    backtrack(0)
    return solutions


def is_safe_backtracking(row, col, assignment):
    for prev_row in range(row):
        prev_col = assignment[prev_row]
        if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
            return False
    return True

def solve_n_queens_backtracking(n):
    assignment = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(assignment.copy())
            return
        for col in range(n):
            if is_safe_backtracking(row, col, assignment):
                assignment[row] = col
                backtrack(row + 1)
                assignment[row] = -1

    backtrack(0)
    return solutions


def print_board(solution):
    n = len(solution)
    for row in solution:
        line = ['.'] * n
        line[row] = 'Q'
        print(' '.join(line))
    print()


def menu():
    print("\n===== N-Queens Solver =====")
    print("1. Solve using Branch and Bound")
    print("2. Solve using Backtracking")
    print("3. Exit")
    print("============================")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '3':
            print("Exiting program. Goodbye!")
            break

        try:
            n = int(input("\nEnter number of queens (N): "))
            if n <= 0:
                print("N must be a positive integer.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if choice == '1':
            print("\nSolving using Branch and Bound...\n")
            solutions = branch_and_bound_n_queens(n)
        elif choice == '2':
            print("\nSolving using Backtracking...\n")
            solutions = solve_n_queens_backtracking(n)
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
            continue

        print(f"Total solutions found: {len(solutions)}")
        if solutions:
            print("\nExample solution:")
            print_board(solutions[0])
        
# ===== N-Queens Solver =====
# 1. Solve using Branch and Bound
# 2. Solve using Backtracking
# 3. Exit
# ============================
# Enter your choice (1-3): 2

# Enter number of queens (N): 4

# Solving using Backtracking...

# Total solutions found: 2

# Example solution:
# . Q . .
# . . . Q
# Q . . .
# . . Q .

# ===== N-Queens Solver =====
# 1. Solve using Branch and Bound
# 2. Solve using Backtracking
# 3. Exit
# ============================
# Enter your choice (1-3): 1

# Enter number of queens (N): 4

# Solving using Branch and Bound...

# Total solutions found: 2

# Example solution:
# . Q . .
# . . . Q
# Q . . .
# . . Q .

# Backtracking: 
# O(N!) — in the worst case, it explores almost all permutations of N queens.
# 💾 Space Complexity:

# O(N²) if you use a full chessboard matrix.

# Or O(N) if you store only one array pos[col] = row (optimized version)

# Branch and Bound: 
# Much better, usually O(N²) in practice (though exponential in worst case), since pruning reduces search space drastically.

# Space Complexity O(N)

# 🎉 Simple Summary (Perfect for Viva/Exams)
# ⭐ Backtracking

# Try assigning values, check constraints, undo when violated.

# ⭐ Branch and Bound

# Improve backtracking by cutting off branches that cannot lead to a better or feasible solution.

# ⭐ N-Queens (Backtracking)

# Place queens row by row, check for attacks, backtrack on conflict.

# ⭐ N-Queens (Branch & Bound)

# If current partial placement already violates constraints, stop exploring that branch early.

# ⭐ Graph Coloring (Backtracking)

# Assign colors to nodes ensuring no adjacent conflict.

# ⭐ Graph Coloring (Branch & Bound)

# If current number of used colors exceeds best solution, prune.

# Backtracking:
# Try → Check → Undo → Try next option.

# Branch & Bound:
# Try → Check → Prune branches that are already worse than the best.