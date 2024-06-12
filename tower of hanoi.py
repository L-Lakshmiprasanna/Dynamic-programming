def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)

n = 3
tower_of_hanoi(n, 'A', 'C', 'B')

#------------with dynamic programing

def hanoi(n, source, destination, auxiliary, memo):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1
    if (n, source, destination) in memo:
        return memo[(n, source, destination)]
    moves1 = hanoi(n - 1, source, auxiliary, destination, memo)

    print(f"Move disk {n} from {source} to {destination}")
    moves2 = hanoi(n - 1, auxiliary, destination, source, memo)
    total_moves = moves1 + 1 + moves2
    memo[(n, source, destination)] = total_moves

    return total_moves

def tower_of_hanoi(n):
    memo = {}
    total_moves = hanoi(n, 'A', 'C', 'B', memo)
    print(f"Total moves required: {total_moves}")

tower_of_hanoi(3)