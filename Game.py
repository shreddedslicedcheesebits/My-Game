from opening import *
from FloorMaps import *
from current_room import *
#Items
#opening
opening()
#Selection Menu
c = None
current = 2,0,0
while c != "q":
	c = input(f"""
{"|-------Menu-------|":^20}
{"View Inventory  1":^20}
{"View Current room  2":^20}
{"Show Floor maps  3":^20}
{"Interact  4":^20}
{"Walk forward  w":^20}
{"Walk Backward  s":^20}
{"Walk Left  a":^20}
{"Walk Right  d":^20}
{"Surrender  q":^20}
\nType Movement\n""")
	if c == "2":
		# Create an instance of the CurrentRoom class
		game_map = CurrentRoom()
		# Retrieve the name of the current room from the map
		current_room_name = game_map.get_room(current)
		# Display the current room name
		print(f"""{"You are currently in the:":^30}\n {current_room_name}""")
		print(f"""\n{"Type any key to close":^20}""")
		interaction()
	if c == "3":
		try:
			floor = int(input(f"""
{"--Select a floor--":^20}
{"Basement  0":^20}
{"First floor  1":^20}
{"Second Floor  2":^20}
{"Third Floor  3":^20}

{"Floor":<} """))
			floor_map(floor)
			print(f"""\n{"Type any key to close":^20}""")
			interaction()
		except:
			print("That wasn't a floor")
			interaction()
	if c == "w":
		floor,x,y = current
		if floor == 0:
			print("Cannot move forward or backward")
		elif floor == 1:
			if y != 0:
				print("Cannot move forward")
				interaction()
			else:
				if x not in range(0,2):
					print("Cannot move forward")
					interaction()
				else:
					x+=1
					print(floor,x,y)
					current = floor,x,y
		elif floor == 2:
			if y != 0:
				print("Cannot move forward")
			else:
				if x not in range(-1,1):
					print("Cannot move forward")
					interaction()
				else:
					x+=1
					print(floor,x,y)
					current = floor,x,y
		elif floor == 3:
			if y != 0:
				print("Cannot move forward")
			else:
				if x not in range(-1,1):
					print("Cannot move forward")
					interaction()
				else:
					x+=1
					print(floor,x,y)
					current = floor,x,y
	if c == "s":
		floor,x,y = current
		if floor == 0:
			print("Cannot move forward or backward")
		elif floor == 1:
			if y != 0:
				print("Cannot move backward")
				interaction()
			else:
				if x not in range(1,3):
					print("Cannot move backward")
					interaction()
				else:
					x-=1
					current = floor,x,y
		elif floor == 2:
			if y != 0:
				print("Cannot move forward")
			else:
				if x not in range(0,2):
					print("Cannot move backward")
					interaction()
				else:
					x-=1
					current = floor,x,y
		elif floor == 3:
			if y != 0:
				print("Cannot move forward")
			else:
				if x not in range(0,2):
					print("Cannot move backward")
					interaction()
				else:
					x-=1
					current = floor,x,y
	if c == "a":
		floor,x,y = current
		if floor == 0:
			if y != 1:
				print("Cannot move left")
				interaction()
			else:
				y-= 1
				current = floor,x,y
		elif floor == 1:
			if x != 2:
				print("Cannot move left")
				interaction()
			else:
				if y not in range(-1,2):
					print("Cannot move left")
					interaction()
				else:
					y-= 1
					current = floor,x,y
		elif floor == 2:
			if x != 0:
				print("Cannot move left")
				interaction()
			else:
				if y not in range(0,2):
					print("Cannot move left")
					interaction()
				else:
					y-= 1
					current = floor,x,y
		elif floor == 3:
			if x not in range(-1,1):
				print("Cannot move left")
				interaction()
			else:
				if y not in range(0,1):
					print("Cannot move left")
					interaction()
				else:
					y-= 1
					current = floor,x,y
	if c == "d":
		floor,x,y = current
		if floor == 0:
			if y != 0:
				print("Cannot move right")
				interaction()
			else:
				y+= 1
				current = floor,x,y
		elif floor == 1:
			if x != 2:
				print("Cannot move right")
				interaction()
			else:
				if y not in range(-2,1):
					print("Cannot move right")
					interaction()
				else:
					y+= 1
					current = floor,x,y
		elif floor == 2:
			if x != 0:
				print("Cannot move right")
				interaction()
			else:
				if y not in range(-1,1):
					print("Cannot move right")
					interaction()
				else:
					y+= 1
					current = floor,x,y
		elif floor == 3:
			if x not in range(-1,1):
				print("Cannot move right")
				interaction()
			else:
				if y not in range(0,1):
					print("Cannot move right")
					interaction()
				else:
					y-= 1
					current = floor,x,y




#starting room
