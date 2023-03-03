# TPO - PROGRAMACION III - UADE PINAMAR 2023 #
# Eduardo Stipa - L.U. 1018538
# Mariano Fortunato - L.U. 1135771
from grafo_operaciones import *

def grafo_ejemplo_bfs():
	grafo = Grafo(False)
	# Agregar vertices 
	grafo.agregar_vertice("r")
	grafo.agregar_vertice("s")
	grafo.agregar_vertice("t")
	grafo.agregar_vertice("u")
	grafo.agregar_vertice("v")
	grafo.agregar_vertice("w")
	grafo.agregar_vertice("x")
	grafo.agregar_vertice("y")
	# Agregar aristas
	grafo.agregar_arista("r", "s", 0)
	grafo.agregar_arista("r", "v", 0)
	grafo.agregar_arista("s", "w", 0)
	grafo.agregar_arista("w", "t", 0)
	grafo.agregar_arista("w", "x", 0)
	grafo.agregar_arista("t", "u", 0)
	grafo.agregar_arista("t", "x", 0)
	grafo.agregar_arista("x", "u", 0)
	grafo.agregar_arista("x", "y", 0)

	return grafo

def grafo_ejemplo_dfs():
	grafo = Grafo(True)
	# Agregar vertices 
	grafo.agregar_vertice("u")
	grafo.agregar_vertice("v")
	grafo.agregar_vertice("w")
	grafo.agregar_vertice("x")
	grafo.agregar_vertice("y")
	grafo.agregar_vertice("z")
	# Agregar aristas
	grafo.agregar_arista("u", "v", 0)
	grafo.agregar_arista("u", "x", 0)
	grafo.agregar_arista("v", "y", 0)
	grafo.agregar_arista("w", "y", 0)
	grafo.agregar_arista("w", "z", 0)
	grafo.agregar_arista("x", "v", 0)
	grafo.agregar_arista("y", "x", 0)
	grafo.agregar_arista("z", "z", 0)

	return grafo

def grafo_ejemplo_floyd_no_dirigido():
	grafo = Grafo(False)
	# Agregar vertices 
	grafo.agregar_vertice("0")
	grafo.agregar_vertice("1")
	grafo.agregar_vertice("2")
	grafo.agregar_vertice("3")
	grafo.agregar_vertice("4")
	grafo.agregar_vertice("5")
	# Agregar aristas
	grafo.agregar_arista("0", "1", 24)
	grafo.agregar_arista("0", "5", 28)
	grafo.agregar_arista("1", "2", 11)
	grafo.agregar_arista("2", "3", 13)
	grafo.agregar_arista("3", "4", 20)
	grafo.agregar_arista("3", "5", 12)
	grafo.agregar_arista("4", "5", 15)

	return grafo

if __name__ == "__main__":
	print("~ TPO ~")

	print("\n~ BFS ~")
	grafo = grafo_ejemplo_bfs()
	solucion = bfs(grafo, "s")
	print("Nodo | Padre")
	print("-----|------")
	for x in solucion:
		print(x, "   | ", solucion[x])

	print("\n~ DFS ~")
	grafo = grafo_ejemplo_dfs()
	solucion = dfs(grafo, "u")
	salida = ''
	for x in solucion:
		salida = salida + str(x) + " -> "
	print(salida[:-4]) # Para remover la ultima flecha

	print("\n~ Floyd ~")
	grafo = grafo_ejemplo_floyd_no_dirigido()
	for solucion in floyd(grafo):
		print(solucion)