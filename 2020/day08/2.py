from functools import reduce


class TerminationException(Exception):
    pass


class LoopException(Exception):
    pass


class Program:

    def __init__(self, program):
        self.program = program
        self.accumulator = 0
        self.current_instruction = 0
        self.seen_instructions = []

    def nop(self, value):
        # print("Doing NOP @ line %s" % self.current_instruction)
        self.seen_instructions.append(self.current_instruction)
        self.current_instruction += 1
        return    

    def acc(self, value):
        # print("Doing ACC @ line %s" % self.current_instruction)
        self.accumulator += value
        self.seen_instructions.append(self.current_instruction)
        self.current_instruction += 1
        return

    def jmp(self, value):
        # print("Doing JUMP @ line %s" % self.current_instruction)
        self.seen_instructions.append(self.current_instruction)
        self.current_instruction += value
        return

    def do_current_instruction(self):
        # print("Step %s:" % len(self.seen_instructions))
        if self.current_instruction in self.seen_instructions:
            raise LoopException(
                "Loop prevention kicked in at instruction %s, "
                "after %s executions, "
                "accumulator: %s" % (self.current_instruction,
                                     len(self.seen_instructions),
                                     self.accumulator)
            )
        if self.current_instruction >= len(self.program):
            raise TerminationException(
                'Program terminated at instruction %s; '
                'after %s executions, '
                'accumulator: %s' % (self.seen_instructions[-1],
                                     len(self.seen_instructions),
                                     self.accumulator)
            )
        instruction = self.program[self.current_instruction]
        try:
            inst, value = instruction.split(' ')
        except ValueError:
            print(instruction)
            raise
        getattr(self, inst)(int(value))

    def __call__(self):
        is_terminated = False
        while not is_terminated:
            try:
                self.do_current_instruction()
            except TerminationException as e:
                print(e)
                is_terminated = True
        return self.accumulator


with open('input') as rawinput:
    program = [l.strip() for l in rawinput.read().split('\n') if l.strip() != '']


# Brute forcing the shit out of it ...

for i in range(len(program)):
    if program[i][:3] == 'nop':
        print('Changing NOP to JMP at instruction %s' % i)
        altered_program = program[:i] + ['jmp' + program[i][3:], ] + program[i+1:]
    elif program[i][:3] == 'jmp':
        print('Changing JMP to NOP at instruction %s' % i)
        altered_program = program[:i] + ['nop' + program[i][3:], ] + program[i+1:]
    else:
        altered_program = []
    
    if altered_program:
        try:
            acc = Program(altered_program)()
            break
        except LoopException:
            print('Program caught in a loop, continueing ...')

print(acc)
