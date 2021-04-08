from typing import List


def multiply_to_elements_except_itself_brute_force(numbers: List[int]) -> List[int]:
    """Time complexity = (n^2), Space complexity = content (assuming we are not counting result object and variables)"""
    if not numbers:
        return False
    result = []
    for index, number in enumerate(numbers):
        if number <=0:
            return False
        product = 1
        for i, j in enumerate(numbers):
            if i == index:
                continue
            product*=j
        result.append(product)
    return result

assert multiply_to_elements_except_itself_brute_force([1,2,3,4,5]) == [120, 60, 40, 30, 24]

#assuming numbers are greater then 0 for below apis.
def multiply_to_elements_except_itself_nlogn_solution(numbers: List[int]) -> List[int]:
    """I am assuming here that return object can be in any order here
    I notice the biggest product will be at where tje smallest element in the list.
    Time complexity = (nlogn + n)
    Space complexity = content (assuming we are not counting result object and variables)"""
    numbers = sorted(numbers)
    result = []
    max_product = 1
    for _, number in enumerate(numbers, start=1):
        max_product*=number
    for _,number in enumerate(numbers, start=1):
        result.append(int(max_product/number))
    return result
assert multiply_to_elements_except_itself_nlogn_solution([5,1,2,3,4]) == [120, 60, 40, 30, 24]


def multiply_to_elements_except_itself_n_solution(numbers: List[int]) -> List[int]:
    """Time complexity = O(2n) or if you want to consider when we constructing result and populating with 0 then O(3n),
    Space complexity = content (assuming we are not counting result object and variables)"""
    input_length = len(numbers)
    result = [0] * input_length
    result[0] = numbers[0]
    for index in range(1, input_length-1):
        result[index] = result[index - 1] * numbers[index]
    result[input_length - 1] = result[input_length - 2]
    product = numbers[input_length - 1]
    for index in range(input_length - 2, 0, -1):
        result[index] = result[index - 1] * product
        product *= numbers[index]
    result[0] = product
    return result

assert multiply_to_elements_except_itself_n_solution([5,1,2,3,4]) == [24, 120, 60, 40, 30]