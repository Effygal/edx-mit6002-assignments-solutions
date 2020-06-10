#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:37:08 2020

@author: Effy Wang

UNIT3-Exercises

"""
#Lecture7 Exercise 3
#5.0/5.0 points (graded)
#Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and outputs the standard deviation of the lengths of the strings. Return float('NaN') if L is empty.

def stdDevOfLengths(L):
    if len(L) == 0:
        return float('NaN')
    total_len = 0.0    
    for string in L:
        l = len(string)
        total_len += l
    mean_len = total_len / len(L)
    count = 0.0
    for string in L:
        l = len(string)
        count += (l-mean_len)**2
    return float((count / len(L)) ** 0.5)

#Correct

#Lecture8 Exercise 1-2
#5.0/5.0 points (graded)
#We are handed a biased coin and want to infer the probability that it lands on heads. Use the code provided for CLT, along with the provided helper function flipCoin, to generate confidence intervals for the probability of heads. You should only need to change a few lines of code.
#
#You have two files: flipcoin.py with the code to fill in and with some code to plot the results, and coin_flips.txt with the flip data.
#
#####################
### Helper functions#
#####################
#def flipCoin(numFlips):
#    '''
#    Returns the result of numFlips coin flips of a biased coin.
#
#    numFlips (int): the number of times to flip the coin.
#
#    returns: a list of length numFlips, where values are either 1 or 0,
#    with 1 indicating Heads and 0 indicating Tails.
#    '''
#    with open('coin_flips.txt','r') as f:
#        all_flips = f.read()
#    flips = random.sample(all_flips, numFlips)
#    return [int(flip == 'H') for flip in flips]
#
#
#def getMeanAndStd(X):
#    mean = sum(X)/float(len(X))
#    tot = 0.0
#    for x in X:
#        tot += (x - mean)**2
#    std = (tot/len(X))**0.5
#    return mean, std
#
#    
##############################
### CLT Hands-on             #
###                          #
### Fill in the missing code #
### Do not use numpy/pylab   #
##############################
#meanOfMeans, stdOfMeans = [], []
#sampleSizes = range(10, 500, 50)
#
#def clt():
#    """ Flips a coin to generate a sample. 
#        Modifies meanOfMeans and stdOfMeans defined before the function
#        to get the means and stddevs based on the sample means. 
#        Does not return anything """
#    for sampleSize in sampleSizes:
#        sampleMeans = []
#        for t in range(20):
#            sample = ## FILL THIS IN
#            sampleMeans.append(getMeanAndStd(sample)[0])
#        ## FILL IN TWO LINES
#        ## WHAT TO DO WITH THE SAMPLE MEANS?
#  
#Paste only the clt() function.
def clt():
    for sampleSize in sampleSizes:
        sampleMeans = []
        for t in range(20):
            sample = flipCoin(sampleSize)## FILL THIS IN
            sampleMeans.append(getMeanAndStd(sample)[0])
        meanOfMeans.append(getMeanAndStd(sampleMeans)[0])
        stdOfMeans.append(getMeanAndStd(sampleMeans)[1])
#Correct
        
#Exercise 4
#5.0/5.0 points (graded)
#You have a bucket with 3 red balls and 3 green balls. Assume that once you draw a ball out of the bucket, you don't replace it. What is the probability of drawing 3 balls of the same color?
#
#Write a Monte Carlo simulation to solve the above problem. Feel free to write a helper function if you wish.
#        
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    count = 0
    for trial in range(numTrials):
        bucket = ["r", "r", "r", "g", "g", "g"]
        picks = []
        for i in range(3):
            pick = random.choice(bucket)
            picks.append(pick)
            bucket.remove(pick)     
        if picks == ["r", "r", "r"] or picks == ["g", "g", "g"]:
            count += 1
    return count / numTrials
#Correct
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        