# required exercise:
#%%
# 1. Write a simple function

# create the function
def greet(name):
    print(f"Hello, {name}!" )

# call the function
greet("World")

#%%
# 2. If/else statements
def goldilocks(size):
    if size < 140:
        print("Too small!")
    elif size > 150:
        print("Too large!")
    else:
        print("Just right. :)")
# call the function
goldilocks(139)
goldilocks(140)
goldilocks(151)
goldilocks(150)

#%%
# 3. For loops
def square_list(n):
    return [i**2 for i in n]

# call the function
print(square_list([1, 2, 3]))

#%%
# 4. While loops
def fibonacci_stop(max_value):
    fib = [1, 1]
    while (n := fib[-1] + fib[-2]) <= max_value:
        fib.append(n) # append the new value to the list
    return fib if max_value >= 1 else []

#fib[-1]: This accesses the last element in the list.
#fib[-2]: This accesses the second-to-last element in the list.
# call the function where max_value = 30
print(fibonacci_stop(30))

#%%
# 5. Logical operators
def clean_pitch(pitch,status_signals):
    return [
        -999 if (angle < 0 or angle > 90) and status_signals > 0 else angle
        for angle, status_signals in zip(pitch
        , status_signals)
    ]
x = [-1, 2, 6, 95]
status = [1, 0, 0, 0]
print(clean_pitch(x, status))



