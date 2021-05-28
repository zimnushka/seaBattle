import os
clear = lambda: os.system('cls')
def main():
	global healthTWO
	global healthONE
	healthONE=int(3)
	healthTWO=int(3)
	playerONEfield={}
	playerONEfield= {'A': [0,0,0], 'B': [0,0,0], 'C': [0,0,0]}
	playerONEbattle={}
	playerONEbattle= {'A': [0,0,0], 'B': [0,0,0], 'C': [0,0,0]}
	playerTWOfield={}
	playerTWOfield= {'A': [0,0,0], 'B': [0,0,0], 'C': [0,0,0]}
	playerTWObattle={}
	playerTWObattle= {'A': [0,0,0], 'B': [0,0,0], 'C': [0,0,0]}
	def print_field(playerfield):
		print("  1 |2| 3")
		print("A|" + str(playerfield['A']))
		print("B|" + str(playerfield['B']))
		print("C|" + str(playerfield['C']))
	def set_ship(playerfield):
		i=int(0)
		while i<3 :
			inpt=str(input("Введи позицию коробля(например:A1)"))
			symbol=list(inpt)
			playerfield[str(symbol[0])][int(symbol[1])-1]=1	
			print_field(playerfield)
			i+=1
	def destroy_ship(playerfield,playerbattle,player):
		inpt=str(input("Введи позицию выстрела (например:A1)"))
		symbol=list(inpt)
		playerbattle[str(symbol[0])][int(symbol[1])-1]=1
		if playerfield[str(symbol[0])][int(symbol[1])-1]==playerbattle[str(symbol[0])][int(symbol[1])-1]:
			print("BOOOOM!!!!!")
			player-=1
			print(player)
			playerbattle[str(symbol[0])][int(symbol[1])-1]=2
			return player
		else:
			print("miss")
	def print_game():
		print("  1 |2| 3          1 |2| 3")
		print("A|" + str(playerONEbattle['A']) + "      " + str(playerTWObattle['A']))
		print("B|" + str(playerONEbattle['B']) + "      " + str(playerTWObattle['B']))
		print("C|" + str(playerONEbattle['C']) + "      " + str(playerTWObattle['C']))
	def game():
		global healthTWO
		global healthONE
		i=int(0)
		while i < 9:
			print("первый игрок")
			healthTWO = destroy_ship(playerTWOfield,playerTWObattle,healthTWO)
			print_game()
			if healthTWO ==0:
				i=10
				clear()
				print("1 player WON")
			print("второй игрок")
			healthONE = destroy_ship(playerONEfield,playerONEbattle,healthONE)
			print_game()
			if healthONE ==0:
				i=10
				clear()
				print("2 player WON")
	print("1 игрок раставь корабли")
	print_field(playerONEfield)		
	set_ship(playerONEfield)
	clear()
	print("2 игрок раставь корабли")
	input("нажми на любую клавишу для продолжения")
	print_field(playerTWOfield)		
	set_ship(playerTWOfield)
	clear()
	print_game()
	game()
main()