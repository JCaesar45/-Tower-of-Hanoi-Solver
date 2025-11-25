```
🗼 Tower of Hanoi Solver

A Python implementation of the classic Tower of Hanoi puzzle.
This project prints the complete sequence of moves required to solve the puzzle for any number of disks, following the mathematical rules of the game.

📌 Features

Function: hanoi_solver(n)

Solves the Tower of Hanoi puzzle in 2ⁿ − 1 moves

Prints:

The starting arrangement

Every move made

Each state on its own line

Rods displayed as Python lists

Fully matches the formatting and logic required by common unit tests

🧠 Problem Description

The Tower of Hanoi puzzle consists of 3 rods and n disks of different sizes.

Rules:

Only the top disk of any rod may be moved.

Only one disk can be moved at a time.

No disk may be placed on top of a smaller disk.

Your goal: Move all disks from the first rod to the last rod.

🧩 Example Output (n = 3)
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]

🛠️ Code Implementation

Below is the full working solution:

def hanoi_solver(n):
    rods = [
        list(range(n, 0, -1)),  # Source rod (A)
        [],                     # Auxiliary rod (B)
        []                      # Target rod (C)
    ]
    
    output = []

    # Helper to record state
    def record():
        output.append(f"{rods[0]} {rods[1]} {rods[2]}")

    # Move disk from rod i to rod j
    def move(i, j):
        disk = rods[i].pop()
        rods[j].append(disk)
        record()

    # Classical recursive Hanoi
    def solve(k, start, aux, end):
        if k == 0:
            return
        solve(k - 1, start, end, aux)  # Move top k-1 to auxiliary
        move(start, end)               # Move largest disk
        solve(k - 1, aux, start, end)  # Move k-1 on top of largest

    # Record starting arrangement
    record()

    # Solve
    solve(n, 0, 1, 2)

    return "\n".join(output)

▶️ How to Use

Save the function in a Python file, for example:

hanoi.py


Import and run:

from hanoi import hanoi_solver

print(hanoi_solver(3))


Output will show all rod states from start to finish.

🧪 Testing

The function passes common unit test expectations:

Returns a string

Prints the starting rod configuration

Prints all 2ⁿ − 1 moves

Maintains exact formatting required for automated grading systems

Works for any positive integer n

📚 Concepts Covered

Recursion

Algorithmic thinking

Data structure manipulation

Mathematical problem solving

Functional decomposition

📄 License

This project is free to use for educational or portfolio purposes.
