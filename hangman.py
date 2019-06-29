def hangman(word):
    wrong = 0
    stages = ["",
              "_______       ",
              "|             ",
              "|      |      ",
              "|      O      ",
              "|     /|\     ",
              "|     / \     ",
              "|             ",
              ]
    rletters = list(word) #list関数でwordをリスト化しておく
    board = ["_"] * len(word) #答えのWordの文字数の長さをアンダーバーでヒントにしている
    win = False
    print("Welcom to hangman!")
    while wrong < len(stages) -1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters: #charがrletters内にあるかどうか
            cind = rletters.index(char) #charの文字がrlettersの何番目にあるか確認し、変数にindex番号を格納しておく
            board[cind] = char #リストborad「＿＿＿」の正解の文字を格納する。「cat」の「a」が入力されたのであれば「＿a＿」となる。
            rletters[cind] = '$' #同じ文字が複数回存在する文字列であれば、正確に動作しないため、$に置き換えておく。
        else:
            wrong += 1
        print(" ".join(board))#スコアボードの表示
        e = wrong + 1
        print("\n".join(stages[0:e]))#ハングマンの表示
        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}です。".format(word))

import random
word_list = ["cat", "egg" ,"fish", "tiger"]
r_n = random.randint(0, 5)
r_word = word_list[r_n]
hangman(r_word)
