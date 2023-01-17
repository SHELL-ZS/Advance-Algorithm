import math
import random

"""
Parameters:
-predictions (--boolean metric): The predictions of each expert in total amount 
of trading days, an expert's predictions per line. (Txn)
[[T, F, F, F, T]
 [F, F, T, F, T]
 [T, T, T, T, F]]

-days (--integer): total amount days of trading. (T)
5

-experts (--integer): the number of experts. (n)
3

-outcome (--boolean list): the true result
[T, T, F, T, F]

Output:
-vote_result (--boolean list): outcomes vote by the experts
"""
def wma(predictions, days, experts, outcome):
    weights = [1.0]*experts
    vote_result = []
    for t in range(days):
        yes = 0
        no = 0
        for i in range(experts):
            if predictions[i][t] == True:
                yes += weights[i]
            else:
                no += weights[i]
        
        if yes > no:
            vote_result.append(True)
        else:
            vote_result.append(False)

        for i in range(experts):
            if predictions[i][t] != outcome[t]:
                weights[i] = weights[i]/2
    
    count = 0
    for i in range(days):
        if outcome[i] == vote_result[i]:
            count += 1
    return count/days

'''
Parameters:

-predictions (--boolean metric): The predictions of each expert in total amount 
of trading days, an expert's predictions per line. (Txn)
[[T, F, F, F, T]
 [F, F, T, F, T]
 [T, T, T, T, F]]

-days (--integer): total amount days of trading. (T)
5

-experts (--integer): the number of experts. (n)
3

-outcome (--boolean list): the true result. (T)
[T, T, F, T, F]

-distribution(--float list): the probaility of following each expert's prediction 
on each day.
p^t = (p_1, ..., p_n)
p_i = w_i/sum(w_1,...,w_n)

-costs(--float list):the cost of following each expert's prediction on each day. Set
m^t = p^t. If the expert i's prediction is correct, then m_i = -p_i, otherwise m_i = p_i
m^t = (m_1, .., m_n)
m_i = -p_i, if prediction correct
      p_i, if prediction is wrong


'''
def mwu(predictions, days, experts, outcome, epsilon):
    weights = [1.0]*experts
    
    for t in range(days):
        distribution = []
        cost = []
        weight_sum = sum(weights)
        for i in range(experts):
            distribution.append(weights[i]/weight_sum)
        cost = distribution

        for i in range(experts):
            if predictions[i][t] == outcome[t]:
                cost[i] = -cost[i]

        for w in range(experts):
            weights[w] = weights[w] * math.exp(-epsilon*cost[w])
        
    max_weight = weights.index((max(weights)))
    choice = predictions[max_weight] 

    count = 0
    for i in range(days):
        if outcome[i] == choice[i]:
            count += 1
    return count/days

def main():
    experts = 4
    days = 10
    predictions = []
    epsilon = 0.5
    delta = 0.05

    outcome = [bool(random.getrandbits(1)) for i in range(days)]
    print(outcome)

    # uniformly random prediction
    expert_one = [bool(random.getrandbits(1)) for i in range(days)]

    # always predicts the same as the outcome of the previous day
    expert_two = [bool(random.getrandbits(1))] * days

    # predicts the future outcomes with accuracy 0.5 + delta
    expert_three = []
    accuracy = 0.5 + delta
    for o in outcome:
        population = [o,not o]
        weight = [accuracy, 1-accuracy]
        expert_three = expert_three + random.choices(population,weight)
    
    # always predicts the next outcome as the opposite of the previous one
    expert_four = []
    expert_four.append(bool(random.getrandbits(1)))
    d = 1
    while d < days:
        next = not expert_four[d-1]
        expert_four.append(next)
        d += 1
    
    # one bit prediction
    expert_five = []
    expert_five.append(bool(random.getrandbits(1)))
    for o in range(days):
        if o < len(outcome)-1:
            if outcome[o] == expert_five[o]:
                expert_five.append(expert_five[o])
            else:
                expert_five.append(not expert_five[o])
    
    print(expert_four)
    predictions.append(expert_one)
    predictions.append(expert_two)
    predictions.append(expert_three)
    predictions.append(expert_five)

    a1 = wma(predictions,days,experts,outcome)
    a2 = mwu(predictions,days,experts,outcome,epsilon)
    print("wma: ", a1, "  mwu: ", a2)


if __name__ == '__main__':
    main()
