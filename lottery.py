def get_next(numbers, prompt):
    next = raw_input(prompt.format(*numbers)) 
    if (valid_number(numbers, next)):
        return next 
    while (not valid_number(numbers, next)): 
        print("Please try again")
        next = raw_input(prompt.format(*numbers)) 
        if (valid_number(numbers, next)):
            return next

def valid_number(numbers, next):
    try:
        x = int(next) 
        if (x < 1 or x > 69):
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

if __name__ == "__main__":
    first = get_name("Enter your first name: ") 
    last = get_name("Enter your last name: ") 
    numbers = [] 

    numbers.append(get_next(numbers, "select 1st # (1 thru 69): ")) 
    numbers.append(get_next(numbers, "select 2nd # (1 thru 69 excluding {0}): ")) 
    numbers.append(get_next(numbers, "select 3rd # (1 thru 69 excluding {0} and {1}): ")) 
    numbers.append(get_next(numbers, "select 4th # (1 thru 69 excluding {0}, {1} and {2}): ")) 
    numbers.append(get_next(numbers, "select 5th # (1 thru 69 excluding {0}, {1}, {2} and {3}): ")) 
    print(numbers) 

