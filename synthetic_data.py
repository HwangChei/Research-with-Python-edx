import numpy as np
import pandas as pd
import random

def distance(p1,p2):
    '''Finds the distance between points p1 and p2.'''
    return np.sqrt(np.sum(np.power(p2-p1,2)))
#loop over all points
    #compute the distance between point p and every other point
# sort distances and return those k points that are nearest to point p

points = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
p = np.array([2.5,2])
import matplotlib.pyplot as plt
plt.plot(points[:,0],points[:,1],"ro")
plt.plot(p[0],p[1],"bo")
plt.axis([0.5, 3.5, 0.5, 3.5])

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

def find_nearest_neighbors(p, points, k=5):
    '''
    Find the k nearest nrighbors of point p and return their indices
    '''
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k = 5):
    #find k nearest neighbors
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])
    #predict the class of p based on majority vote
outcomes = np.array([0,0,0,0,1,1,1,1,1])

def make_prediction_grid(predictors, outcomes, limits, h, k):
    '''Classify each points on the prediction grid.'''
    x_min, x_max, y_min, y_max =  limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)

    prediction_grid = np.zeros(xx.shape, dtype = int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x,y])
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)
    return(xx,yy, prediction_grid)
seasons = ["spring", "summer", "fall", "winter"]
print(list(enumerate(seasons)))
for ind, season in enumerate(seasons):
    print(ind, season)