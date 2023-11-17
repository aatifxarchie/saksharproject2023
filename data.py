import matplotlib.pyplot as plt

with open('analytics.txt','r') as file:
    content = file.read()
    numbers_as_strings = content.split()
    numbers = [float(num) for num in numbers_as_strings]
    times = [float(num / 1000) for num in numbers]
    times_new = times[:9]


scenes = ['S1','S2','S3','S4','S5','A1','A2','A3','A4']

bars = plt.bar(scenes,times_new)

plt.xlabel('Game Scenes')
plt.ylabel('Time taken in seconds')
player_name = 'Ronit Kumar'
aggregate_time = times[9]
plt.title('Player statistics of '+ player_name + ' '+ str(aggregate_time) + ' seconds')

for bar,value in zip(bars,times_new):
    plt.text(bar.get_x() + bar.get_width()/2,bar.get_height(),round(value,2),ha='center',va='bottom')

plt.grid(linestyle='--',alpha=0.6)

plt.savefig('player_graph.png')

plt.show()