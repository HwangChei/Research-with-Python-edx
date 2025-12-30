import random 
def majority_vote(votes):
    """
     xxx
    """ 
    vote_counts = {}
    for vote in votes:
        #known word
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
        #unknown word
    winners =[]
    max_counts = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_counts:
            winners.append(vote)
    return random.choice(winners)


votes = [1,2,2,3,1,2,2,2,2,3,1,3,3,3,3]
winner = majority_vote(votes)
winner

import scipy.stats as ss
def majority_vote_short(votes):
    """
     Return the most common element votes in votes.
    """ 
    mode, count = ss.mstats.mode(votes)
    return mode
votes = [1,2,2,3,1,2,2,2,2,3,1,3,3,3,3]
majority_vote_short(votes)
