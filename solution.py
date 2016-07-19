

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

listo = [['null',3],[3,1],[1,5]]
# give a list of two numbers each representing a parent child n-ary match


def build_n_ary_tree(listo):
    temp_list = []
    counter = 1

    for ab in listo:
        k = Node(ab[0])
        k.add_child(ab[1])
        if ab[0] == 'null':
            starting_node = k

    return starting_node

def navigate_tree(starting_node):
    if starting_node.children:
        for ab in starting_node.children:
            starting_node =  ab
            navigate_tree(starting_node)
        else:
            #no more children!
            pass
