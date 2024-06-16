import sys
sys.setrecursionlimit(10**7)

board = [0 for _ in range(9)]

win_con = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6]
]

def showBoard():
  print('-'*10)
  for i in range(3):
    print(' '.join(['O' if j == 1 else 'X' if j == -1 else '□' for j in board[i*3:i*3+3]]))
  print('-'*10)

def check(board):
  for con in win_con:
    a, b, c = con
    if board[a] == board[b] == board[c] and board[a] != 0:
      return board[a]
  return 0

def simulF(b, t):
  wc = 0
  dc = 0
  simul_board = b.copy()
  for j in range(len(simul_board)):
    if simul_board[j]:
      continue
    simul_board[j] = t
    isWin = check(simul_board)
    if isWin == -1:
      wc += 1
      continue
    elif isWin == 1:
      continue
    elif not isWin and simul_board.count(0) == 0:
      dc += 1
      break
    swc, sdc = simulF(simul_board, t*-1)
    wc += swc
    dc += sdc
  return wc, dc

def simul(b, t):
  win_cnt = [0 for _ in range(9)]
  draw_cnt = [0 for _ in range(9)]
  nowLose = 0
  for i in range(len(b)):
    simul_board = b.copy()
    if simul_board[i]:
      continue
    simul_board[i] = t
    isWin = check(simul_board)
    if isWin == -1:
      return i
    for j in range(len(b)):
      defence_simul_board = simul_board.copy()
      if defence_simul_board[j]:
        continue
      defence_simul_board[j] = t * -1
      isWin = check(defence_simul_board)
      if isWin == 1:
        nowLose = j
        continue
    wc, dc = simulF(simul_board, t * -1)
    win_cnt[i] = wc
    draw_cnt[i] = dc
  if nowLose:
    return nowLose
  if max(win_cnt) < max(draw_cnt):
    return draw_cnt.index(max(draw_cnt))
  else:
    return win_cnt.index(max(win_cnt))

while True:
  showBoard()
  isWin = check(board)
  if isWin:
    print(f"{'Player' if isWin == 1 else 'SIMUL'} Win!")
    break
  if board.count(0) == 0:
    print('Draw!')
    break
  position = int(input('\nPosition > '))
  if not board[position - 1]:
    board[position - 1] = 1
  else:
    continue
  isWin = check(board)
  if isWin:
    showBoard()
    print(f"{'Player' if isWin == 1 else 'SIMUL'} Win!")
    break
  if board.count(0) == 0:
    showBoard()
    print('Draw!')
    break
  print('\n고민 중..')
  board[simul(board, -1)] = -1