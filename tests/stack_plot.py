from matplotlib import pyplot   as plt

plt.style.use('ggplot')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 =[1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 =[1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 =[1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = ['player1', 'player2', 'player3']

#plt.pie([1, 1, 1], labels=["Player 1", "Player 2", "Player 3" ])
plt.stackplot(minutes, player1, player2, player3, labels=labels)

plt.legend(loc='upper left')

plt.title("Stack Plot Test")
plt.tight_layout()
plt.show()
