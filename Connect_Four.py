import numpy as np



"""
Connect Four
Take a look at wiki description of Connect Four game:

Wiki Connect Four

The grid is 6 row by 7 columns, those being named from A to G.

You will receive a list of strings showing the order of the pieces which dropped in columns:

  pieces_position_list = ["A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "G_Red",
                          "B_Yellow"]
The list may contain up to 42 moves and shows the order the players are playing.

The first player who connects four items of the same color is the winner.

You should return "Yellow", "Red" or "Draw" accordingly.
"""

list1 = ["A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "G_Red",
                          "B_Yellow"]

list2 = [
"C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red",
"G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red",
"D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red",
"C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red",
"E_Yellow", "E_Red"
]



def who_is_winner(pieces_position_list):

    row_index = 0
    column_index = 0
    moves_list =[]
    matrix = np.full((6,7),"_")

    #matrix[row_index][column_index] = "Y"
    #moves_list.append(str(row_index)+str(column_index))

    if moves_list.__contains__('56'):
        print("yes")
    A,B,C,D,E,F,G = 5,5,5,5,5,5,5
    new_list = []
    for i in pieces_position_list:
        new_list.append(i.split("_"))
    count_map = dict()
    for k,v in new_list:
        if k == 'A':
            matrix[A][0] = v
            A-=1
        if k == 'B':
            matrix[B][1] = v
            B-=1
        if k == 'C':
            matrix[C][2] = v
            C-=1
        if k == 'D':
            matrix[D][3] = v
            D-=1
        if k == 'E':
            matrix[E][4] = v
            E-=1
        if k == 'F':
            matrix[F][5] = v
            F-=1
        if k == 'G':
            matrix[G][6] = v
            G-=1
    print(matrix)

"""
def who_is_winner(pieces_position_list):
    x = []
    for i in pieces_position_list:
        x.append(i.split("_"))
    count_map = dict()
    for position in pieces_position_list:
        if position not in count_map:
            count_map[position] = 1
        else:
            count_map[position] = count_map[position] + 1
            if count_map[position] == 3:
                print(position.split("_")[1])
                print(count_map)
                return position.split("_")[1]


"""

print(who_is_winner(list2))