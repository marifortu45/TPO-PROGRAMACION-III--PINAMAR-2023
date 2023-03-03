# Elementos utilizados para la resolucion de los algoritmos planteados 
from collections import deque 
from grafo import *

# Constantes utilizadas durante la resolucion
NV = "No visitado"
D = "Descubierto"
V = "Visitado"
INFINITO = 9999

# Implementaciones #
def bfs(grafo, v_origen):
	# Para cada vértice v alcanzable desde el vértice origen, obtiene el camino
	#  más corto desde origen hasta v
	estado = {} 
	padres = {}
	for v in grafo.obtener_vertices():
		estado[v] = NV   # Inicializamos cada vertice como no visitado
		padres[v] = None # Inicializamos los padres de cada vertice
	estado[v_origen] = D
	padres[v_origen] = None
	cola = deque() # Creamos una cola
	cola.append(v_origen) # Agregamos el vertice de origen
	while cola:
		v = cola.popleft() # Desencolamos para evaluar los adyacentes del nodo
		for w in grafo.obtener_adyacentes(v):
			if estado[w] == NV:
				estado[w] = D
				padres[w] = v 
				cola.append(w) # Al encolar los adyacentes, permite recorrer por niveles
		estado[v] = V # Al evaluar todos los adyacentes, marcamos el actual como Visitado
	return padres # Devolvemos la estructura 'padres' que contiene cada nodo y como acceder a traves de su predecesor

def dfs(grafo, v_origen):
	# Parte desde un vértice fuente explorando recursivamente sus sucesores.
	# Desde el último vértice descubierto v explora en profundidad cada arco 
	# Cuando todos los arcos desde v han sido explorados, la búsqueda retrocede al vértice desde el cual v fue descubierto.
	# El proceso continúa hasta que todos lo vértices alcanzables desde el vértice fuente original han sido descubiertos.
	estado = {}
	solucion = []
	for v in grafo.obtener_vertices(): # Inicializamos todos los nodos como No Visitados
		estado[v] = NV
	_dfs(grafo, v_origen, estado, solucion) # Llamada recursiva	
	return solucion # Devolvemos la solucion que contiene cada nodo y el sucesor a visitar, de forma ordenada

def _dfs(grafo, v_origen, estado, solucion):
	solucion.append(v_origen)
	estado[v_origen] = D 
	for v in grafo.obtener_adyacentes(v_origen):
		if estado[v] == NV:
			_dfs(grafo, v, estado, solucion)
	estado[v_origen] == V # Al evaluar toda la profundidad, marcamos el actual como Visitado

def floyd(grafo):
	# Obtención del camino más corto entre cada para de vértices de un grafo rotulado 
	#  (puede ser dirigido o no dirigido).
	# Obtiene una tabla que brinda el costo menor requerido para ir de un vértice a otro.
	indices = {}
	solucion = [] # Corresponde a una Matriz de costos con los caminos mas cortos
	vertices = grafo.obtener_vertices()
	vi = 0
	wi = 0
	for v in vertices: # Creamos una Matriz de costos
		indices[vi] = v
		solucion.append([])
		wi = 0
		for w in vertices:
			if grafo.estan_conectados(v, w):
				solucion[vi].append([vertices[v][w], v]) 
			else:
				solucion[vi].append([INFINITO, None])
			if v == w: 
				solucion[vi][wi] = [0, None] 
			wi +=1
		vi += 1

	long_vertices = len(vertices) 
	for i in range(long_vertices):
		for j in range(long_vertices):
			for k in range(long_vertices):
				if solucion[i][j][0] > (solucion[i][k][0] + solucion[k][j][0]):
					solucion[i][j][0] = solucion[i][k][0] + solucion[k][j][0] # Guardamos el costo de la arista
					solucion[i][j][1] = indices[k] # Guardamos el predecesor del vertice 
	return solucion
