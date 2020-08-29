import pygraphviz as pgv

# A=pgv.AGraph(directed=True)
# A.node_attr['style']='filled'
# A.add_edge(1, 2)
# A.add_edge(2, 3)
# A.add_edge(3, 4)
# A.add_edge(4, 1)

# n = A.get_node('1')
# n.attr['fillcolor']="#CCCCFF"
# n.attr['label'] = 'MY LOVELY LABEL'
# for key in n.attr:
#     print (key + ":" + n.attr[key])

# A.layout(prog='dot')
# A.draw('map.svg', format='svg')

# A.write('file.neato')

B = pgv.AGraph("file.dot", directed=True)

B.layout()
B.draw('map1.svg', format='svg')