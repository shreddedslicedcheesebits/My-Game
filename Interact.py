from opening import interaction
def ap(item,inventory):
	if item not in inventory:
		inventory.append(item)
		print(f"\"{item}\" added to inventory")
		interaction()
	else:
		print(f"You have already pick up the \"{item}\" in this room")
		interaction()
		return inventory
def interact(current,inventory,door_open,end):
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
			interaction()
		else:
			print("You open the locked door in the Dinning Room and enter the basement.")
			current = 0,0,0
			interaction()
	elif current == (2,0,-1):
		if "Crowbar" not in inventory:
			print("There is a boarded locked door on the far left wall.\nyou cannot open it")
			interaction()
		else:
			print("You knock the boards off with the crowbar and enter the Dungeon")
			if "Glinting Sword" not in inventory:
				print("You look around you at notice little goblins all around you.\nYou defeat the first few, but quickly you perish.")
				inventory = []
				current = [1,0,0]
				interaction()
			else:
				if "Red Gem" not in inventory:
					print("You look around you at notice little goblins all around you.\nWith your Glinting Sword, you swiftly defeat the goblins and collect a Red Jem")
					inventory.append("Red Gem")
					interaction()
				else:
					print("You have already collected the Red Gem")
					interaction()
	elif current == (3,-1,1):
		if "Broken Bottle" not in inventory:
			print("You see a room with not much in it except for a broken bottle")
			interaction()
		else:
			print("You place your part of a broken bottle on the broken bottle on a dresser and it magically fits.\n In a nearby room, you hear a stone grinding.")
			door_open = True
			interaction()
	elif current == (3,0,-1):
		if "Ladder" not in inventory:
			print("You find a massive pit and jump down it killing you instantly")
			inventory = []
			current = (1,0,0)
			interaction()
		else:
			print("You lay the Ladder down flat over the pit.")
			interaction()
			if door_open != True:
				print("You walk across the ladder and meet a closed off wall.")
				interaction()
			else:
				print("You walk across the ladder and enter into a room with a massive shrine\n")
				interaction()
			if door_open == True:
				if "Sealed Book" in inventory:
					if "Blue Gem" not in inventory:
						print("You place the Sealed Book on the shrine and receive a Blue Gem")
						interaction()
						inventory.append("Blue Gem")
					else:
						print("You have already collected the Blue Gem.")
						interaction()
	elif current == (3,1,0):
		if "Torch" not in inventory:
			print("You look out over the balcony...")
			interaction()
		else:
			if "Yellow Gem" not in inventory:
				print("You place the torch on the balcony rail and the sky starts to illuminate\nSuddently lighting flashes and in place of the torch you find a yellow gem")
				interaction()
				inventory.append("Yellow Gem")
			else:
				print("You have already collected the Yellow Gem.")
				interaction()
	elif current == (0,0,1):
		if "Blue Gem" and "Yellow Gem" and "Red Gem" not in inventory:
			print("You find a sealed door with 3 holes in it")
			interaction()
		else:
			print("You place the 3 gems you found in the slots and the door opens")
			if "Golden Key" not in inventory:
				print("You enter a bright room with a golden door\nYou cannot open it")
				interaction()
			else:
				print("You enter a bright room with a golden door")
				interaction()
				print("You place the Golden Key in the door and it opens")
				interaction()
				print("You Walk through and escape")
				end = True
				interaction()
	elif current == (2,1,0):
		if "Guiding Coin" not in inventory:
			print("You look out over the balcony...")
			interaction()
		else:
			print("You see a hint appear in the sky")
			if "Broken Bottle" in inventory:
				print("\nPlace your piece of the broken bottle on the bottle on the dresser")
			if "Rusty Key" in inventory:
				print("\nThe Rusty key opens the door to the basement")
			if "Red Gem" not in inventory:
				print("The Red Gem can be found on the 2nd floor")
			if "Yellow Gem" not in inventory:
				print("The Yellow Gem can be found on the 3rd floor")
			if "Blue Gem" not in inventory:
				print("The Blue Gem can be found on the 3rd floor")
			interaction()
	else:
		print("Cannot interact here")
		interaction()
	return inventory, current, door_open, end
