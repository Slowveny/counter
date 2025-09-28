number = int(input('Enter a number: '))
counter = 0 
for i in range(1, number + 1):
    counter += i
print(f'The sum from 1 to {number} is {counter}')
