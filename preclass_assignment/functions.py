#%%
#1. write a simple function
def greet(name):
        print(f"Hello, {name}!")


#%%
# 2. If/else statements
def goldilocks(length):
        if 140<length<150:
            print("Just right :)")
        elif  length<140:
            print ("Too small!")
        else:
            print ('Too large!')
    


#%%
# 3. For loops
import numpy as np
def square_list(X):
    result=[]
 
    for i in X:
        value=np.sqrt(i) # convert the result to an integer
        result.append(value)

    print(result)  # Debug print statement
    return result # return the result instead of printing it
 
# print(result)


#%%
# 4. While loops
def fibonacci_stop(max_value):
    fib = [1, 1]
    while (n := fib[-1] + fib[-2]) <= max_value:
        fib.append(n) # append the new value to the list

    print(fib) # Debug print statement
    return fib if max_value >= 1 else []
 
#fib[-1]: This accesses the last element in the list.
#fib[-2]: This accesses the second-to-last element in the list.
# call the function where max_value = 30


#%%
# 5.Logical operators
def clean_pitch(x,state):
    clean_pitch=[]
    for i ,k in zip(x,state):
        if (i<0 or i>90 ) and k==1:
            clean_pitch.append(-999)
        else:
            clean_pitch.append(i)
    
    print(clean_pitch) # Debug print statement       
    return clean_pitch

# %%