""" Playing to build topo from Arista eAPI"""
from graphviz import Digraph

# add code to pull dynamically from live box

topo = '''{
  "jsonrpc": "2.0",
  "result": [
    {},
    {
      "tablesLastChangeTime": 1483721367.4560423,
      "tablesAgeOuts": 0,
      "tablesInserts": 3,
      "lldpNeighbors": [
        {
          "ttl": 120,
          "neighborDevice": "HP830_LSW",
          "neighborPort": "GigabitEthernet1/0/12",
          "port": "Ethernet47"
        },
        {
          "ttl": 120,
          "neighborDevice": "HP_5500EI",
          "neighborPort": "GigabitEthernet2/0/22",
          "port": "Ethernet48"
        },
        {
          "ttl": 120,
          "neighborDevice": "HP_5500EI",
          "neighborPort": "GigabitEthernet1/0/24",
          "port": "Management1"
        }
      ],
      "tablesDeletes": 0,
      "tablesDrops": 0
    }
  ],
  "id": "EapiExplorer-1"
}'''


neighbors = topo['result'][1]['lldpNeighbors']

def create_topo(root, neigh_list):
    nodes = [root]
    edges = []
    for neighbor in neigh_list:
        nodes.append(neighbor['neighborDevice'])
        edges.append([root, neighbor['neighborDevice'], neighbor['neighborPort'] + "-" + neighbor['port'] ])
    return [nodes, edges]


#Creating the Topo graphic
dot = Digraph(comment='My Network')

def make_topology(network_name, mytopo):
    dot = Digraph(comment=network_name, format='png')
    dot.attr('node', shape='box')
    for i in mytopo[0]:
        dot.node(i)
    for i in mytopo[1]:
        dot.edge(i[0], i[1], i[2])
    return dot

dot = make_topology("My New Network", my_topo)
dot.render(filename='My Topo')


[root, neighbor['neighborDevice'],"label= " + neighbor['neighborPort'] ]
root + " , " + neighbor['neighborDevice'] + " , label= " + neighbor['neighborPort']