from Game import Game


def play(players):
    player_first = players.split()[0]
    player_second = players.split()[1]
    play_bowl = Game(name1=player_first, name2=player_second)
    play_bowl.turn()
    play_bowl.print_table()
    print(play_bowl.score_list_1, play_bowl.score_list_2)


if __name__ == '__main__':
    # players = input('Enter the names othe players separted by a space:')
    play('Neo Smith')





