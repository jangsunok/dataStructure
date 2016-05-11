import networkx as nx
import matplotlib.pyplot as plt



#그래프를 이미지로 만들기 위한 파일
#실행시 course.png파일을 만들고 파일이름을 리턴함
#png 파일이 html에서 엑박뜸ㅠㅠ 나중에 db연동 해서 띄게 해야할듯!

def draw_graph(graph):

    # create networkx graph
    G=nx.Graph()

    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

    # add nodes
    for node in nodes:
        G.add_node(node, node_size=200)
        
    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])



    # a="hphob"
    # b="polarity"
    # c="alpha"
    # d="beta"
    # G.add_edge(a,b,weight=0.5)
    # G.add_edge(b,c,weight=0.5)
    # G.add_edge(c,d,weight=0.5)
    # G.add_edge(a,d,weight=0.5)
    # G.add_edge(a,c,weight=0.5)
    # G.add_edge(b,d,weight=0.5)
    # draw graph
    pos = nx.shell_layout(G)
    nx.draw(G, pos)
    #nx.draw_networkx_nodes(G,pos,node_size=100, node_color="white")
    nx.draw_networkx_edges(G,pos,width=6,alpha=0.5,edge_color='black')
    
    #labels
    edge_labels = { ("seoul", "city1"): "hi", ("city1", "city2") : "hello" }
    
    nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif',encoding='utf-8')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    # show graph
    plt.show(encoding='utf-8')
    file = "course.png"
    plt.savefig(file, encoding='utf-8')
    
    return file
    
