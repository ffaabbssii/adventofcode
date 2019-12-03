import csv
from itertools import permutations

STEPSIZE = 4
MULTIPLY = 2
ADD = 1
STOP = 99
INITIAL_INTCODE = list()

def process_intcode(intcode: list):
    position = 0
    while position < len(intcode):
        op_code = intcode[position]
        if op_code == STOP:
            # print(intcode)
            return intcode
        
        operand_pos1 = intcode[position + 1]
        operand_pos2 = intcode[position + 2]
        result_pos =  intcode[position + 3]

        if op_code == ADD:
            result = intcode[operand_pos1] + intcode[operand_pos2] 
        elif op_code == MULTIPLY:
            result = intcode[operand_pos1] * intcode[operand_pos2] 
        else:
            print(f'Operation not known. Operant = {intcode[position]}')
        intcode[result_pos] = result
        position += STEPSIZE





def main():
    with open('2019/day2_input.txt', 'rt') as f:
        reader = csv.reader(f, delimiter=',', skipinitialspace=True)
        cols = next(reader)
        INITIAL_INTCODE = list(map(int, cols))

    perm = list(permutations(range(0,100,1), 2))
    for pair in perm:
        intcode = INITIAL_INTCODE.copy()
        intcode[1] = pair[0]
        intcode[2] = pair[1]
        result = process_intcode(intcode)
        if result[0] == 19690720:
            print(pair)
            print(100*pair[0] + pair[1])
            break




if __name__ == "__main__":
    main()
    assert process_intcode([1,0,0,0,99]) == [2,0,0,0,99]
    assert process_intcode([2,3,0,3,99]) == [2,3,0,6,99]
    assert process_intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert process_intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99] 
    