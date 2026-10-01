import numpy as np

def go_group_liberties(board: list, row: int, col: int) -> tuple:
    """
    Returns a tuple of two sorted coordinate lists: [group, liberties].
    """
    board_arr = np.array(board)
    num_rows, num_cols = board_arr.shape
    
    target_color = board_arr[row, col]
    
    group = set()
    liberties = set()
    stack = [(row, col)]
    
    # 4 orthogonal directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        r, c = stack.pop()
        if (r, c) in group:
            continue
            
        group.add((r, c))
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check board boundaries
            if 0 <= nr < num_rows and 0 <= nc < num_cols:
                neighbor_val = board_arr[nr, nc]
                
                if neighbor_val == target_color:
                    if (nr, nc) not in group:
                        stack.append((nr, nc))
                elif neighbor_val == 0:
                    liberties.add((nr, nc))
                    
    # Format to sorted lists of [row, col]
    sorted_group = [list(coord) for coord in sorted(group)]
    sorted_liberties = [list(coord) for coord in sorted(liberties)]
    
    return (sorted_group, sorted_liberties)