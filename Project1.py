# List of used Libraries
import numpy as np
import copy
from collections import deque


def BlankTileLocaton(CurrentNode): # Determines the position of empty tile defines initial state
    for i in range(CurrentNode.shape[0]):
        for j in range(CurrentNode.shape[1]):
            if CurrentNode[i, j] == 0:
                return i, j


def Solvable(Node, goal): #  Funtion added to check if a solution exist
    list=copy.deepcopy(Node)
    cont = 0
    for i, val in enumerate(list):
            if (val > goal[i]) & val!=0:
                cont+=1

    return cont % 2 == 0

def ActionMoveLeft(CurrentNode, Parent, N_idx, P_idx): # Calculates if 0 can move to his left
    new_state = CurrentNode[:]
    index = new_state.index(0)

    if index not in [0, 1, 2]: # Defines the boundary of a left move
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        N_idx += 1 # Defines that this current move comes from P_idx

        Node = {'state': new_state, 'parent': Parent, 'Node_ind': N_idx, 'Parent_ind': P_idx} # storage my new node in a dictionary with its respective parent, and index

        if Node['state'] == Parent: # compares if new node is equal to parent
            return -1 # returns a flag to avoid this calculation
        else:

            return Node
    else:   # return a flag if the move is not posible
        return -1


def ActionMoveRight(CurrentNode, Parent, N_idx, P_idx): # Same idea as ActionMoveLeft but applied to Right
    new_state = CurrentNode[:]
    index = new_state.index(0)

    if index not in [6,7,8]:
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        N_idx += 1
        Node = {'state': new_state, 'parent': Parent, 'Node_ind': N_idx, 'Parent_ind': P_idx}

        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        return -1


def ActionMoveUp(CurrentNode, Parent, N_idx, P_idx): # Same idea as previous nodes
    new_state = CurrentNode[:]
    index = new_state.index(0)

    if index not in [0, 3, 6]:
        temp = new_state[index -1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        N_idx += 1
        Node = {'state': new_state, 'parent': Parent, 'Node_ind': N_idx, 'Parent_ind': P_idx}

        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        return -1


def ActionMoveDown(CurrentNode, Parent, N_idx, P_idx):# Same idea as ActionMoveLeft but applied to Right
    new_state = CurrentNode[:]
    index = new_state.index(0)

    if index not in [2,5,8]:
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        N_idx += 1
        Node = {'state': new_state, 'parent': Parent, 'Node_ind': N_idx, 'Parent_ind': P_idx}

        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        return -1


def ActionMoveUpperLeft(CurrentNode, Parent, N_idx, P_idx): # Same idea as ActionMoveLeft but applied to Right
    new_state = CurrentNode[:]
    index = new_state.index(0)

    if index not in [0, 1, 2, 3, 6]:
        temp = new_state[index - 4]
        new_state[index - 4] = new_state[index]
        new_state[index] = temp
        N_idx += 1
        Node = {'state': new_state, 'parent': Parent, 'Node_ind': N_idx, 'Parent_ind': P_idx}

        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        return -1


def ActionMoveUpperRight(CurrentNode, Parent, N_idx, P_idx): # Same idea as ActionMoveLeft but applied to Right
    new_state = CurrentNode[:]
    index = new_state.index(0)

    if index not in [0,3,6,7,8]:
        temp = new_state[index + 2]
        new_state[index + 2] = new_state[index]
        new_state[index] = temp
        N_idx += 1
        Node = {'state': new_state, 'parent': Parent, 'Node_ind': N_idx, 'Parent_ind': P_idx}

        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        return -1


def ActionMoveLowerLeft(CurrentNode, Parent, N_idx, P_idx): # Same idea as ActionMoveLeft but applied to Right
    new_state = CurrentNode[:]
    index = new_state.index(0)

    if index not in [0,1,2,5,8]:
        # Swap the values.
        temp = new_state[index - 2]
        new_state[index - 2] = new_state[index]
        new_state[index] = temp
        N_idx += 1
        Node = {'state': new_state, 'parent': Parent, 'Node_ind': N_idx, 'Parent_ind': P_idx}

        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        # Can't move it, return None
        return -1


def ActionMoveLowerRight(CurrentNode, Parent, N_idx, P_idx): # Same idea as ActionMoveLeft but applied to Right
    new_state = CurrentNode[:]
    index = new_state.index(0)

    if index not in [2,5,6,7,8]:
        temp = new_state[index + 4]
        new_state[index + 4] = new_state[index]
        new_state[index] = temp
        N_idx += 1
        Node = {'state':new_state, 'parent': Parent, 'Node_ind': N_idx, 'Parent_ind': P_idx}
        if Node['state'] == Parent:
            return -1
        else:

            return Node
    else:
        return -1


def branch_nodes(Node, Parent, N_idx, P_idx): # funtion that determines the all the posible moves of cero. It returns my new nodes from its parent
    Nodes=[]
    #Nodes.append(ActionMoveUpperRight(Node, Parent, N_idx, P_idx)) # intend to calculate move in diagonal
    Nodes.append(ActionMoveLeft(Node, Parent, N_idx, P_idx))
    if Nodes[0] != -1: # condition that consider a flag as a node even that after it will get erased
        N_idx = Nodes[0]['Node_ind']
    #Nodes.append(ActionMoveLowerLeft(Node, Parent, N_idx, P_idx))
    Nodes.append(ActionMoveRight(Node, Parent, N_idx, P_idx))
    if Nodes[1] != -1:
        N_idx = Nodes[1]['Node_ind']
    Nodes.append(ActionMoveUp(Node, Parent, N_idx, P_idx))
    if Nodes[2] != -1:
        N_idx = Nodes[2]['Node_ind']
    Nodes.append(ActionMoveDown(Node, Parent, N_idx, P_idx))
    #Nodes.append(ActionMoveUpperLeft(Node, Parent, N_idx, P_idx))
    #Nodes.append(ActionMoveLowerRight(Node, Parent, N_idx, P_idx))
    if Nodes[3] != -1:
        N_idx = Nodes[3]['Node_ind']
    Nodes = [x for x in Nodes if x != -1]
    #print("exit branchs", Nodes)

    return Nodes


if __name__ == '__main__':
    #____Inicial Data
    #define Matrix
    Goal = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 0]])
    Initial = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 0, 8]])

    # # # # # # # # # P R O G R A M # # # # # # # # #  #  #
    In =list(np.reshape(Initial,9,order='F'))

    goal = list(np.reshape(Goal, 9, order='F'))

    ######## Solvable checking code##########3
    Sol=Solvable(In, goal)
    if Sol == True :

        nodes = deque()
        Parents = deque()
        New_Nodes = deque()
        father = {'state': In, 'parent': None, 'Node_ind': 1, 'Parent_ind': 0} # condition that defines a dictionary to store the values and nodes
        # Create the queue with the root node in it.
        node = copy.deepcopy(father)

        #New_Layer=[]
        Parents.append(node)

        x = 0
        d = open("Nodes.txt", "w+")
        n = open("NodesInfo.txt", "w+")
        N_idx = node['Node_ind']
        P_idx = node['Parent_ind']
        while True:
            father = node['state']
            if node['state'] == goal:
                break
            else:
                New_Nodes = branch_nodes(node['state'], father, N_idx, P_idx)  # calculate the possible nodes excluding the ones that have been already calculated.
                parentsStates = [parent['state'] for parent in Parents]
                for New_Node in New_Nodes:                                     # Condition to store only new nodes
                    if New_Node['state'] not in parentsStates:
                        Parents.append(New_Node)
            node = Parents[x+1]                         # this instruction refress the node to continue with the next iteration
            N_idx = New_Node['Node_ind']+1
            P_idx = node['Node_ind']
            np.savetxt(d, [node['state']], fmt='%.i')
            aux1 = node['Node_ind']
            aux2 = node['Parent_ind']
            Node_info = np.array([aux1,aux2])

            np.savetxt(n, [Node_info], fmt='%.i')
            x = x+1
            #print([parent['parent'] for parent in Parents])
        d.close()
        n.close()
        backParents = [parent for parent in Parents if parent['state'] == goal]
        print('Goal:\t\t', goal)
        print('Init:\t\t', In)

        while True:
            parentGoal = backParents[-1]
            if parentGoal['state'] == In:
                break
            parentForGoal = [parent for parent in Parents if parent['state'] == parentGoal['parent']]
            backParents.append(parentForGoal[0])
            #print(parentForGoal)
        # CHEcKING RESULTS

        # print([parent['Node_ind'] for parent in backParents])
        # print(len(backParents))

        f = open("nodePath.txt", "w+")
        for i in range(len(backParents)):

            print(backParents[-i-1]['state'])
            np.savetxt(f, [backParents[-i-1]['state']], fmt='%.i')
        f.close()
    else:
        print("This puzzle doesn't have a solution")
