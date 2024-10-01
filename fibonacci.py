def is_fibonacci(number):
    # Generate the Fibonacci sequence until the number is greater than or equal to the input
    fibonacci = [0, 1]
    index = 1
    while fibonacci[index] < number:
        fibonacci.append(fibonacci[index - 1] + fibonacci[index])
        index += 1
    # Check if the input number is in the Fibonacci sequence
    return number in fibonacci

while True:
    try:
        # Prompt the user for input and ensure it's a positive integer
        num = int(input("Please give me a number: "))

        if num < 0:
            print('Please enter a positive number.')
        else:
            break
    except ValueError:
        print('Invalid input. Please enter a valid integer.')

# Check if the number is part of the Fibonacci sequence
if is_fibonacci(num):
    print("It's a Fibonacci number")
else:
    print("It's not a Fibonacci number")
