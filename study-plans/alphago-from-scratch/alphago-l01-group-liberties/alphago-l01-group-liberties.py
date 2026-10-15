import numpy as np

def go_group_liberties(board: list, row: int, col: int) -> tuple:
    arr = np.array(board)
    target_color = arr[row, col]
    rows, cols = arr.shape
    
    group = set()
    liberties = set()
    stack = [(row, col)]
    
    while stack:
        r, c = stack.pop()
        if (r, c) in group:
            continue
        group.add((r, c))
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbor = arr[nr, nc]
                if neighbor == target_color:
                    if (nr, nc) not in group:
                        stack.append((nr, nc))
                elif neighbor == 0:
                    liberties.add((nr, nc))
                    
    return sorted(list(group)), sorted(list(liberties))