 Turing Machine Implemented in Python
    
        A Turing Machine is a machine with an infinte tape,
        filled with cells, represented as an array here.
        On each cell a symbol can be printed, and the machine
        may read one cell at a time. The other symbols which
        are not being scanned do not affect the behavior of
        the machine. The machine can move both right and left,
        and change the symbol currently being scanned.

        A Turing Machine is a hypothetical construct, made
        to explore the limits of mechanical computation. It
        can be adapted to simulate any algorithm.

        The 'program' for a Turing machine consists of a group
        of transition rules. For example, a program to change
        a list of binary numbers to their opposites, can be
        written as

        [
            [init,0,init,1]
            [init,1,init,0]
            [init,'b',final,b]
        ]


