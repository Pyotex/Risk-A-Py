# Settings for one game party
player_count = 2
terrs_per_player = 2

territory_count = player_count * terrs_per_player
init_troops = territory_count // player_count

max_moves = 100000

# Chance for connecting two territories
connection_factor = 0.5

show_graph = False
show_matrix = False

# Simulation settings
max_repetition = 20
out_file = 'sim_out.txt'
