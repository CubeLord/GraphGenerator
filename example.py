from graph_api import *

test_l = [[0, 1, 2, 3],
     [1, 3],
     [2, 3],
     [3]]

test_l_2 = [[1, 4],
     [0, 4, 2, 3],
     [1, 3],
     [1, 4, 2],
     [3, 0, 2]]

test_l_3 = [['1', 1, 4],
     ['2', 0, 4, 2, 3],
     ['3', 1, 3],
     ['4', 1, 4, 2],
     ['5', 3, 0, 2]]

gen_graph_from_list_of_lists(test_l_3)
# gen_graph_from_list_of_lists(test_l_2, node_name_on_index_0=False)
# gen_graph_from_list_of_lists(test_l)
