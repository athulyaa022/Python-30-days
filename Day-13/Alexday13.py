'''
Author:Alex
Date:27-1-2024
Description:Create a program to manage a list of favorite games.
'''
list_1=['Minecraft', 'FIFA', 'Call of Duty']
print("Current list of games: ",list_1)
game=input("Enter  game to add: ")
list_1.append(game)
print("Updated list of games: ",list_1)
remove_game=input("Enter a game to remove: ")
list_1.remove(remove_game)
print("Final list of games: ",list_1)