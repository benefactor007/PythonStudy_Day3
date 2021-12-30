# coding=utf-8
import random, pylab

def clear(n, clearProb, steps: int):
    numRemaining = [n]              # use List to store
    for t in range(steps):
        numRemaining.append(n*((1-clearProb)**t))
    pylab.plot(numRemaining, label = "Exponential")


def clearSim(n, clearProb, steps):
    numRemaining = [n]
    for t in range(steps):
        numLeft = numRemaining[-1]
        for m in range(numRemaining[-1]):       # For molecule m in range
            if random.random() <= clearProb:    # if I came out with sth less than the clear prob
                numLeft -= 1                    # I got rid of that molecule.
        numRemaining.append(numLeft)
    pylab.plot(numRemaining, 'r', label = "Simulation")

def main():
    # clear(1000, 0.01, 500)
    # # pylab.semilogy()
    # pylab.show()
    clear(1000, 0.01, 500)
    clearSim(1000, 0.01, 500)
    pylab.show()

if __name__ == '__main__':
    main()
