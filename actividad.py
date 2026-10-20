import matplotlib.pyplot as plt
import networkx as nx

# ==========================================
# PROBLEMA 1: RED DE NAVEGACIÓN Y ENTREGA
# ==========================================


def crear_grafo_navegacion():
    # Grafo Dirigido y Ponderado
    G = nx.DiGraph()

    # Aristas con costos (Distancias en km)
    rutas = [
        ("Deposito", "Nodo_A", 4),
        ("Deposito", "Nodo_B", 2),
        ("Nodo_A", "Nodo_C", 5),
        ("Nodo_A", "Nodo_D", 10),
        ("Nodo_B", "Nodo_A", 1),
        ("Nodo_B", "Nodo_D", 3),
        ("Nodo_C", "Cliente", 4),
        ("Nodo_D", "Cliente", 2),
    ]

    for u, v, w in rutas:
        G.add_edge(u, v, weight=w)

    return G


def graficar_grafo_navegacion(G):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))

    # Dibujar nodos y aristas
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="skyblue")
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
    nx.draw_networkx_edges(
        G, pos, edgelist=G.edges(), arrowstyle="->", arrowsize=20, edge_color="gray"
    )

    # Dibujar pesos de las aristas
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

    plt.title("Problema 1: Grafo Dirigido y Ponderado - Ruta de Entrega")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# ==========================================
# PROBLEMA 2: ÁRBOL DE ESTADOS 8-PUZZLE
# ==========================================


def generar_espacio_8puzzle_reducido():
    # Grafo No Dirigido representando transiciones entre estados
    G = nx.Graph()

    # Representación de estados simples como tuplas
    estado_inicial = "1-2-3\n4-0-6\n7-5-8"
    e1 = "1-0-3\n4-2-6\n7-5-8"  # Arriba
    e2 = "1-2-3\n4-5-6\n7-0-8"  # Abajo
    e3 = "1-2-3\n0-4-6\n7-5-8"  # Izquierda
    e4 = "1-2-3\n4-6-0\n7-5-8"  # Derecha

    # Estado Meta accesible desde e2
    estado_meta = "1-2-3\n4-5-6\n7-8-0"

    G.add_edge(estado_inicial, e1, action="Arriba")
    G.add_edge(estado_inicial, e2, action="Abajo")
    G.add_edge(estado_inicial, e3, action="Izquierda")
    G.add_edge(estado_inicial, e4, action="Derecha")
    G.add_edge(e2, estado_meta, action="Derecha (Meta)")

    return G, estado_inicial, estado_meta


def graficar_8puzzle(G):
    pos = nx.spring_layout(G, seed=15)
    plt.figure(figsize=(10, 7))

    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color="lightgreen", node_shape="s")
    nx.draw_networkx_labels(G, pos, font_size=8, font_family="monospace")
    nx.draw_networkx_edges(G, pos, width=2, edge_color="blue")

    edge_labels = nx.get_edge_attributes(G, "action")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Problema 2: Espacio de Búsqueda Parcial del 8-Puzzle")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# Ejecución
if __name__ == "__main__":
    g_nav = crear_grafo_navegacion()
    graficar_grafo_navegacion(g_nav)

    g_puz, init, goal = generar_espacio_8puzzle_reducido()
    graficar_8puzzle(g_puz)