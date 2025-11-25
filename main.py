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
