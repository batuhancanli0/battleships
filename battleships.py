# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print(
        "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print(
        "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print(
        "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print(
        "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write(
            "If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write(
            "If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
# f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = False  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    counter = 0
    gemiuzunluklari = {'carrier': 5, 'battleship': 4, 'cruiser': 3, 'submarine': 3, 'destroyer': 2}
    gemiler = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
    board_size = 10
    oyuncu1 = [['-' for i in range(board_size)] for x in range(board_size)]
    oyuncu2 = [['-' for i in range(board_size)] for x in range(board_size)]
    oyuncu1_bos = [['-' for i in range(board_size)] for x in range(board_size)]
    oyuncu2_bos = [['-' for i in range(board_size)] for x in range(board_size)]
    my_list = [oyuncu1_bos, oyuncu2_bos]
    koyulmusgemiler_1 = []
    koyulmusgemiler_2 = []
    gemiler2 = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
    gemili_noktalar1=[]

    input_list = []
    while counter < 5:

        oyuncu2 = [['-' for i in range(board_size)] for x in range(board_size)]
        oyuncu1_bos = [['-' for i in range(board_size)] for x in range(board_size)]
        oyuncu2_bos = [['-' for i in range(board_size)] for x in range(board_size)]
        my_list = [oyuncu1, oyuncu2_bos]
        print_3d_list(my_list)

        print_ships_to_be_placed()

        for gemi in gemiler:
            print_single_element(gemi)
        print_empty_line()
        n = 1
        print_player_turn_to_place(n)
        print_to_place_ships()
        inputlist = input().split()
        koyulacak_gemi = inputlist[0].lower().strip()

        if koyulacak_gemi in koyulmusgemiler_1:
            print_ship_is_already_placed(koyulacak_gemi)
        else:
            if len(inputlist) == 4:
                gemi_x = inputlist[2].lower().strip()
                gemi_y = inputlist[1].lower().strip()
                try:
                    int(gemi_x)
                except ValueError:
                    print_incorrect_input_format()
                    continue
                try:
                    int(gemi_y)
                except ValueError:
                    print_incorrect_input_format()
                    continue

                if int(inputlist[1]) < 11:
                    if int(inputlist[2]) < 11:
                        if koyulacak_gemi in gemiler:

                            h_mi_v_mi = inputlist[3].lower().strip()
                            gemi_x = inputlist[2].lower().strip()
                            gemi_y = inputlist[1].lower().strip()
                            try:
                                if h_mi_v_mi == 'v':
                                    for gemiuzunluk in range(gemiuzunluklari[inputlist[0].lower().strip()]):
                                        if oyuncu1[int(gemi_x) + gemiuzunluk - 1][int(gemi_y) - 1] == '#':
                                            print_ship_cannot_be_placed_occupied(koyulacak_gemi)

                                            for sil in range(gemiuzunluk+1):
                                                oyuncu1[int(gemi_x) - sil+1 ][int(gemi_y)-1 ] = 'p'

                                            break

                                        else:
                                            oyuncu1[int(gemi_x) + gemiuzunluk - 1][int(gemi_y) - 1] = '#'


                                elif h_mi_v_mi == 'h':
                                    for gemiuzunluk in range(gemiuzunluklari[inputlist[0].lower().strip()]):
                                        oyuncu1[int(gemi_x) - 1][int(gemi_y) + gemiuzunluk - 1] = '#'

                                else:
                                    print_incorrect_orientation()
                                    continue
                                gemiler.remove(koyulacak_gemi.lower())
                                counter = counter + 1
                                koyulmusgemiler_1.append(koyulacak_gemi.lower())


                                if len(koyulmusgemiler_1) == 5:
                                    print_3d_list(my_list)
                                    print_confirm_placement()
                                    yesorno = input().strip().lower()
                                    if yesorno == 'y':
                                        continue
                                    else:
                                        counter = 0
                                        oyuncu1 = [['-' for i in range(board_size)] for x in range(board_size)]
                                        gemiler = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
                                        koyulmusgemiler_1 = []

                            except:
                                try:
                                    if h_mi_v_mi == 'v':
                                        for gemiuzunluk in range(gemiuzunluklari[inputlist[0].lower().strip()]):
                                            oyuncu1[int(gemi_x) + gemiuzunluk - 1][int(gemi_y) - 1] = '-'
                                    elif h_mi_v_mi == 'h':
                                        for gemiuzunluk in range(gemiuzunluklari[inputlist[0].lower().strip()]):
                                            oyuncu1[int(gemi_x) - 1][int(gemi_y) + gemiuzunluk - 1] = '-'
                                except:
                                    print_ship_cannot_be_placed_outside(koyulacak_gemi)












                        else:
                            print_incorrect_ship_name()

                    else:
                        print_incorrect_coordinates()
                else:
                    print_incorrect_coordinates()
            else:
                print_incorrect_input_format()

        print()
    counter2 = 0

    while counter2 < 5:

        oyuncu1_bos = [['-' for i in range(board_size)] for x in range(board_size)]
        oyuncu2_bos = [['-' for i in range(board_size)] for x in range(board_size)]
        my_list = [oyuncu1_bos, oyuncu2]
        print_3d_list(my_list)

        print_ships_to_be_placed()

        for gemi2 in gemiler2:
            print_single_element(gemi2)
        print_empty_line()
        n = 2
        print_player_turn_to_place(n)
        print_to_place_ships()
        inputlist = input().split()
        koyulacak_gemi = inputlist[0].lower().strip()

        if koyulacak_gemi in koyulmusgemiler_2:
            print_ship_is_already_placed(koyulacak_gemi)
        else:
            if len(inputlist) == 4:
                gemi_x = inputlist[2].lower().strip()
                gemi_y = inputlist[1].lower().strip()
                try:
                    int(gemi_x)
                except ValueError:
                    print_incorrect_input_format()
                    continue
                try:
                    int(gemi_y)
                except ValueError:
                    print_incorrect_input_format()
                    continue

                if int(inputlist[1]) < 11:
                    if int(inputlist[2]) < 11:
                        if koyulacak_gemi in gemiler2:

                            koyulacak_gemi = inputlist[0].lower().strip()
                            h_mi_v_mi = inputlist[3].lower().strip()
                            gemi_x = inputlist[2].lower().strip()
                            gemi_y = inputlist[1].lower().strip()

                            try:
                                if h_mi_v_mi == 'v':
                                    for gemiuzunluk in range(gemiuzunluklari[inputlist[0]]):
                                        oyuncu2[int(gemi_x) + gemiuzunluk - 1][int(gemi_y) - 1] = '#'
                                elif h_mi_v_mi == 'h':
                                    for gemiuzunluk in range(gemiuzunluklari[inputlist[0]]):
                                        oyuncu2[int(gemi_x) - 1][int(gemi_y) + gemiuzunluk - 1] = '#'
                                else:
                                    print_incorrect_orientation()
                                    continue

                                gemiler2.remove(koyulacak_gemi)
                                counter2 = counter2 + 1
                                koyulmusgemiler_2.append(koyulacak_gemi)
                                if len(koyulmusgemiler_2) == 5:
                                    print_3d_list(my_list)
                                    print_confirm_placement()
                                    yesorno = input().strip().lower()
                                    if yesorno == 'y':
                                        continue
                                    else:
                                        counter = 0
                                        oyuncu2 = [['-' for i in range(board_size)] for x in range(board_size)]
                                        gemiler2 = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
                                        koyulmusgemiler_2 = []


                            except:
                                try:
                                    if h_mi_v_mi == 'v':
                                        for gemiuzunluk in range(gemiuzunluklari[inputlist[0]]):
                                            oyuncu2[int(gemi_x) + gemiuzunluk - 1][int(gemi_y) - 1] = '-'
                                    elif h_mi_v_mi == 'h':
                                        for gemiuzunluk in range(gemiuzunluklari[inputlist[0]]):
                                            oyuncu2[int(gemi_x) - 1][int(gemi_y) + gemiuzunluk - 1] = '-'
                                except:
                                    print_ship_cannot_be_placed_outside(koyulacak_gemi)
                                    continue








                        else:
                            print_incorrect_ship_name()

                    else:
                        print_incorrect_coordinates()
                else:
                    print_incorrect_coordinates()
            else:
                print_incorrect_input_format()

        print()


    tekmiciftmi = 0
    finishsayaci=0
    finishsayaci2=0
    vurulmus1=[]
    vurulmus2=[]
    oyuncu1_vurdugu=[['-' for i in range(board_size)] for x in range(board_size)]
    oyuncu2_vurdugu=[['-' for i in range(board_size)] for x in range(board_size)]

    while True:

        if tekmiciftmi % 2 == 0:
            my_list = [oyuncu1, oyuncu1_vurdugu]
            print_3d_list(my_list)
            n = 1
            print_player_turn_to_strike(n)
            print_choose_target_coordinates()

            vurulacak_hedef = input().split()
            if vurulacak_hedef in vurulmus1:
                print_tile_already_struck()
            else:
                vurulmus1.append(vurulacak_hedef)
                if len(vurulacak_hedef) == 2:
                    vurulacak_x = int(vurulacak_hedef[0])
                    vurulacak_y = int(vurulacak_hedef[1])
                    try:
                        int(vurulacak_x)
                    except:
                        print_incorrect_input_format()
                        continue
                    try:
                        int(vurulacak_y)
                    except:
                        print_incorrect_input_format()
                        continue
                    if oyuncu2[vurulacak_y - 1][vurulacak_x - 1] == '#':
                        print_hit()
                        oyuncu2[vurulacak_y - 1][vurulacak_x - 1] = '!'
                        oyuncu1_vurdugu[vurulacak_y-1][vurulacak_x-1]='!'

                        finishsayaci = finishsayaci + 1
                        if finishsayaci == 17:
                            print_player_won(n)
                            print_thanks_for_playing()
                            break
                    elif oyuncu2[vurulacak_y - 1][vurulacak_x - 1] == '-':
                        print_miss()
                        oyuncu2[vurulacak_y - 1][vurulacak_x - 1] = 'O'
                        oyuncu1_vurdugu[vurulacak_y-1][vurulacak_x-1]='O'

                        while True:
                            n=2
                            print_type_done_to_yield(n)
                            donemi = input().lower().strip()
                            if donemi=='done':
                                tekmiciftmi=tekmiciftmi+1
                                break
                            else:
                                continue
                else:
                    print_incorrect_input_format()



        elif tekmiciftmi % 2 == 1:
            my_list = [oyuncu2_vurdugu, oyuncu2]
            print_3d_list(my_list)
            n = 2
            print_player_turn_to_strike(n)
            print_choose_target_coordinates()
            vurulacak_hedef = input().split()
            if vurulacak_hedef in vurulmus2:
                print_tile_already_struck()
            else:
                vurulmus2.append(vurulacak_hedef)
                if len(vurulacak_hedef) == 2:
                    vurulacak_x = int(vurulacak_hedef[0])
                    vurulacak_y = int(vurulacak_hedef[1])
                    try:
                        int(vurulacak_x)
                    except:
                        print_incorrect_input_format()
                        continue
                    try:
                        int(vurulacak_y)
                    except:
                        print_incorrect_input_format()
                        continue
                    if oyuncu1[vurulacak_y - 1][vurulacak_x - 1] == '#':
                        print('hit')
                        oyuncu1[vurulacak_y - 1][vurulacak_x - 1] = '!'
                        oyuncu2_vurdugu[vurulacak_y-1][vurulacak_x-1]='!'

                        finishsayaci2 = finishsayaci2 + 1
                        if finishsayaci2 == 17:
                            print_player_won(n)
                            print_thanks_for_playing()
                            break
                    elif oyuncu1[vurulacak_y - 1][vurulacak_x - 1] == '-':
                        print('miss')
                        oyuncu1[vurulacak_y - 1][vurulacak_x - 1] = 'O'
                        oyuncu2_vurdugu[vurulacak_y-1][vurulacak_x-1]='O'
                        while True:
                            n=1
                            print_type_done_to_yield(n)
                            donemi = input().lower().strip()
                            if donemi=='done':
                                tekmiciftmi=tekmiciftmi+1
                                break
                            else:
                                continue
                else:
                    print_incorrect_input_format()
        else:
            continue

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()