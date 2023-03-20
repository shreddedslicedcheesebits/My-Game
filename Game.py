from opening import *
from FloorMaps import *
#Items
#opening
opening()
#Selection Menu
c = None
while c != "q":
	c = input(f"""
{"|-------Menu-------|":^20}
{"View Inventory  1":^20}
{"Show Floor maps  2":^20}
{"Interact  3":^20}
{"Walk forward  w":^20}
{"Walk Backward  s":^20}
{"Walk Left  a":^20}
{"Walk Right  d":^20}
{"Surrender  q":^20}
\nType Movement\n""")
	if c == "2":
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
