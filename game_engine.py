import random
import copy

# --- COLONEL BLOTTO ---


def generate_blotto_setup(): return [
    random.randint(10, 50) for _ in range(3)], 100


def evaluate_blotto(p1, p2, pts):
    s1, s2 = 0, 0
    for i in range(3):
        if p1[i] > p2[i]:
            s1 += pts[i]
        elif p2[i] > p1[i]:
            s2 += pts[i]
    return s1, s2


def get_random_blotto():
    a = random.randint(0, 100)
    b = random.randint(0, 100 - a)
    return [a, b, 100 - a - b]

# --- CONNECT 4 & MINIMAX ORACLE ---


def create_board(): return [[0 for _ in range(7)] for _ in range(6)]
def get_valid_cols(b): return [c for c in range(7) if b[0][c] == 0]


def print_board(b):
    sym = {0: ".", 1: "X", 2: "O"}
    return "Col: 0 1 2 3 4 5 6\n" + "\n".join(["     " + " ".join([sym[c] for c in r]) for r in b])


def drop_piece(b, col, p):
    for r in range(5, -1, -1):
        if b[r][col] == 0:
            b[r][col] = p
            return True
    return False


def check_win(b, p):
    for r in range(6):
        for c in range(4):
            if all(b[r][c+i] == p for i in range(4)):
                return True
    for r in range(3):
        for c in range(7):
            if all(b[r+i][c] == p for i in range(4)):
                return True
    for r in range(3):
        for c in range(4):
            if all(b[r+i][c+i] == p for i in range(4)):
                return True
            if all(b[r+3-i][c+i] == p for i in range(4)):
                return True
    return False


def minimax_solver(board, depth, alpha, beta, maximizing):
    valid = get_valid_cols(board)
    if check_win(board, 1):
        return (None, -100000)
    if check_win(board, 2):
        return (None, 100000)
    if depth == 0 or not valid:
        return (None, 0)

    best_col = random.choice(valid)
    if maximizing:
        val = -float('inf')
        for col in valid:
            temp = copy.deepcopy(board)
            drop_piece(temp, col, 2)
            score = minimax_solver(temp, depth-1, alpha, beta, False)[1]
            if score > val:
                val, best_col = score, col
            alpha = max(alpha, val)
            if alpha >= beta:
                break
        return best_col, val
    else:
        val = float('inf')
        for col in valid:
            temp = copy.deepcopy(board)
            drop_piece(temp, col, 1)
            score = minimax_solver(temp, depth-1, alpha, beta, True)[1]
            if score < val:
                val, best_col = score, col
            beta = min(beta, val)
            if alpha >= beta:
                break
        return best_col, val
