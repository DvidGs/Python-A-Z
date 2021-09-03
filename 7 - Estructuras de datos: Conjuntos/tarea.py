# Ayuda a Pyratilla a hacer un conjunto de las islas de su mundo, llamado islands.
islands = {'Isla Alegre', 'Isla Golosa', 'Isla Espesura', 'Isla Arrecife', 'Isla Lejana', 'Isla Torva', 'Isla Verde'}
# Crea otro conjunto llamado visited_islands que tenga, de momento, un solo elemento: Isla Alegre.
visited_islands = {'Isla Alegre'}
# Crea un último conjunto, llamado unvisited_islands resultado de eliminar Isla Alegre al conjunto islands
unvisited_islands = islands.symmetric_difference(visited_islands)



