def floor_map(floor):
	Fmap = {1:"""
                |-----------------------------------|
        |-------|                                   |
        |       |                                   |
        |       |                                   |
|-------|       |                                   |-------|
| Chefs |Dinning|                                   |       |
|       |       |       Grand Staircase             | Sword |
|Kitchen| Room  |                                   |Display|
|-------|       |                                   |       |
        |       |                                   |-------|
        |       |                                   |
        |       |                                   |
        |-------|                                   |
                |-----------------------------------|"""}

	print(Fmap[floor])