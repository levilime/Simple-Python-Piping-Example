'''
Test out the performance difference between piping in and from python programs and
just having the functionality in one program, the file used for piping is called fibofibo

call from shell with: python -c "from pipecomparison import fiboin, fiboremote; fiboremote(42); fiboin(42)"
'''
import time
import os
import sys

from subprocess import Popen, PIPE


def fiboin(n):
    # solves fibonacci within the current python run
    return fibofunction(fibonormal, n)


def fiboremote(n):
    # solves fibonacci by asking through pipe input and output about the fibo compuation
    return fibofunction(fibopipe, n)


def fibopipe(f):
    # call this files main function pipe input, it contains the program to use (python) and arguments for the program
    # file, and two fibonacci numbers and stdout=PIPE makes it so that the output of the pipe is gotten
    p = Popen(['python', '-u', os.path.dirname(os.path.abspath(__file__))+"/pipecomparison.py", str(f[0]), str(f[1])], bufsize=1, stdout=PIPE )
    # read the output of the pipe, which is the print statement on line 52
    output, stderr = p.communicate()
    # decode bytes in string format and parse
    output = output.decode("utf-8").split("[")[1].split("]")[0].split(",")
    f = int(output[0]), int(output[1])
    print(f)
    return f


if __name__ == "__main__":
    # when fiboremotefunction opens the pipe this piece of code is called, it takes the arguments send
    # to it and calculates the next fibonacci number
    print(str("["+str(int(sys.argv[2]))+","
              + str(int(sys.argv[1]) + int(sys.argv[2]))+"]").encode("utf-8"))


def fibonormal(f):
    return f[1], f[0] + f[1]


def fibofunction (method, n):
    start_time = time.time()
    f = (0, 1)
    if n < 1:
        return f[0]
    n -= 1
    while n > 0:
        f = method(f)
        n -= 1
    print ("Result: "+ str(f[1]))
    print("The time that " + method.__name__ +" took is:"+ str(time.time() - start_time))
    return f[1]

