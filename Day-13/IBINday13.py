games=['Minecraft', 'Subway surfer', 'Dr driving']
print("Current list of games:",games)
new_game=input("Enter a game to add:")
games.append(new_game)
print("Updated list of games:",games)
game_remove=input("Enter a game to remove:")
games.remove(game_remove)
print("Final list of games:",games)