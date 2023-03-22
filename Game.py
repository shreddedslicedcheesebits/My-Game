from opening import *
from FloorMaps import *
from current_room import *
#Items
#opening
opening()
#Selection Menu
c = None
floor=1
room="Start"
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
		a = CurrentRoom()
		print(a.get_room(floor,room))
	if c == "3":
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

#starting room
