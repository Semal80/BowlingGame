from Game import Game


def play(players):
    player_first = players.split()[0]
    player_second = players.split()[1]
    play_bowl = Game(name1=player_first, name2=player_second)
    play_bowl.frames()
    play_bowl.score()
    if play_bowl.score1 > play_bowl.score2:
        print('Win {}'.format(player_first), 'with Score ', play_bowl.score1, 'againts', play_bowl.score2)
    elif play_bowl.score1 == play_bowl.score2:
        print('All Winners. Result equal {}'.format(play_bowl.score1))
    else:
        print('Win {}'.format(player_second), 'with Score ', play_bowl.score2, 'againts', play_bowl.score1)

if __name__ == '__main__':
    # players = input('Enter the names othe players separted by a space:')
    play('Neo Smith')





