def floor_map(floor):
	Fmap = {1:"""
                |-----------------------------------|
        |-------|                                   |
        |       |                                   |
        |       |                                   |
|-------|       |                                   |-------|
| Chefs |Dinning|                                   |       |
|       \       \       Grand Staircase             \ Sword |
|Kitchen| Room  \                                   \Display|
|-------|       |                                   |       |
        |       |                                   |-------|
        |       |                                   |
        |       |                                   |
        |-------|                                   |
                |------|                    |-------|
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
                       |                    |
                   |---|--------\  \--------|---|
                   |                            |
                   |          Starting          |
                   |            Room            |
                   |                            |
                   |----------------------------|""",\
2:"""
                |-------------------|
                |      Balcony      |
                |                   |
        |-------|-------     -------|-------|
|-------|       |                   |       |
|       | Guest |                   | Guest |
|   ?   |       \  Grand Staircase  \       |
|       \Bedroom|                   |Bedroom|
|-------|       |                   |       |
        |-------|                   |-------|
                |---\ \-------\ \---|
                |     Bathroom      |
                |                   |
                |-------------------|""",\
3:"""
                              |-----------------------------------|
                              |            Balcony                |
                              |                                   |
|-------------------|         |-----------  \       \  -----------|------------------|
|                   |---------|                                   |                  |
|                   |         |                                   |      Master      |
|         ?         |   pit   \          Grand Staircase          \                  |
|                   |         \                                   \     Bedroom      |
|                   |         |                                   |                  |
|                   |---------|                                   |                  |
|-------------------|         |-------                     -------|------------------|
                              |                                   |
                              |                                   |
            |-----------------|                                   |-----------------|
            |                 |                                   |                 |
            |                 |                                   |                 |
            |                 |              Hallway              |                 |
            |                 |                                   |                 |
            |      Room       |                                   |                 |
            |                 |                                   |      Room       |
            |                 \                                   \                 |
            |                 \                                   \                 |
            |                 |                                   |                 |
            |                 |                                   |                 |
            |                 |                                   |                 |
            |                 |                                   |                 |
            |                 |-----------------------------------|                 |
            |                 |                                   |                 |
            |-----------------|                                   |-----------------|""",\
0:"""
|\----------|
|           |
|           |
| WineCellar|    |-------|
|           |    |       |
|           |----|       |
|           \Door\   ?   |
|-----------|----|       |
                 |       |
                 |-------|"""}
	print(Fmap[floor])
	return Fmap
