def my_function(arg1, arg2=10, arg3=None):
    if arg3 is None:
        print(arg1 + arg2)
    else:
        print(arg1 * arg2 * arg3)
        my_function(5)
        my_function(5, 2)
        my_function(5, 2, 3)


def strings_by_length(strings):
    return [s for s in strings if len(s) >= 5]
input_list = ["apple", "cat", "banana", "dog", "orange"]
output_list = strings_by_length(input_list)
print(output_list)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
prime_numbers = list(filter(is_prime, numbers))
print("Prime numbers:", prime_numbers)
string_list = ["hello", "hi", "simi", "sujith"]
uppercase_list = list(map(str.upper, string_list))
print(uppercase_list)
