import matplotlib.pyplot as plt

f = open('analytics.txt')

fil = open('players.txt')

players_data = []
for line in fil:
    players_data.append(line)

linecount = 0

for line in f:
    numbers_as_strings = line.split()
    numbers = [float(num) for num in numbers_as_strings]
    times = [float(num / 1000) for num in numbers]
    times_new = times[:12]

    scenes = ['S1','S2','S3','S4','S5','A1','A2','A3','A4','T1','T2','T3']

    bars = plt.bar(scenes,times_new)

    plt.xlabel('Game Scenes')

    plt.ylabel('Time Taken in Seconds')

    aggregate_time = times[12]

    player_name = players_data[linecount]

    plt.title('Player statistics of ' + player_name + str(aggregate_time) + ' seconds')

    
    for bar,value in zip(bars,times_new):
        plt.text(bar.get_x() + bar.get_width()/2,bar.get_height(),round(value,2),ha='center',va='bottom')

    plt.grid(linestyle='--',alpha=0.6)

    graph_name = 'Player_graph_' + str(linecount)

    plt.savefig(graph_name)

    linecount = linecount + 1




