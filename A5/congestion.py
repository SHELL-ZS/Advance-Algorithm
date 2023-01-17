'''
check if the current edge is a valid path for a player
'''
def check(edge,player_edges):
    for e in player_edges:
        if e == edge:
            return True

'''
cost_str: a+b
         where a is linear rate
               b is flat rate

congest: the number of players went on this path

cost = a*congest + b
'''
def linear_function(cost_str,congest):
    costs = cost_str.split("+")
    flat = 0
    linear = 0
    if costs[0].find(".") == -1:
        linear = int(costs[0])
    else:
        linear = float(costs[0])
    if costs[1].find(".") == -1:
        flat = int(costs[1])
    else:
        flat = float(costs[1])
    cost = congest*linear + flat
    return cost
    
'''
calculate the cost for each player in a pair of strategise(path).

i_path: a list of strings that show player1's strategy from source to destination
        i_path = ['AB','BD']
j_path: a list of strings that show player2's strategy from source to destination
        j_path = ['AB','BD']
edges: a dictionary that contains each edge's cost
        edges = {'AB': '0+3', 'AC': '1+0', 'BC': '0+0.5', 'BD': '1+0', 'CD': '0+3'}
'''
def cost_calculation_2(i_path,j_path,edges):
    edge = list(set(i_path) | set(j_path))
    i_cost = 0
    j_cost = 0
    for e in edge:
        if check(e,i_path) and check(e,j_path): #there is a congestion of 2
            cost = edges[e]
            i_cost += linear_function(cost,2)
            j_cost += linear_function(cost,2)
        elif check(e,i_path):
            cost = edges[e]
            i_cost += linear_function(cost,1)
        else:
            cost = edges[e]
            j_cost += linear_function(cost,1)
    return i_cost,j_cost

'''
calculate the cost for each player in a pair of strategise(path).

i_path: a list of strings that show player1's strategy from source to destination
        e.p. i_path = ['AB','BD']
j_path: a list of strings that show player2's strategy from source to destination
        e.p. j_path = ['AB','BD']
h_path: a list of strings that show player3's strategy from source to destination
        e.p. h_path = ['AB','BD']
edges: a dictionary that contains each edge's cost
        e.p. edges = {'AB': '0+3', 'AC': '1+0', 'BC': '0+0.5', 'BD': '1+0', 'CD': '0+3'}
'''
def cost_calculation_3(i_edge,j_edge, h_edge,edges):
    path = list(set(i_edge) | set(j_edge) | set(h_edge))
    i_cost = 0
    j_cost = 0
    h_cost = 0
    for p in path:
        if check(p,i_edge) and check(p,j_edge) and check(p,h_edge): #there is a congestion of 3
            cost = edges[p]
            i_cost += linear_function(cost,3)
            j_cost += linear_function(cost,3)
            h_cost += linear_function(cost,3)
        elif check(p,i_edge) and check(p,j_edge): #there is a congestion of 2
            cost = edges[p]
            i_cost += linear_function(cost,2)
            j_cost += linear_function(cost,2)
        elif check(p,i_edge) and check(p,h_edge): #there is a congestion of 2
            cost = edges[p]
            i_cost += linear_function(cost,2)
            h_cost += linear_function(cost,2)
        elif check(p,h_edge) and check(p,j_edge): #there is a congestion of 2
            cost = edges[p]
            h_cost += linear_function(cost,2)
            j_cost += linear_function(cost,2)
        elif check(p,i_edge):
            cost = edges[p]
            i_cost += linear_function(cost,1)
        elif check(p,j_edge):
            cost = edges[p]
            j_cost += linear_function(cost,1)
        else:
            cost = edges[p]
            h_cost += linear_function(cost,1)
    return i_cost,j_cost,h_cost

'''
Within the boundary of the matrix/matice found the neighbour of the target item:

if there are 2 players, there maximum 2 horizontal neighbour and 2 vertical neighbour.
if there are 3 players, the maximum 2 horizontal neighbour,  2 vertical neighbour and 2 
back and front neighbour.

'''
def neighbour(index, players, table):
    if players == 2:
        x = index[0] # the row
        y = index[1] # the colunm
        i_neighbours = [] # left and right
        j_neighbours = [] # up and down
        if y-1 >= 0:
            i_neighbours.append(table[x][y-1])
        if y+1 < len(table[0]):
            i_neighbours.append(table[x][y+1])
        if x-1 >= 0:
            j_neighbours.append(table[x-1][y])
        if x+1 < len(table):
            j_neighbours.append(table[x+1][y])
        
        return i_neighbours, j_neighbours
    else:
        x = index[1] # the row
        y = index[2] # the colunm
        z = index[0] # the matrix
        i_neighbours = [] # left and right
        j_neighbours = [] # up and down
        h_neighbours = [] # front and back
        if y-1 >= 0:
            i_neighbours.append(table[z][x][y-1])
        if y+1 < len(table[0][0]):
            i_neighbours.append(table[z][x][y+1])
        if x-1 >= 0:
            j_neighbours.append(table[z][x-1][y])
        if x+1 < len(table[0]):
            j_neighbours.append(table[z][x+1][y])
        if z-1 >= 0:
            h_neighbours.append(table[z-1][x][y])
        if z+1 < len(table):
            h_neighbours.append(table[z+1][x][y])
        return i_neighbours, j_neighbours, h_neighbours
    

''' 
generates the cost table for the game:

for 2 players:
edges = {'AB': '0+3', 'AC': '1+0', 'CB': '0+0.5', 'BD': '1+0', 'CD': '0+3'}
                      p1(i)
     (ci,cj)  'ABBD'    'ACCBBD'    'ACCD'
      'ABBD' [[[5, 5]  , [3.5, 5]  , [4, 4]], 
p2(j) 'ACCBBD'[[5, 3.5], [4.5, 4.5], [5, 3.5]], 
      'ACCD'  [[4, 4]  , [3.5, 5]  , [5, 5]]]
-----------------------------------------------------------------------------
for 3 players:
edges = {'AB': '0+3', 'AC': '1+0', 'BD': '1+0', 'CD': '0+3'}
                        p1(i)
p3(h)        (ci,cj,ch) 'ABBD'     'ACCD'
'ABBD' p2(j) 'ABBD' [[[[6, 6, 6], [4, 5, 5]], 
             'ACCD'   [[5, 4, 5], [5, 5, 4]]], 

                        p1(i)
p3(h)       (ci,cj,ch)  'ABBD'     'ACCD'
'ACCD' p2(j) 'ABBD'  [[[5, 5, 4], [5, 4, 5]], 
             'ACCD'   [[4, 5, 5], [6, 6, 6]]]]

'''
def cost_table(strategies,edges,player_number):
    if player_number == 2:
        table = []
        label = []
        player1_strategies = strategies["player1"]
        player2_strategies = strategies["player2"]
        for j in player2_strategies:
            row = []
            for i in player1_strategies:
                label_pair = [i, j]
                row.append(label_pair)
            label.append(row)

        for j in player2_strategies:
            row = []
            for i in player1_strategies:
                i_path = [i[x:x+2] for x in range(0,len(i),2)]
                j_path = [j[x:x+2] for x in range(0,len(j),2)]
                i_cost, j_cost = cost_calculation_2(i_path,j_path,edges)
                cost_pair = [i_cost, j_cost]
                row.append(cost_pair)
            table.append(row)
        return table, label
    if player_number == 3:
        table = []
        label = []
        player1_strategies = strategies["player1"]
        player2_strategies = strategies["player2"]
        player3_strategies = strategies["player3"]
        for h in player3_strategies:
            matrix = []
            for j in player2_strategies:
                row = []
                for i in player1_strategies:
                    label_pair = [i, j, h]
                    row.append(label_pair)
                matrix.append(row)
            label.append(matrix)
        for h in player3_strategies:
            matrix = []
            for j in player2_strategies:
                row = []
                for i in player1_strategies:
                    i_path = [i[x:x+2] for x in range(0,len(i),2)]
                    j_path = [j[x:x+2] for x in range(0,len(j),2)]
                    h_edges = [h[x:x+2] for x in range(0,len(h),2)]
                    i_cost, j_cost, h_cost = cost_calculation_3(i_path,j_path,h_edges,edges)
                    cost_pair = [i_cost, j_cost, h_cost]
                    row.append(cost_pair)
                matrix.append(row)
            table.append(matrix)
        return table, label

'''
Find Nash equilibriums in a cost table:

For each item (ci,cj,ch) in the table, find it's left and right neighboursc(ci',cj,ch), up and down 
neighbours (ci,cj',ch), and front and back neighbours (ci,cj,ch').

Compare ci with ci', cj with cj', ch with ch', see if any one tend to move, if non, then this item is
a Nash equilibrium.
'''
def nash(table, label, players):
    if players == 2:
        equilibrium = {}
        for j in range(len(table)):
            for i in range(len(table[0])):
                i_neighbours, j_neighbours = neighbour([j,i],players,table)
                check1 = True
                check2 = True
                for hn in i_neighbours:
                    if hn[0] >= table[j][i][0]:
                        check1 = check1 and True
                    else:
                        check1 = check1 and False
                for vn in j_neighbours:
                    if vn[1] >= table[j][i][1]:
                        check2 = check2 and True
                    else:
                        check2 = check2 and False
                if check1 and check2:
                    equilibrium[j,i] = [table[j][i], label[j][i]]
        return equilibrium
    else:
        equilibrium = {}
        for h in range(len(table)):
            for j in range(len(table[0])):
              for i in range(len(table[0][0])):
                i_neighbours, j_neighbours, h_neighbours = neighbour([h, j,i],players,table)
                check1 = True
                check2 = True
                check3 = True
                for i_n in i_neighbours:
                    if i_n[0] >= table[h][j][i][0]:
                        check1 = check1 and True
                    else:
                        check1 = check1 and False
                for j_n in j_neighbours:
                    if j_n[1] >= table[h][j][i][1]:
                        check2 = check2 and True
                    else:
                        check2 = check2 and False
                for h_n in h_neighbours:
                    if h_n[2] >= table[h][j][i][2]:
                        check3 = check3 and True
                    else:
                        check3 = check3 and False
                if check1 and check2 and check3:
                    equilibrium[h,j,i] = [table[h][j][i], label[h][j][i]]
        return equilibrium

'''
player's strategy to destination
'''
def player_strategy(requirements, singe_side_edges, player_number,mode):
    edges = {}
    if mode == "one":
        edges = singe_side_edges
    else:
        keys = singe_side_edges.keys()
        for key in keys:
            edges[key] = singe_side_edges[key]
            edges[key[1]+key[0]] = singe_side_edges[key]
    '''
    Find all valid path in the current topology
    mode = one-way mode (the edge have direction)
    edges = {'AB': '0+3', 'AC': '1+0', 'CB': '0+0.5', 'BD': '1+0', 'CD': '0+3'}
    valid_path = ['AB', 'AC', 'CB', 'ACCB', 'BD', 'ABBD', 'CBBD', 'ACCBBD', 'CD', 'ACCD']
    '''
    edge = []
    for key in edges.keys():
        edge.append(key)
    n = len(edge)
    power = [[edge[k] for k in range(n) if i&1<<k] for i in range(2**n)]
    valid_path = []

    for p in power:
        e = ""
        for i in range(len(p)):
            e += p[i]
        if len(e) > 2:
            correct = True
            for x in range(1,len(e)-1,2):
                if e[x] == e[x+1]:
                    correct = correct and True
                else:
                    correct = correct and False
            if correct:
                valid_path.append(e)
        elif len(e)==2:
            valid_path.append(e)

    '''
    According to player's source and destination, found the feasible path for each player:
    requirements = {'player1': 'AD', 'player2': 'AD'}
    player1: From A to D
    player2: From A to D
    strategies = {'player1': ['ABBD', 'ACCD', 'ABBCCD'], 'player2': ['ABBD', 'ACCD', 'ABBCCD']}
    '''
    strategies = {}
    for key in requirements.keys():
        value = requirements[key]
        player_path = []
        for vp in valid_path:
            if value[0] == vp[0] and value[len(value)-1] == vp[len(vp)-1]:
                player_path.append(vp)
        strategies[key] = player_path
    return cost_table(strategies,edges,player_number)

'''
Read from a input file
Start the congestion game
Write the result to a output file
'''
def start_game(file_name,mode):

    # read from the input file
    player_equirements = {}
    edges = {}
    with open(file_name,'rt') as f:
        text = f.read()
    information = text.split("\n")
    for i in information:
        if i[0:6] == "player":
            player_equirements[i[0:7]] = i[9]+i[12]
        else:
            index = i.find(",",5,11)
            edges[i[1]+i[4]] =i[8:index] + "+" + i[11:-1]

    # start the game
    player_number = len(player_equirements.items())
    strategy_table, label_table = player_strategy(player_equirements,edges, player_number,mode)
    equilibrium = nash(strategy_table,label_table,player_number)

    # output the result
    output_text = ""
    for key in equilibrium.keys():
        value = equilibrium[key][0]
        label = equilibrium[key][1]
        for i in range(player_number):
            num = i +1
            output_text += "player" + str(num) + ", Cost = " + str(value[i]) + ": "
            nodes = []
            for head in range(0,len(label[i]),2):
                nodes.append(label[i][head])
            nodes.append(label[i][-1])
            for n in range(len(nodes)):
                if n == len(nodes)-1:
                    output_text += nodes[n] + ";\n"
                else:
                    output_text += nodes[n] + ", "
    with open('output.txt', 'wt') as f:
        f.write(output_text)


if __name__ == "__main__":
    
    print("Remain: in the one-way edge mode, the direction matters! \n (A, B) means From A to B")
    correct_mode = False
    correct_file = False
    while correct_mode == False:
        mode = input("Enter the edge mode, one-way or two-way [one/two]?")
        if mode == "one" or  mode == "two":
            correct_mode = True
        else:
            print("Please input valid mode")
    print("Remain: the input should follow the example format. \n And there should be at least 2 players and no more then 3 players")
    while correct_file == False:
        file_name = input("Enter a txt file directory: ")
        if file_name[len(file_name)-4:] == ".txt":
            correct_file = True
        else:
            print("Please input txt file")

    start_game(file_name,mode)