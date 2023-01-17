import time
import random
'''
It generate a random set cover sample by inputs.
cost_range : the range of cost for each item, start from 1
item_range : the range of items, start from 0
num_items : the size of U
num_covers : the size of K (maximum is the size of U)
'''
def random_set (cost_range, item_range, num_items):
    K = {}
    U = set(random.sample(range(item_range),num_items))
    print("Items set: ", U)
    covers = []
    check = set()
    num_covers = random.randint(1,num_items-1) # the number of covers is between 1 and the number of items
    copy = num_covers
    while num_covers > 0:
        if num_covers == 1 and check != U: # prevent there are items in U are not covered
            cover = list(U-check)
            covers.append(cover)
            break
        cover_size = random.randrange(1,num_items)
        cover = random.sample(list(U),cover_size)
        covers.append(cover)
        check |= set(cover)
        num_covers -= 1
    

    print("Covers set: ",covers, copy)
    costs = random.sample(range(1,cost_range),copy)
    print("Covers' cost: ",costs)

    K["cost"] = costs
    K["cover"] = covers

    return U, K

'''
A fixed set cover sample
'''
def small_set():
    U = set(range(5))
    cost = [2,3,6,1,8]
    cover = [[1,3],[0],[0,1,2],[4],[2,3]]
    K = {}
    K["cost"] = cost
    K["cover"] = cover
    return U, K

'''
Remove item of an index from two list
'''
def remove(index,l1,l2):
    n1 = []
    n2 = []
    if len(l1) == len(l2):
        for i in range(len(l1)):
            if i != index:
                n1.append(l1[i])
                n2.append(l2[i])
    return n1, n2

'''
calculate the minimal price for the uncovered items in the selected cover
'''
def price (costs, covers, C):
    min_price = 0
    index = -1
    for i in range(len(covers)):
        if (len(covers[i])-(len(list(set(covers[i]) & C)))) > 0: # if there exist a uncovered item in the selected cover
            if min_price == 0: # if is the first iteration
                min_price = costs[i] / len(covers[i])-(len(list(set(covers[i]) & C)))
                index = i
            else:
                price = costs[i] / len(covers[i])-(len(list(set(covers[i]) & C)))
                if price <= min_price: # update the minimum price
                    min_price = price
                    index = i
    return index
'''
Use greedy algorithm to solve set cover
'''
def set_cover_greedy (U, K):
    result = {}
    C = set()
    select_cover = []
    select_cost = []
    costs = K["cost"]
    covers = K["cover"]
    while C != U: # until the select covers cover all the items in U
        index = price(costs,covers, C) # return the index of the selected cover at this iteration
        select_cover.append(covers[index])
        select_cost.append(costs[index])
        C = C | set(covers[index]) # combine the items in the selected cover into the selected items
        costs, covers = remove(index, costs, covers)
    result["cover"] = select_cover
    result["cost"] = select_cost
    return result

def set_cover_exhaustive (U, K):
    result = {}
    c = K["cover"]
    n = len(c)
    powerset = [[c[k] for k in range(n) if i&1<<k] for i in range(2**n)] # get all the subset of K
    min_cost = 0
    select_cover = []
    select_cost = []
    for cover_set in powerset:
        check = set()
        for i in cover_set:
            check |= set(i)
        if check == U:  # check whether this subset of the total covers contain all the items in U
            total_cost = 0
            costs = []
            for i in cover_set:
                index = K["cover"].index(i)
                total_cost += K["cost"][index]
                costs.append(K["cost"][index])
            if min_cost == 0 or total_cost <= min_cost:
                min_cost = total_cost
                select_cover = cover_set
                select_cost = costs
    result["cover"] = select_cover
    result["cost"] = select_cost
    return result


'''
Check if there exist a covers that hits the constrain as y grow.
'''
def check_constrains(y, constrains):
    result = False # use this boolean to show whether there exist a cover that hits the constrain
    constrain_id = -1
    for i in range(len(constrains)):
        if y < constrains[i]:
            result = False
        else: # if there exist a cover that hits the constrain, break the loop.
            result = True
            constrain_id = i
            break
    
    return result,constrain_id
'''
Use primal dual algorithm to solve set cover
'''
def set_cover_primal_dual (U, K):
    result = {}
    list_of_item = list(U)
    y = [0]*len(list(U)) # construct a counter for each item
    x = [0]*len(K["cover"]) # an indicator to show whether the ith cover is selected or not
    covers = K["cover"]
    costs = K["cost"]
    C = set()
    while C != U:
        uncovered = U-C 
        e = random.choice(list(uncovered)) # randomly choose the counter for a uncovered item
        index_of_e = list_of_item.index(e)
        e_sets = [] # a list of covers that this uncovered item e is in
        constrains = [] # the corresponding cost for each cover in e_set
        for i in range(len(covers)):
            if e in covers[i]:
                e_sets.append(i)
                constrains.append(costs[i])
        meet_constrain,constrain_id = check_constrains(y[index_of_e],constrains)
        while meet_constrain != True: # when there is a cover being selected, it will break the loop
            y[index_of_e] += 1
            meet_constrain,constrain_id = check_constrains(y[index_of_e],constrains)
            
        selected_cover_id = e_sets[constrain_id]
        x[selected_cover_id] = 1 # mark the selected cover
        C = C | set(covers[selected_cover_id])
    select_covers = []
    select_costs = []
    for i in range(len(x)):
        if x[i] == 1:
            select_covers.append(covers[i])
            select_costs.append(costs[i])
    
    result["cover"] = select_covers
    result["cost"] = select_costs
    return result
    
        

def total_cost(result):
    list = result["cost"]
    t = 0
    for l in list:
        t = t + l
    return t



def main():
    #U, K = small_set()
    #U, K = random_set(80,80,5)

    a_g = 0
    a_p = 0

    loop = 0
    
    while loop < 20:
        U, K = random_set(80,80,15)
        #start_time_g = time.process_time()
        result_g = set_cover_greedy(U,K)
        g = total_cost(result_g)
        #print("running time for greedy: ", time.process_time() - start_time_g, "seconds")
        #print(result_g)

        #start_time_e = time.process_time()
        result_p = set_cover_primal_dual(U,K)
        p = total_cost(result_p)
        #print("running time for primal_dual: ", time.process_time() - start_time_e, "seconds")
        #print(result_e)

        result_e = set_cover_exhaustive(U,K)
        e = total_cost(result_e)
        if loop == 0:
            a_g = g/e
            a_p = p/e
        else:
            if a_g < g/e:
                a_g = g/e
            if a_p < p/e:
                a_p = p/e
        loop += 1
    
    print("approximation ratio of greedy: ", a_g)
    print("approximation ratio of primal dual: ", a_p)



if __name__ == '__main__':
    main()