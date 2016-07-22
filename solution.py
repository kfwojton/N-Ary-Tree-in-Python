
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

listo = [['null',3],[3,1],[1,5],[3,4],[3,10]]
#usage first_node = buld_nary_tree(listo)

def build_n_ary_tree(listo):
    temp_list = []

    for ab in listo:

        if ab[0] in temp_list:


            temp_list.append(ab[1])
            navigate_tree(starting_nodea,ab[0],ab[1])

        elif ab[0] == 'null':
            f = Node(ab[0])
            temp_list.append(ab[1])
            starting_nodea = f
            starting_nodea.add_child(Node(ab[1]))
        else:
            print '[has no parent node]' , ab[0]


    return starting_nodea

def navigate_tree(starting_node,look_for,add_value):
    if starting_node.children:
        for ab in starting_node.children:
            starting_node =  ab
            if look_for == ab.data:
                ab.add_child(Node(add_value))
                pass
            else:
                navigate_tree(starting_node,look_for,add_value)

    else:

        pass
