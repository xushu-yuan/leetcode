import math
from random import random, randint, shuffle

def largestPerimeter(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        if len(nums) >= 3:
            nums.sort(reverse=True)
            for i in range(2, len(nums)):
                if nums[i] + nums[i-1] > nums[i-2]:
                    result = nums[i]+nums[i-1]+nums[i-2]
                    return result
            return result
        else:
            return result
    

def output_permutative(s, first_index):
    if len(s) == 1:
        print("".join(s))
    else:
        for i in range(first_index, len(s)):
            if first_index == len(s)-1:
                print("".join(s))
            swap(s, first_index,i)
            output_permutative(s,first_index+1)
            swap(s, first_index,i)


def swap(string,i,j):
    tmp = string[i]  
    string[i] = string[j]  
    string[j] = tmp 

def prime_number_solution_1(start, end):
    start = 2 if start < 2 else start
    for num in range(start, end+1):
        if all(num % i != 0 for i in range(2, num)):
            print(num)

# remove all even numbers and the last half
def prime_number_solution_2(start, end):
    start = 2 if start < 2 else start
    for num in range(start, end+1):
        if num > 2 and num % 2 == 0:
            continue
        elif all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            print(num)


# remove i*n only works when counting from 2
def prime_number_solution_3(n):
    prime = [True]*(n+1)
    for p in range(2, n+1):
        if prime[p]:
            print(p)
            for i in range(p, n+1, p):
                prime[i] = False

def count_element_in_string(string, element):
    # # using count()
    # print(string.count(element))

    # #generator
    n = sum(s == element for s in string)
    print(n)

def random_number(start, end):
    return start + (end - start)*random()

def remove_duplicate_in_string_method_1(string):
    s = set(string)
    print("".join(s))

def remove_duplicate_in_string_method_2(string):
    d = sorted(dict.fromkeys(string))
    print("".join(d))

# stupid way
def remove_duplicate_in_string_method_3(string):
    result = []
    for s in string:
        if s not in result:
            result.append(s)
    print("".join(result))

def compare(src_data, target_data):
    # we assume these are 2 dict from json.loads(json)
    if isinstance(src_data, dict):
        for key in src_data.keys():
            if key in target_data.keys():
                compare(src_data[key], target_data[key])
            else:
                print("'{}' does not exist in target".format(key))
            
        for key in target_data.keys():
            if key not in src_data.keys():
                print("'{}' does not exist in source".format(key))
    elif isinstance(src_data, list):
        if len(src_data) != len(target_data):
            print(src_data)
        else:
            for source, target in zip(sorted(src_data), sorted(target_data)):
                compare(source, target)
    else:
        if src_data != target_data:
            print(src_data)
    
def fibonacci(n):
    if n <=2:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

def shuffle(lst):
    n = len(lst)
    for i in reversed(range(1, n)):
        j = randint(0,i)
        lst[i], lst[j]=lst[j], lst[i]
    return lst
        

if __name__ == "__main__":
    # # 1.prime number
    # start = 2
    # end = 100
    # prime_number_solution_1(start, end)
    # prime_number_solution_2(start, end)
    # prime_number_solution_3(end)

    # # 2. find number a in a string
    # element = 'a'
    # string = 'abaacccdda'
    # count_element_in_string(string, element)

    # # 3. random from [0,10000]
    # print(random_number(0, 100))

    # # 4. remove duplicate in string
    # remove_duplicate_in_string_method_1(string)
    # remove_duplicate_in_string_method_2(string)
    # remove_duplicate_in_string_method_3(string)

    # # 5. compare 2 json

    # # 7. fibonacci
    # for i in range(1,11):
    #     print(fibonacci(i))
    # print(fibonacci(2))

    # # 7. shuffle
    lst = [1,2,3,4,5]
    print(shuffle(lst))
