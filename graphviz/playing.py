#from tutorial at http://matthiaseisen.com/articles/graphviz/

import graphviz as gv

g1 = gv.Graph(format='svg')
g1.node('A')
g1.node('B')
g1.edge('A', 'B')

print(g1.source)

filename = g1.render(filename='img/g1.svg')
print (filename)