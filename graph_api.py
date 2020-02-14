from igraph import *

def gen_graph_from_list_of_lists(l, node_name_on_index_0=True):
    G = Graph()
    G.add_vertices(len(l))
    nr_vertices = len(l)

    if node_name_on_index_0:
        for i in range(nr_vertices):
            G.vs[i]["Name"] = l[i][0]
            if len(l[i]) != 1:
                for j in l[i][1:len(l[i])]:
                    G.add_edge(i, j)
    else:
        for i in range(nr_vertices):
            G.vs[i]["Name"] = i
            for j in l[i]:
                G.add_edge(i, j)
    graph_draw(G, nr_vertices)
    return

def graph_draw(G, nr_vertices):
    lay = G.layout('circle')
    position = {k: lay[k] for k in range(nr_vertices)}
    Y = [lay[k][1] for k in range(nr_vertices)]
    M = max(Y)

    es = EdgeSeq(G)  # sequence of edges
    E = [e.tuple for e in G.es]  # list of edges

    L = len(position)
    Xn = [position[k][0] for k in range(L)]
    Yn = [2 * M - position[k][1] for k in range(L)]
    Xe = []
    Ye = []
    for edge in E:
        Xe += [position[edge[0]][0], position[edge[1]][0], None]
        Ye += [2 * M - position[edge[0]][1], 2 * M - position[edge[1]][1], None]

    labels = G.vs.get_attribute_values("Name")

    import plotly.graph_objects as go
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Xe,
                             y=Ye,
                             mode='lines',
                             name='Edge',
                             line=dict(color='rgb(100,100,100)', width=2),
                             hoverinfo='none',
                             text=labels
                             ))
    fig.add_trace(go.Scatter(x=Xn,
                             y=Yn,
                             mode='markers+text',
                             name='Node',
                             marker=dict(symbol='circle',
                                         size=50,
                                         color='#6175c1',  # '#DB4551',
                                         line=dict(color='rgb(50,50,50)', width=1)
                                         ),
                             text=labels,
                             textfont={"size": 25},
                             textposition="middle center",
                             hoverinfo='text',
                             opacity=1
                             ))

    fig.write_html('Graph.html', auto_open=True)
    return