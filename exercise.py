def sum_with_while(start, end):
    """
    Calculate the sum of all numbers between start and end (inclusive) using a while loop.
    """
    list_middle = [index for index in range(start, (end + 1))]
    
    sum_all = 0
    running_sum = 0
    for j in range((start - 1),(end)):
        while j < len(list_middle):
            next_i = list_middle.index(j + 1)
            running_sum += list_middle[next_i]
            break
        
    sum_all = running_sum
    return sum_all
        
        

def count_vowels_in_string(input_string):
    """
    Count the number of vowels in a given string using a for loop.
    """
    vowels = ['a','e','i','o','u']
    count = 0
    
    for char in vowels:
        for j in input_string:
            if char == j.lower():
                count += 1
    
    return count
        

def filter_numbers(numbers):
    """
    Filter a list of numbers based on specific conditions using a for loop and conditionals.
    """
    pos_list = []
    even_list = []
    odd_list = []
    neg_list = []
    
    storage = {}
    
    for n in numbers:
        if n % 2 == 0 or n == 0:
            even_list.append(n)
        if n % 2 != 0:
            odd_list.append(n)
        if n < 0:
            neg_list.append(n)
        if n > 0:
            pos_list.append(n)
            
    storage['positive'] = pos_list
    storage['negative'] = neg_list
    storage['even'] = even_list
    storage['odd'] = odd_list
    
    print(storage)
    return storage

def fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms using a while loop.
    """
    
    fibo_list = []
    a,b = 0,1
    count = 0
    
    while count < n:
        fibo_list.append(a)
        a,b = b, a + b
        count += 1
        
    return fibo_list
    
    

def pascals_triangle(rows):
    """
    Generate Pascal's Triangle up to a given number of rows.
    """
    triangle = [1]
    start_end = 1
    storage = []

    middle_num = 0
    
    for row in range(rows):
        if row == 0:
            middle_num += start_end
            storage.append(start_end)
            print(storage)
            storage.append(middle_num)
            print(storage)
            triangle.append(storage)

        else:
            for index in range(rows):
                middle_num = triangle[-1][index - 1] + triangle[-1][index + 1]
                storage.append(start_end)
                storage.append(middle_num)
                storage.append(start_end)

        
    print(triangle)
    return triangle




def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi problem recursively.
    """
    pass

def find_dna_sequence(dna, sequence):
    """
    Find the first occurrence of a DNA subsequence within a larger DNA string.
    """
    pass

def is_palindrome(input_string):
    """
    Check if a given string is a palindrome (ignoring spaces, capitalization, and punctuation).
    """
    # empty_1 = []
    # empty_2 = []

    # input_string = "A man, a plan, a canal, Panama"
    # input_string_formatted = input_string.lower()
    # print(input_string_formatted[::-1])
    # print(input_string_formatted)
    
    # for char in len(list(input_string_formatted)):
    #     if not input_string_formatted[char].isalpha():
    #         print(input_string_formatted[char])
            
        # empty_1.remove('')

    # for char in input_string_formatted[::-1]:
    #     empty_2.append(char)

    
    # print(empty_2)


    # if empty_1 == empty_2:
    #     return True
    # else:
    #     return False


def generate_permutations(input_string):
    """
    Return all possible permutations of a given string.
    """
    pass

def is_valid_sudoku(board):
    """
    Validate a given 9x9 Sudoku board.
    """
    pass

def solve_n_queens(n):
    """
    Find all possible solutions to the N-Queens problem.
    """
    pass

def longest_common_subsequence(str1, str2):
    """
    Find the length of the longest subsequence common to both strings.
    """
    pass

if __name__ == "__main__":
    # print("Testing sum_with_while:")
    # sum_ans = sum_with_while(-3, 3)
    # print(f"Sum: {sum_ans}\n")
    
    # print("\nTesting count_vowels_in_a_string:")
    # vowel_count = count_vowels_in_string('HELLO')
    # print(f"Vowel count: {vowel_count}")
    
    # print("\nTesting filter_numbers:")
    # filtered = filter_numbers([1,-1,2,-2,0])
    # print(f"Filtered: {filtered}")
    
    print("\nTesting fibonacci_sequence:")
    fibo = fibonacci_sequence(5)
    print(f"Fibonacci: {fibo}")

    # print("\nTesting is_palindrome:")
    # pali = is_palindrome("A man, a plan, a canal, Panama")
    # print(f"Palindrome: {pali}")
    
    print("\nTesting pascals_triangle:")
    rows_num = pascals_triangle(3)
    print(f"Pascal's triangle: {rows_num}")