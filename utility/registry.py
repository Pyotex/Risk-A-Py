#Settings for one game party
player_count = 2
terrs_per_player = 4

territory_count = player_count * terrs_per_player
init_troops = territory_count // player_count

max_moves = 10

#Chance for connecting two territories
connection_factor = 0.5

show_graph = True
show_matrix = False

#Simulation settings
max_repetition = 1
out_file = 'sim_out.txt'