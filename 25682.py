import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[0]*M] + [[0] + list(input().strip()) for _ in range(N)]


W_check = ["0"*(M+1)] + ["0" + "WB"*(M//2) + "W"*(M%2), "0" + "BW"*(M//2) + "B"*(M%2)]*(N//2) + ["0" + "WB"*(M//2) + "W"*(M%2)]*(N%2)
B_check = ["0"*(M+1)] + ["0" + "BW"*(M//2) + "B"*(M%2), "0" + "WB"*(M//2) + "W"*(M%2)]*(N//2) + ["0" + "BW"*(M//2) + "B"*(M%2)]*(N%2)
    
sub_W = [[0]*(M+1) for _ in range(N+1)]
sub_B = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        sub_W[i][j] = int(board[i][j] != W_check[i][j]) + sub_W[i-1][j] + sub_W[i][j-1] - sub_W[i-1][j-1]
        sub_B[i][j] = int(board[i][j] != B_check[i][j]) + sub_B[i-1][j] + sub_B[i][j-1] - sub_B[i-1][j-1]

result = 10**10
for x_start in range(1, N-K+2):
    for y_start in range(1, M-K+2):
        x_point = x_start+K-1
        y_point = y_start+K-1
        
        cnt_color_W = sub_W[x_point][y_point] - sub_W[x_start-1][y_point] - sub_W[x_point][y_start-1] + sub_W[x_start-1][y_start-1]
        cnt_color_B = sub_B[x_point][y_point] - sub_B[x_start-1][y_point] - sub_B[x_point][y_start-1] + sub_B[x_start-1][y_start-1]
        
        result = min(result, cnt_color_W, cnt_color_B)

print(result)