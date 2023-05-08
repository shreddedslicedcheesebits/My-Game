from opening import interaction
def ap(item,inventory):
	if item not in inventory:
		inventory.append(item)
		print(f"\"{item}\" added to inventory")
		interaction()
	else:
		print(f"You have already pick up the \"{item}\" in this room")
		return inventory
def interact(current,inventory,door_open):
	if current == (0, 0, 0):
		ap("Broken Bottle",inventory)
	elif current == (1,0,0):
		ap("Guiding Coin",inventory)
	elif current == (1,1,0):
		ap("Torch",inventory)
	elif current == (1,2,1):
		ap("Glinting Sword",inventory)
	elif current == (1,2,-2):
		ap("Ladder",inventory)
	elif current == (2,0,1):
		ap("Rusty Key",inventory)
	elif current == (2,-1,0):
		ap("Sealed Book",inventory)
	elif current == (3,0,1):
		ap("Golden Key",inventory)
	elif current == (3,-1,-1):
		ap("Crowbar",inventory)
	elif current == (1,2,-1):
		if "Rusty Key" not in inventory:
			print("There is a locked door in the corner of the Dinning Room.\nYou cannot open it")
		else:
			print("You open the locked door in the Dinning Room and enter the basement.")
			current = 0,0,0
	elif current == (2,0,-1):
		if "Crowbar" not in inventory:
			print("There is a boarded locked door on the far left wall.\nyou cannot open it")
		else:
			print("You knock the boards off with the crowbar and enter the Dungeon")
			if "Glinting Sword" not in inventory:
				print("You look around you at notice little goblins all around you.\nYou defeat the first few, but quickly you perish.")
				inventory = []
				current = 1,0,0
			else:
				print("You look around you at notice little goblins all around you.\nWith your Glinting Sword, you swiftly defeat the goblins and collect a Red Jem")
				inventory.append("Red Gem")
	elif current == (3,-1,1):
		if "Broken Bottle" not in inventory:
			print("You see a room with not much in it except for a broken bottle")
		else:
			print("You place your part of a broken bottle on the broken bottle on a dresser and it magically fits.\n In a nearby room, you hear a stone grinding.")
			door_open = True
	elif current == (3,0,-1):
		if "Ladder" not in inventory:
			print("You find a massive pit and jump down it killing you instantly")
			inventory = []
			current = 1,0,0
		else:
			print("You lay the Ladder down flat over the pit.")
			if door_open != True:
				print("You walk across the ladder and meet a closed off wall.")
			else:
				print("You walk across the ladder and enter into a room with a massive shrine\n")
			if door_open == True:
				if "Sealed Book" in inventory:
					print("You place the Sealed Book on the shrine and receive a Blue Gem")
					inventory.append("Blue Gem")

	else:
		print("Cannot interact here")
	return inventory, current, door_open
