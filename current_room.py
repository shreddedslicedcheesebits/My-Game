class CurrentRoom:
    def __init__(self):
        self.room = {
            1: {
                0: {
                    0:"""
    |---|--------\  \--------|---|
    |                            |
    |          Starting          |
    |            Room            |
    |                            |
    |----------------------------|"""
                },
                1: {
                    0:"""
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
    |                    |"""
                },
                2: {
                    0:"""
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
                    1:"""
    |-------|
    |       |
    \ Sword |
    \Display|
    |       |
    |-------|""",
                    -1:"""
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
                    -2:"""
    |-------|
    | Chefs |
    |       \ 
    |Kitchen|
    |-------|"""
                }
            },
            2: {}
        }

    def get_room(self, current):
        floor, x, y = current
        print(floor, x, y)
        return self.room[floor][x][y]
