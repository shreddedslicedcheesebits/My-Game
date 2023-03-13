from opening import *
from FloorMaps import *
#Items
#opening
opening()
#Selection Menu
c = 'select'
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
#starting room
floor_map(1)