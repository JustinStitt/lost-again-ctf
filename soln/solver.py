import util

grid = util.convert_to_grid()
offsets = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

def get_offset_neighbours(r, c):
    neighbours = []
    for (ro, co) in offsets:
        if r + ro < 0 or r + ro > 7 or c + co < 0 or c + co > 7: continue
        neighbours.append((c+co, r+ro))
    return neighbours

def generate_graph():
    graph = {}
    ri, ci = (0, 0)
    for r in grid:
        ci = 0
        for c in r:
            graph[(ci, ri)] = get_offset_neighbours(ri, ci)
            ci += 1
        ri += 1
    return graph

graph = generate_graph()

run = True
def knights_tour(start):
    global graph
    visited = [[0]*8 for _ in range(8)]
    def traverse(r, c, visited, pos):
        global run
        if not run: return 
        visited[c][r] = pos
        if pos >= 64:  # 64 vertices seen
            for r in visited:
                for c in r:
                    print(c, end = ' ')
                print()
            run = False
            return
        neighbours = [neighbour for neighbour in graph[(c, r)] if visited[neighbour[0]][neighbour[1]] == 0]
        neighbours = sorted(neighbours, key = lambda x : len(graph[(x[1],x[0])]))
        for neighbour in neighbours:
            traverse(neighbour[1], neighbour[0], visited, pos+1)
        
        visited[c][r] = 0

    traverse(start[1], start[0], visited, 1)

knights_tour((4, 3))