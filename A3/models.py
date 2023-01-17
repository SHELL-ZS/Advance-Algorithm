import random

def create_bins(num_bins):
    bins = []
    for n in range(num_bins):
        bins.append(0)
    return bins

def select_bins(bins, num_bins, d):
    # prevent exception
    if num_bins < d:
        return -1
    selector = list(random.sample(range(0, num_bins), d)) # selector d bins randomly
    print(selector)
    choice = -1
    compare = bins[selector[0]]
    # pick a bin from d bins that has the minimum load
    for s in selector:
        if bins[s] <= compare:
            compare = bins[s]
            choice = s
    return choice


def balls_and_bins(num_balls, num_bins):
    # prevent exception
    if num_balls == 0 or num_bins == 0:
        return [],0
    bins = create_bins(num_bins)
    while num_balls > 0:
        select_bin = random.randint(0,num_bins-1) # randomly pick a bin from n bins
        bins[select_bin] = bins[select_bin] + 1
        num_balls -= 1
    
    max_load = max(bins)
    return bins, max_load

def d_choices (num_balls, num_bins, d):
    # prevent exception
    if num_balls == 0 or num_bins == 0:
        return [],0
    bins = create_bins(num_bins)
    while num_balls > 0:
        choice = select_bins(bins,num_bins, d)
        # prevent exception
        if choice < 0:
            return [], 0
        bins[choice] = bins[choice] + 1
        num_balls -= 1
    
    max_load = max(bins)
    return bins, max_load

def main():
    # number of balls
    m = 10
    # number of bins
    n = 3
    # number of choices
    d = 2

    bin_1, max_1 = balls_and_bins(m,n)
    print(bin_1,max_1)

    bin_2, max_2 = d_choices(m,n,d)
    print(bin_2,max_2)


if __name__ == '__main__':
    main()