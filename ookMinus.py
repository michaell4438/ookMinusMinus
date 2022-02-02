import sys

class OokMinusInterpreter:
    tape = []
    pointer = 500
    index = 0
    
    loopList = []
    
    commands = {}
    
    def __init__(self):
        self.tape = self.initTapeArray()
        self.commands = {
            "?.": self.moveLeft,
            ".?": self.moveRight,
            "!!": self.decrement,
            "..": self.increment,
            "!.": self.output,
            ".!": self.input,
            "!?": self.beginLoop,
            "?!": self.endLoop
        }

    def initTapeArray(self):
        array = []
        for i in range(0, 1000):
            array.append(0)
        return array

    def decrement(self):
        self.tape[self.pointer] -= 1
    
    def increment(self):
        self.tape[self.pointer] += 1
    
    def moveLeft(self):
        self.pointer -= 1
        
    def moveRight(self):
        self.pointer += 1
        
    def output(self):
        print(chr(self.tape[self.pointer]), end='')
		
    def input(self):
        self.tape[self.pointer] = ord(sys.stdin.read(1))
        
    def beginLoop(self):
        self.loopList.append(self.index)
    
    def endLoop(self):
        if self.tape[self.pointer] != 0:
            self.index = self.loopList[-1]
        else:
            self.loopList.pop()

    def execute(self, program):
        program = program.split(" ")
        while self.index < len(program):
            try:
                self.commands[program[self.index]]()
            except:
                pass
            self.index += 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception
    with open(sys.argv[1]) as f:
        program = f.read()
        m = OokMinusInterpreter()
        m.execute(program)