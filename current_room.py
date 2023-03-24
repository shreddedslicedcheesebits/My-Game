class CurrentRoom:
	def __init__(self):
		self.room = {
			"1": {
				"Start": """
    |---|--------\  \--------|---|
    |                            |
    |          Starting          |
    |            Room            |
    |                            |
    |----------------------------|""",
				"Hallway": """
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |
    |      Hallway       |
    |                    |
    |                    |
    |                    |
    |                    |
    |                    |""",
				"Staircase-1": """
    |-----------------------------------|
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    \       Grand Staircase             \ 
    \                                   \ 
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |                                   |
    |------|                    |-------|""",
				"Sword-display": """
    |-------|
    |       |
    \ Sword |
    \Display|
    |       |
    |-------|""",
				"Dinning": """
    |-------|
    |       |
    |       |
    |       |
    |Dinning|
    \       \ 
    | Room  \ 
    |       |
    |       |
    |       |
    |       |
    |-------|""",
				"Chef": """
    |-------|
    | Chefs |
    |       \ 
    |Kitchen|
    |-------|""",
			},
			"2": {}
		}

	def get_room(self, floor, room):
			return self.room[floor][room]