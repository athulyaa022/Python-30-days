games = ['Minecraft', 'FIFA', 'Call of Duty']
print("Current list of games:", games)
new_game = input("Enter a game to add: ")
games.append(new_game)
print("Updated list of games:", games)
remove_game = input("Enter a game to remove: ")
if remove_game in games:
    games.remove(remove_game)
print("Final list of games:", games)
