#%%
#1. write a simple function
def greet(name):
        print(f"Hello, {name}!")
greet('world')

#%%
# 2. If/else statements
def goldilocks(length):
        if 140<length<150:
            print("Just right :)")
        if  length<140:
            print ("Too small!")
        else:
            print ('Too large!')
goldilocks (145)

#%%
# 3. For loops
def square_list(X):
    result=[]
 
    for i in X:
        value=np.sqrt(i)
        result.append(value)
 
    print(result)
square=square_list([1,4,9])

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
# 5.Logical operators
def clean_pitch(measurements, status):
    cleaned_list = []
    for i in range(len(measurements)):
        if 0 <= measurements[i] <= 90:
            cleaned_list.append(measurements[i])
        elif status[i] > 0:
            cleaned_list.append(-999)
        else:
            cleaned_list.append(measurements[i])
    return cleaned_list
measurements = [-1,2,6,95]
status = [1,0,0,0]
cleaned_measurements = clean_pitch(measurements, status)
print(cleaned_measurements)
# %%
