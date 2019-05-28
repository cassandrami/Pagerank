
# assumes graph is unweighted (all weights are 1)
# only works with a graph with number labelled nodes, starting at 0
# theres a math/rounding error, so there's a slight difference between nx.pagerank

import networkx as nx
import matplotlib as plt

# pagerank: graph G, damping factor alpha, number of iterations
def prank(G, alpha = .85, it = 10):

    # if the graph is empty, return
    if len(G.nodes()) == 0:
        return


    # init- old ranks, new ranks to update during iteration
    oranks = {}
    nranks = {}

    # populate with 1 evenly divided between all nodes
    for node in G.nodes():
        oranks[node] = 1 / len(G.nodes())


    # iterations

    while it > 0:
        # for each node
        for node in G.nodes():
            #reset current pagerank
            nranks[node] = 1 / len(G.nodes())

        # rank of node i
        for node in G.nodes():

            # init calculation of sum in equation
            total = 0

            # for each edge containing curr node
            for edge in G.edges():

                # if curr node is the source node
                if(edge[1] == node):

                    # math
                    total += (oranks[edge[0]] / G.out_degree(edge[0]))
            # more math
            nranks[node] = (alpha * total) + ( 1 - alpha )

        # reset ranks
        oranks = nranks

        it = it - 1

    return nranks

# testing --> this is the graph from wikipedia

H = nx.DiGraph()

H.add_node(0)
H.add_node(1)
H.add_node(2)
H.add_node(3)
H.add_node(4)
H.add_node(5)

H.add_node(6)
H.add_node(7)
H.add_node(8)
H.add_node(9)
H.add_node(10)


H.add_edge(2, 1)
H.add_edge(1, 2)
H.add_edge(3, 0)
H.add_edge(3, 1)
H.add_edge(4, 1)
H.add_edge(4, 3)
H.add_edge(4, 5)
H.add_edge(5, 4)
H.add_edge(5, 1)

H.add_edge(6, 1)
H.add_edge(6, 4)
H.add_edge(7, 1)
H.add_edge(7, 4)
H.add_edge(8, 1)
H.add_edge(8, 4)
H.add_edge(9, 4)
H.add_edge(10, 4)

#nx.draw(H, with_labels= True)

prank(H)
