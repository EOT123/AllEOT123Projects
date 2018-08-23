import random

game_board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
empty_game_board_list = []
for i in range(0, len(game_board_list)):
    empty_game_board_list.append("*")


def print_board():
    print("{}  {}  {}  {}".format(game_board_list[0], game_board_list[1], game_board_list[2], game_board_list[3]))
    print("{}  {}  {}  {}".format(game_board_list[4], game_board_list[5], game_board_list[6], game_board_list[7]))
    print("{}  {}  {}  {}".format(game_board_list[8], game_board_list[9], game_board_list[10], game_board_list[11]))
    print("{}  {}  {}  {}".format(game_board_list[12], game_board_list[13], game_board_list[14], game_board_list[15]))
    print("{}  {}  {}  {}".format(empty_game_board_list[0], empty_game_board_list[1], empty_game_board_list[2],
                                  empty_game_board_list[3]))
    print("{}  {}  {}  {}".format(empty_game_board_list[4], empty_game_board_list[5], empty_game_board_list[6],
                                  empty_game_board_list[7]))
    print("{}  {}  {}  {}".format(empty_game_board_list[8], empty_game_board_list[9], empty_game_board_list[10],
                                  empty_game_board_list[11]))
    print("{}  {}  {}  {}".format(empty_game_board_list[12], empty_game_board_list[13], empty_game_board_list[14],
                                  empty_game_board_list[15]))


print(game_board_list)
temp_list_for_tiles = []
for i in range(1, 4):
    new_tile = random.randrange(2, 3)
    temp_list_for_tiles.append(new_tile)
    new_tile_placement = random.randrange(0, 8)
    print("tile num = " + str(new_tile) + "    place of tile = " + str(new_tile_placement))
print(temp_list_for_tiles)
for i in range(0, 3):
    print(empty_game_board_list)
    remove_index_from_egb = random.randrange(0, 8)
    empty_game_board_list.remove(empty_game_board_list[remove_index_from_egb])
    empty_game_board_list.insert(remove_index_from_egb, temp_list_for_tiles[i])
print_board()
new_list = []
for i in range(0, 16):
    if i % 4 == 0:
        new_list.append(game_board_list[i])

print(new_list)
