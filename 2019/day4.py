import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
logger.addHandler(ch)

def is_six_digits_int(input):
    is_int = False
    six_digits = False

    if type(input) == int:
        is_int = True 
    
    if len(get_digits_list(input)) == 6:
        six_digits = True
    
    logger.debug(f'is int:                {is_int}')
    logger.debug(f'has six digits:        {six_digits}')
    return is_int & six_digits


def is_in_range(input,start,stop):
    in_range = (start <= input <= stop)
    logger.debug(f'is in range:           {in_range}')
    return in_range


def digits_never_decrease(input):
    digits_list = get_digits_list(input)
    result = False
    for i in range(0, len(digits_list)-1, 1):
        if digits_list[i] <= digits_list[i+1]:
            result = True
        else:
            result = False
            break
    logger.debug(f'digits_never_decrease: {result}')
    return result


def adjacent_digits(input):
    digits_list = get_digits_list(input)
    result = False
    group_size = 1
    valid_group_found = 0

    for i in range(0, len(digits_list)-1, 1):
        if digits_list[i] == digits_list[i+1]:
            group_size += 1
        else:
            group_size = 1
    
        if group_size == 2:
            valid_group_found +=1
        if group_size == 3:
            valid_group_found -=1     
        
    if valid_group_found > 0:
        result = True
        
    logger.debug(f'adjacent_digits:       {result}')
    return result


def get_digits_list_old(input):
    list_of_digits = list(str(input))       # convert to str and put each digit into a list
    list_of_digits = list(map(int, list_of_digits)) # convert list of str to list of int
    return list_of_digits


def get_digits_list(number, base=10):
    assert number >= 0
    if number == 0:
        return [0]
    l = []
    while number > 0:
        l.append(number % base)
        number = number // base
    l.reverse()    
    return l


def test_all_conditionals(input):
    logger.debug(f'Testing: {input}')
    if not is_six_digits_int(input):
        raise Exception('Input is not type: integer')
    result = []
    result.append(is_six_digits_int(input))
    result.append(is_in_range(input,145852, 616942))
    result.append(digits_never_decrease(input))
    result.append(adjacent_digits(input))
    return result

def main():
    valid_input = []
    logger.info('starting')
    for input in range(145852,616942,1):
        conditions = test_all_conditionals(input)
        if False not in conditions:
            valid_input.append(input)
    logger.info(valid_input)
    logger.info(f'Number of valid Inputs in range: {len(valid_input)}')




if __name__ == "__main__":
    main()
    # print(adjacent_digits(112233))
    # print(adjacent_digits(123444))
    # print(adjacent_digits(112223))
    # print(adjacent_digits(111122))
    # test_all_conditionals(111111)