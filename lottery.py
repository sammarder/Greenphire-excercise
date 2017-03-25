import random

def get_next(numbers, prompt, max):
    next = raw_input(prompt.format(*numbers)) 
    if (valid_number(numbers, next, max)):
        return next 
    while (not valid_number(numbers, next, max)): 
        print("Please try again")
        next = raw_input(prompt.format(*numbers)) 
        if (valid_number(numbers, next, max)):
            return next

def valid_number(numbers, next, max):
    try:
        x = int(next) 
        if (x < 1 or x > max):
            return False 
        if (next in numbers):
            return False 
        return True
    except ValueError:
        return False

def get_name(prompt):
    name = raw_input(prompt)
    if (len(name) > 0):
        return name
    while (len(name) == 0):
        print("Please enter a non empty string")
        name = raw_input(prompt)
        if (len(name) > 0):
            return name

def generate():
    set = [str(x + 1) for x in range(69)]
    winningNums = random.sample(set, 5)
    powerballs = [x + 1 for x in range(26)]
    powerBall = random.choice(powerballs)
    return " ".join(winningNums) + " Powerball: " + str(powerBall) 

if __name__ == "__main__":
    first = get_name("Enter your first name: ") 
    last = get_name("Enter your last name: ") 
    numbers = [] 

    numbers.append(get_next(numbers, "select 1st # (1 thru 69): ", 69))
    numbers.append(get_next(numbers, "select 2nd # (1 thru 69 excluding {0}): ", 69))
    numbers.append(get_next(numbers, "select 3rd # (1 thru 69 excluding {0} and {1}): ", 69))
    numbers.append(get_next(numbers, "select 4th # (1 thru 69 excluding {0}, {1} and {2}): ", 69))
    numbers.append(get_next(numbers, "select 5th # (1 thru 69 excluding {0}, {1}, {2} and {3}): ", 69))
    powerball = get_next([], "select Power Ball # (1 thru 26): ", 26) 
    
    result = first + " " + last + " {0}, {1}, {2}, {3}, {4} Powerball: ".format(*numbers) + str(powerball) + "\n"

    output = open("lotto.txt", "a")
    input = open("lotto.txt", "r")
    for line in input:
        print(line.strip())
    input.close()
    
    output.write(result)
    output.close()
    print(result.strip())

    win = generate()
    print("\n" + win)
