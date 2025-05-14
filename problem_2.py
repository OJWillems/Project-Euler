# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def main():
    previous_number = 1
    current_number = 2
    sum_of_even_numbers = 0
    while current_number < 4000000:
        # print(current_number)
        temp_current_number = current_number
        if current_number % 2 == 0:
            sum_of_even_numbers += current_number
        current_number += previous_number
        previous_number = temp_current_number
    print(sum_of_even_numbers)


if __name__ == "__main__":
    main()