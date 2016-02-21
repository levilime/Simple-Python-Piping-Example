# Simple-Python-Piping-Example
A very simple code example to make piping to and from python clear

In the directory of the repo open the command line and execute:
`python -c "from pipecomparison import fiboin, fiboremote; fiboremote(NUMBER); fiboin(NUMBER)"`

The result and the time the execution took is printed, it taught me that it is only feasible to use piping when big computations are involved
and it is infeasibly slow when using piping for small computations that are not parellizable because of the constant time it takes for a new instance to finish.
