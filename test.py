# -*- coding: utf-8 -*-
__author__ = 'Chason'

from TnnPlayer import TnnPlayer
from GameBoard import GameBoard
tp = TnnPlayer()
tp.hard_code_tnn()
# tp.tnn.inputNodes[7].value = 1
# tp.tnn.inputNodes[9].value = 1
# tp.tnn.forwardPropagation()
total_games = 100
ai_wins = 0
ai_lose = 0
draws = 0

gb = GameBoard()
for i in range(total_games):
    print "Game%d **************************"%i
    while gb.turns < gb.ROW * gb.COL:
        gb.safe_rnd_move(2)
        gb.show_board()
        res = gb.judge(gb.last_move)
        if res == 2:
            print "AI lose..."
            ai_lose += 1
            break
        elif res == gb.DRAW:
            print "There is a draw..."
            draws += 1
            break

        tp.tnn.get_input(gb.board)
        tp.tnn.forward_propagation()
        # tp.tnn.show_structure(False, False, False)
        if not gb.move(tp.tnn.max_output(), 1):
            print "AI random move..."
            gb.safe_rnd_move(1)
        gb.show_board()

        res = gb.judge(gb.last_move)
        if res == 1:
            print "AI wins..."
            ai_wins += 1
            break
        elif res == gb.DRAW:
            print "There is a draw..."
            draws += 1
            break
    gb.resume_board()

print "total games:", total_games
print "AI wins:", ai_wins
print "AI lose:", ai_lose
print "Draws:", draws