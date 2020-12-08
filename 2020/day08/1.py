from functools import reduce


class Program:

    def __init__(self, program):
        self.program = program
        self.accumulator = 0
        self.current_instruction = 0
        self.seen_instructions = []

    def nop(self, value):
        print("Doing NOP @ line %s" % self.current_instruction)
        self.seen_instructions.append(self.current_instruction)
        self.current_instruction += 1
        return    

    def acc(self, value):
        print("Doing ACC @ line %s" % self.current_instruction)
        self.accumulator += value
        self.seen_instructions.append(self.current_instruction)
        self.current_instruction += 1
        return

    def jmp(self, value):
        print("Doing JUMP @ line %s" % self.current_instruction)
        self.seen_instructions.append(self.current_instruction)
        self.current_instruction += value
        return

    def do_current_instruction(self):
        print("Step %s:" % len(self.seen_instructions))
        if self.current_instruction in self.seen_instructions:
            raise Exception(
                "Loop prevention kicked in at instruction %s, "
                "after %s executions, "
                "accumulator: %s" % (self.current_instruction,
                                     len(self.seen_instructions),
                                     self.accumulator)
            )
        instruction = self.program[self.current_instruction]
        inst, value = instruction.split(' ')
        getattr(self, inst)(int(value))

    def __call__(self):
        while True:
            self.do_current_instruction()
        return self.accumulator


with open('input') as rawinput:
    program = [l.strip() for l in rawinput.read().split('\n')]

print(Program(program)())
