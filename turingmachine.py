"""
    A Turing Machine Implemented in Python
    
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

        
"""
class Tape:
    def __init__(self):
        self.position=0
        self.tape=[]
        self.blank='b'
    def move_left(self):
        if self.position >1:
            self.position = self.position-1
        else:
            self.tape.insert(-1, self.blank)
            self.position=0
    def move_right(self):
        self.position = self.position + 1
    def read(self):
        self.head=self.tape[self.position]
        return self.head
    def set_cell(self,value):
        self.tape[self.position]=value
class Machine:
    def __init__(self,transitions,initial_state,final_states):
        self.tape = Tape(" ")
        self.initial_state = initial_state
        self.transitions=transitions 
        self.current_state=initial_state
        self.final_state='final'
    def show_tape(self):
        print(self.tape)
    def execute(self):
        tape = self.tape
        for cell in tape:
            for transitions in self.transitions:
                if self.current_state == transitions[0] and self.tape[self.positions] == transitions[1]:
                    self.tape[self.position] = transitions[3]
                    self.current_state = transitions[2]
                if self.current_state==self.final_state:
                    print(tape)
            
