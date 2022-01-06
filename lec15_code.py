# coding=utf-8

"""
The formula of standard deviation:
σ(x) = sqrt(1/abs(x)*Σ(x∈X)*(x-μ)^2, μ = mean
"""

# Here is an implementation of the standard deviation
import random

import pylab


def stdDev(X: list) -> float:
    mean = sum(X) / float(len(X))
    tot = 0.0  # tot = total
    for x in X:  # A =Σ(x∈X)
        tot += (x - mean) ** 2  # B =(x-μ)^2
    return (tot / len(X)) ** 0.5  # sqrt(1/abs(x)*Σ(x∈X)*(x-μ)^2))


def flipPolt(minExp, maxExp, numTrials):  # Exp = exponent
    meanRatios = []
    meanDiffs = []
    ratiosDs = []
    diffsDs = []
    xAxis = []  # List of observed sample quantities
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)  # set the each of given sample population, it's 2 as the base.
    for numFlips in xAxis:
        ratios = []
        diffs = []
        for t in range(numTrials):
            numHeads = 0
            for n in range(numFlips):  # to get the number of Heads
                if random.random() < 0.5:
                    numHeads += 1
            numTails = numFlips - numHeads  # to get the number of Tails
            if numTails != 0:
                ratios.append(numHeads / float(numTails))  # warning: the division by 0 is not defined
            else:
                print("WARNING: The fraction is zero")
                ratios.append(float('inf'))
            diffs.append(abs(numHeads - numTails))
        meanRatios.append(sum(ratios) / numTrials)
        meanDiffs.append(sum(diffs) / numTrials)
        ratiosDs.append(stdDev(ratios))
        diffsDs.append(stdDev(diffs))
    # Let's do a bunch of plotting.
    pylab.plot(xAxis, meanRatios, 'bo')
    pylab.title("Mean Heads/Tails Ratios ( " + str(numTrials) + " Trials)")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Mean Heads/Trials")
    pylab.semilogx()
    pylab.figure()
    pylab.plot(xAxis, ratiosDs, 'bo')
    pylab.title("SD Heads/Tails Ratios ( " + str(numTrials) + " Trials)")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Standard Deviation")
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.plot(xAxis, meanDiffs, 'bo')
    pylab.title("Mean abs(#Heads - #Tails) ( " + str(numTrials) + " Trials)")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Mean abs(#Heads - #Tails)")
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.plot(xAxis, diffsDs, 'bo')
    pylab.title("SD abs(#Heads - #Tails) ( " + str(numTrials) + " Trials)")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Standard Deviation")
    pylab.semilogx()
    pylab.semilogy()


def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1.0
    return heads / numFlips


def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    return fracHeads


def labelPlot(nf, nt, mean, sd):
    """nf: numFlips
        nt: numTrial"""
    pylab.title(str(nt) + ' trials of ' + str(nf) + ' flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number OF Trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax - xmin) * 0.02, (ymax - ymin) / 2,
               'Mean = ' + str(round(mean, 6)) + '\nSD = ' + str(round(sd, 6)))
    # pylab.text(pos. on x-axis, pos. on y-axis, text_info)
    # round( x , n)    x -- 数值表达式。
    # n -- 数值表达式，表示从小数点位数。


def makePlots(nf1, nf2, nt):
    """ nt =  number of trials per experiment
        nf1 = number of flips 1st experiment
        nf2 = number of flips 2nd experiment"""
    fracHeads1 = flipSim(nf1, nt)
    mean1 = sum(fracHeads1) / float(len(fracHeads1))
    sd1 = stdDev(fracHeads1)
    pylab.hist(fracHeads1, bins=20)  # Plot a histogram
    xmin, xmax = pylab.xlim()  # I stored the minimum x values and the maximum x value to the current one
    # if you call xlim with no arguments, what it will return (is the minimum x value \
    # value and the minimum y value of the current plot, the current figure.
    ymin, ymax = pylab.ylim()
    labelPlot(nf1, nt, mean1, sd1)
    pylab.figure()  # to plot the figure
    fracHeads2 = flipSim(nf2, nt)
    mean2 = sum(fracHeads2) / float(len(fracHeads2))
    sd2 = stdDev(fracHeads2)
    pylab.hist(fracHeads2, bins=20)
    pylab.hist(fracHeads2, bins=20)
    pylab.xlim(xmin, xmax)
    # set the xlmit to the previous ones that I saved from the previous figure.
    # Q: Why am I doing that?
    # A: Because I want to be able to compare the two figures.
    ymin, ymax = pylab.ylim()
    labelPlot(nf2, nt, mean2, sd2)


def poll(n, p):
    """

    :param n: total number of votes
    :param p: probability for getting the vote.
    :return: votes as received
    """
    votes = 0.0
    for i in range(n):
        if random.random() < p / 100.0:
            votes += 1
    return votes


def testErr(n=5000, p=46.0, numTrials=1000):
    results = []
    for t in range(numTrials):
        results.append(poll(n, p))
    print("size of result: " + str(len(results)))
    print("standard deviation: " + str(stdDev(results)))
    print("std = " + str((stdDev(results) / n ) * 100) + '%')
    """
    什么是标准误差（standard error）呢？看了些文献，有的还是大牛的，定义都不统一，通常来说有两种定义方式：
    1.样本容量为n的标准误差是样本的标准差除以sqrt(n)。ps：这里还有人用样本的标准差除以n来作为标准误差
    （预计是弄错了，只是标准误差是基于整体均值来预计标准差，所以也没有必要说人家错）；
    """
    #  People sometimes call the standard deviation
    # of a set of numbers the "population standard deviation", and write it as σ(n)
    # if we want to get the σ(sigma) which have to divide by n(Sample size)
    # to format as % by using multiple one hundred(100) first.
    results = pylab.array(results) / n
    pylab.hist(results)
    pylab.xlabel("Fraction of Votes")
    pylab.ylabel("Number of Polls")


def main():
    # flipPolt(4,20,20)
    # pylab.show()

    # L = [1, 2, 3, 3, 3, 4]
    # pylab.hist(L, bins=6)

    # makePlots(100, 1000, 100000)
    # pylab.show()

    # testErr(n=10000,numTrials=10000)
    testErr()
    pylab.show()

if __name__ == '__main__':
    main()
