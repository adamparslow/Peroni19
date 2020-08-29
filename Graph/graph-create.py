import pygraphviz as pgv
import PaperData

A = pgv.AGraph(directed=True, overlap=True, splines=True)

def createEdge(graph, src, dest): 
    graph.add_edge(src, dest)
    
def createNode(graph, node, x, y):
    graph.add_node(node, pos=str(x) + ", " + str(y) + "!")

A.node_attr['style']='filled'
createNode(A, 1, 0, 0)
createNode(A, 2, 1, 0)
createNode(A, 3, 2, 3.12)
createNode(A, 5, 3, 0)

createEdge(A, 1, 2)
createEdge(A, 2, 3)
createEdge(A, 3, 5)
createEdge(A, 5, 1)

# positionNode(A.get_node('1'), 0, 0)
# positionNode(A.get_node('2'), 1, 0)
# positionNode(A.get_node('3'), 2, 3) 
# positionNode(A.get_node('5'), 3, 0)

# n = A.get_node('1')
# n.attr['fillcolor']="#CCCCFF"
# n.attr['label'] = 'MY LOVELY LABEL'

A.layout(prog='neato')
A.draw('map.svg', format='svg')