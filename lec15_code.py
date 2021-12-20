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


def flipPolt(minExp, maxExp, numTrails):  # Exp = exponent
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
        for t in range(numTrails):
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
        meanRatios.append(sum(ratios) / numTrails)
        meanDiffs.append(sum(diffs) / numTrails)
        ratiosDs.append(stdDev(ratios))
        diffsDs.append(stdDev(diffs))
    # Let's do a bunch of plotting.
    pylab.plot(xAxis, meanRatios, 'bo')
    pylab.title("Mean Heads/Tails Ratios ( " + str(numTrails) + " Trails)")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Mean Heads/Trails")
    pylab.semilogx()
    pylab.figure()
    pylab.plot(xAxis,ratiosDs, 'bo')
    pylab.title("SD Heads/Tails Ratios ( " + str(numTrails) + " Trails)")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Standard Deviation")
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.plot(xAxis, meanDiffs, 'bo')
    pylab.title("Mean abs(#Heads - #Tails) ( " + str(numTrails) + " Trails)")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Mean abs(#Heads - #Tails)")
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.plot(xAxis, diffsDs, 'bo')
    pylab.title("SD abs(#Heads - #Tails) ( " + str(numTrails) + " Trails)")
    pylab.xlabel("Number of Flips")
    pylab.ylabel("Standard Deviation")
    pylab.semilogx()
    pylab.semilogy()


def main():
    flipPolt(4,20,20)
    pylab.show()

if __name__ == '__main__':
    main()
