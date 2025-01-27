#
# Sus respuestas para las preguntas falso y verdadero deben tener la siguiente forma.
# Sus respuestas deben verse como las dos siguientes:
#ANSWER1 = True
#ANSWER1 = False

# 1: Falso o Verdadero - busqueda Hill Climbing garantiza encontrar una respuesta
#	si es que la hay
ANSWER1 = None

# 2: Falso o Verdadero - busqueda Best-first encontrara una ruta optima
#	(camino mas corto).
ANSWER2 = None

# 3: Falso o Verdadero - Best-first y Hill climbing hacen uso de el
#	valor de la heuristica de los nodos.
ANSWER3 = None

# 4: Falso o Verdadero - A* utiliza un conjunto extendido de nodos
ANSWER4 = None

# 5: Falso o Verdadero - Anchura primero esta garantizado a encontrar un
#	camino con el minimo numero de nodos posible
ANSWER5 = None

# 6: Falso o Verdadero - El Branch and bound regular utiliza valores de
#	la heuristica para acelerar la busqueda de un camino optimo
ANSWER6 = None

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

# Implemente estos y los puede revisar con el modulo tester
## (Breadth-first search)
def bfs(graph, start, goal):
	agenda = [[start]]
	readed = [start]
	while agenda:
		next = agenda.pop()
		if next[0] == goal:
			return next[::-1]
		
		childs = graph.get_connected_nodes(next[0])
		for child in childs:
			if child not in readed:
				agenda.append([child] + next)
				readed.append(child)
	
	return []


## Si hizo el anterior el siguiente debe ser muy sencillo (Depth-first search)
def dfs(graph, start, goal):
	return dfs_rec(graph, start, goal, [])

def dfs_rec(graph, start, goal, readed):
	readed.append(start)
	if start == goal:
		return [start]
	
	agenda = graph.get_connected_nodes(start)
	for next in agenda:
		if next not in readed:
			path = dfs_rec(graph, next, goal, readed)
			if path:
				return [start] + path
	
	return []


## Ahora agregue heuristica a su busqueda
## Hill-climbing puede verse como un tipo de busqueda a profundidad primero
## La busqueda debe ser hacia los valores mas bajos que indica la heuristica
def hill_climbing(graph, start, goal):
	return hill_rec(graph, start, goal, [])

def hill_rec(graph, start, goal, readed):
	readed.append(start)
	if start == goal:
		return [start]
	
	agenda = graph.get_connected_nodes(start)
	agenda = sorted(agenda, key=lambda node: graph.get_heuristic(start, node), reverse=False)
	
	for next in agenda:
		if next not in readed:
			path = hill_rec(graph, next, goal, readed)
			if path:
				return [start] + path
	
	return []


## Ahora implementamos beam search, una variante de BFS
## que acota la cantidad de memoria utilizada para guardar los caminos
## Mantenemos solo k caminos candidatos de tamano n en nuestra agenda en todo momento.
## Los k candidatos deben ser determinados utilizando la
## funcion (valor) de heuristica del grafo, utilizando los valores mas bajos como los mejores
def val_path(graph, path):
	return graph.get_heuristic(path[0], path[-1])
	#val = 0
	#for i in range(0, len(path)-2):
	#	val += graph.get_heuristic(path[i], path[i+1])
	
	#return val

def beam_search(graph, start, goal, beam_width):
	agenda = [[start]]
	readed = [start]
	while agenda:
		next = agenda.pop()
		if next[0] == goal:
			return next[::-1]
		
		childs = graph.get_connected_nodes(next[0])
		for child in childs:
			if child not in readed:
				newrec = [child] + next
				val = val_path(graph, newrec)
				i = 0
				for record in agenda:
					if val < val_path(graph, record):
						agenda.insert(i, newrec)
						readed.append(child)
						break
					i += 1
				if len(agenda) > beam_width:
					del agenda[-1]
	
	return []


## Ahora se implemente busqueda optima, Las anteriores NO utilizan
## las distancias entre los nodos en sus calculos

## Esta funcion toma un grafo y una lista de nombres de nodos y retorna
## la suma de los largos de las aristas a lo largo del camino -- la distancia total del camino.
def path_length(graph, node_names):
	raise NotImplementedError


def branch_and_bound(graph, start, goal):
	raise NotImplementedError

def a_star(graph, start, goal):
	raise NotImplementedError


## Es util determinar si un grafo tiene una heuristica admisible y consistente
## puede dar ejemplos de grafos con heuristica admisible pero no consistente
## consistente pero no admisible?

def is_admissible(graph, goal):
	raise NotImplementedError

def is_consistent(graph, goal):
	raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = ''
WHAT_I_FOUND_INTERESTING = ''
WHAT_I_FOUND_BORING = ''
