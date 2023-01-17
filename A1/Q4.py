import time
import random

def random_set (cost_range, item_range, num_items, num_covers):
    K = {}
    U = set(random.sample(range(item_range),num_items))
    print("Items set: ", U)
    covers = []
    check = set()
    copy = num_covers
    while num_covers > 0:
        if num_covers == 1 and check != U:
            print(check)
            cover = list(U-check)
            covers.append(cover)
        cover_size = random.randrange(1,num_items)
        cover = random.sample(list(U),cover_size)
        covers.append(cover)
        check |= set(cover)
        num_covers -= 1

    print("Covers set: ",covers)
    costs = random.sample(range(1,cost_range),copy)
    print("Covers' cost: ",costs)

    K["cost"] = costs
    K["cover"] = covers

    return U, K


def small_set():
    U = set(range(5))
    cost = [2,3,6,1,8]
    cover = [[1,3],[0],[0,1,2],[4],[2,3]]
    K = {}
    K["cost"] = cost
    K["cover"] = cover
    return U, K


def remove(index,l1,l2):
    n1 = []
    n2 = []
    if len(l1) == len(l2):
        for i in range(len(l1)):
            if i != index:
                n1.append(l1[i])
                n2.append(l2[i])
    return n1, n2


def price (costs, covers, C):
    min_price = 0
    index = -1
    for i in range(len(covers)):
        if (len(covers[i])-(len(list(set(covers[i]) & C)))) > 0:
            if min_price == 0:
                min_price = costs[i] / len(covers[i])-(len(list(set(covers[i]) & C)))
                index = i
            else:
                price = costs[i] / len(covers[i])-(len(list(set(covers[i]) & C)))
                if price <= min_price:
                    min_price = price
                    index = i
    return index


def set_cover_greedy (U, K):
    result = {}
    C = set()
    select_cover = []
    select_cost = []
    costs = K["cost"]
    covers = K["cover"]
    while C != U:
        index = price(costs,covers, C)
        select_cover.append(covers[index])
        select_cost.append(costs[index])
        C = C | set(covers[index])
        costs, covers = remove(index, costs, covers)
    result["cover"] = select_cover
    result["cost"] = select_cost
    return result

def set_cover_exhaustive (U, K):
    result = {}
    c = K["cover"]
    n = len(c)
    powerset = [[c[k] for k in range(n) if i&1<<k] for i in range(2**n)]
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

def main():
    #U, K = small_set()
    U, K = random_set(80,80,15,15)
    
    start_time_g = time.process_time()
    result_g = set_cover_greedy(U,K)
    print("running time for greedy: ", time.process_time() - start_time_g, "seconds")
    print(result_g)

    start_time_e = time.process_time()
    result_e = set_cover_exhaustive(U,K)
    print("running time for exhaustive: ", time.process_time() - start_time_e, "seconds")
    print(result_e)


    

if __name__ == '__main__':
    main()


