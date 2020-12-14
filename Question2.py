from doctest import testmod

class Uniform:
    low: float
    high: float

    def __init__(self, low: float, high: float):
        self.high = high
        self.low = low

def max_revenue_auction_one(agent1: Uniform, value1: float):
    '''
    This function calculates if agent 1 is winning the revenue or not
    due to mairson revenue
    Define input and expected output:
    >>> max_revenue_auction_one(Uniform(10,30),17)
    Agent 1 wins and pays 15.0
    >>> max_revenue_auction_one(Uniform(10,30),14)
    No agent win
    >>> max_revenue_auction_one(Uniform(20, 40), 25)
    Agent 1 wins and pays 20.0
    >>> max_revenue_auction_one(Uniform(20, 40), 30)
    Agent 1 wins and pays 20.0
    >>> max_revenue_auction_one(Uniform(20, 40), 20)
    No agent win
    >>> max_revenue_auction_one(Uniform(20, 40), 40)
    Agent 1 wins and pays 20.0
    '''
    threshold = agent1.high/2
    rv = 2*value1-agent1.high
    if rv > 0:
        print("Agent 1 wins and pays", threshold)
    else:
        print("No agent win")

def max_revenue_auction_two(agent1: Uniform, agent2: Uniform, value1: float, value2: float):
    '''
    This function calculates who need to win or not agent 1 or 2
    due to mairson avenue
    Define input and expected output:
    >>> max_revenue_auction_two(Uniform(10, 30), Uniform(20, 40), 23, 27)
    Agent 1 wins and pays 22.0
    >>> max_revenue_auction_two(Uniform(10, 30), Uniform(20, 40), 14, 19)
    No agent wins
    >>> max_revenue_auction_two(Uniform(10, 30), Uniform(20, 40), 25, 35)
    Agent 2 wins and pays 30.0
    >>> max_revenue_auction_two(Uniform(10, 30), Uniform(20, 40), 30, 40)
    Agent 2 wins and pays 35.0
    >>> max_revenue_auction_two(Uniform(10, 30), Uniform(20, 40), 30, 30)
    Agent 1 wins and pays 25.0
    '''
    # computing the r(v) function and the threshold of each participant
    rv1 = 2*value1-agent1.high
    rv2 = 2*value2-agent2.high
    threshold1 = (rv2 + agent1.high)/2
    threshold2 = (rv1 + agent2.high)/2

    # values assign before if's to determine who is the winner
    winner = 0
    winning = True
    max_pay = 0

    # Checking who is higher
    if rv1 > rv2 and rv1 > 0:
        max_pay = threshold1
        winner = 1
        winning = False
    if rv2 > rv1 and rv2 > 0:
        max_pay = threshold2
        winner = 2
        winning = False

    # if no one is winning
    if winning:
        print("No agent wins")
        return

    # if someone wins
    print("Agent", winner, "wins and pays", max_pay)


# call the testmod function
if __name__ == '__main__':
    testmod(name='max_revenue_auction', verbose=True)