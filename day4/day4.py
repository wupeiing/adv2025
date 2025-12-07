from argparse import ArgumentParser

def question_1(input_file):
    with open(input_file, "r") as f:
        grid = [list(line.strip()) for line in f if line.strip()]

    rows = len(grid)
    cols = len(grid[0])

    # 8 possible directions (including diagonals)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbors = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbors += 1

            if neighbors < 4:
                accessible += 1

    print(accessible)

def question_2(input_file, visualize=False):
    with open(input_file, "r") as f:
        grid = [list(line.rstrip("\n")) for line in f if line.rstrip("\n")]

    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    # 8 neighbor directions
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    # Build initial neighbor counts only for '@' cells (others kept 0)
    neigh = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                cnt = 0
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        cnt += 1
                neigh[r][c] = cnt

    total_removed = 0
    round_no = 0

    while True:
        # collect all removable positions this round
        to_remove = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@' and neigh[r][c] < 4:
                    to_remove.append((r,c))

        if not to_remove:
            break  # no more removals possible

        round_no += 1
        if visualize:
            print(f"Round {round_no}, removing {len(to_remove)} rolls:")

        # remove them simultaneously and update neighbor counts
        for r,c in to_remove:
            grid[r][c] = '.'    # removed
            total_removed += 1
            # decrement neighbor counts for neighboring '@' cells
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                    neigh[nr][nc] -= 1
            neigh[r][c] = 0

        if visualize:
            for row in grid:
                print("".join(row))
            print()

    print(total_removed)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--qid", type=str, required=True,
                        help="Question ID")
    parser.add_argument("--dry", type=str, required=False, default=False,
                        help="using sample input or not")
    args = parser.parse_args()
    if args.dry == "True":
        input_file = "./day4/input_sample.txt"
    else:
        input_file = "./day4/input.txt"
    if args.qid == "1":
        question_1(input_file)
    elif args.qid == "2":
        question_2(input_file)