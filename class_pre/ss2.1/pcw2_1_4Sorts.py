import math
import time # for runtime calculation
import matplotlib.pyplot as plt  # for plotting

# add a global counter for question 5 and 6

def merge(A,p,q,r):
    global count
    #part 1
    n_1 = q-p+1
    count += 1
    n_2 = r-q
    count += 1
    # initialize L and R
    L = list(range(n_1+1))
    count += 1
    R = list(range(n_2+1))
    count += 1
    #assign A elements to L and R
    for i in range(n_1):   # 0,1,...n_1
        L[i] = A[p+i-1]
        count += 1
    for j in range(n_2):
        R[j] = A[q+j]
        count += 1
    # assign last element to infinity
    L[n_1] = math.inf
    count += 1
    R[n_2] = math.inf
    count += 1

    #part 2
    i = 0
    count += 1
    j = 0
    count += 1
    for k in range(p-1, r):
        if L[i] <= R[j]:
            count += 1
            A[k] = L[i]
            count += 1
            i += 1
            count += 1
        else:
            A[k] = R[j]
            count += 1
            j += 1
            count += 1

    return A
    # YOUR CODE HERE
    raise NotImplementedError()

def merge_sort(A,p,r):
    global count
    if p < r:
        count += 1
        q = int((p+r)/2)  # must be floor int number for proper indexing
        count += 1
        merge_sort(A,p,q)
        count += 1
        merge_sort(A,q+1,r)
        count += 1
        merge(A,p,q,r)
        count += 1
    return A   # updates A

    raise NotImplementedError()

def get_MergeSort_data():
    n_list = []  # list of input size, n = 100*k
    steps_list = [] # list of step for each k
    runTime_list = [] # list of running time for each k
    global count  # must initiate again!

    for k in range(1,15):

        count = 0
        list_k = [i for i in range(100*k, 0, -1)]
        p = 1
        r = len(list_k)
        n_list.append(r)

        start_time = time.clock()
        merge_sort(list_k,p,r)
        runTime = time.clock()-start_time
        runTime_list.append(runTime)

        steps_list.append(count)

    return n_list,steps_list,runTime_list

    raise NotImplementedError()


#insertion sort on counter
def insertionSort(A):
    # introduce global counter variable
    global count
    count = 0

    for j in range(1,len(A)):
        key = A[j]
        count += 1
        i= j-1
        count += 1
        while i >= 0 and A[i]>key:
            count += 1  # count step for while statement evaluation
            A[i+1] = A[i]
            count += 1
            i -= 1
            count += 1
        A[i+1] = key
        count += 1

    return A
    raise NotImplementedError()

def get_InsertionSort_data():
    n_list = []  # list of input size, n = 100*k
    steps_list = [] # list of step for each k
    runTime_list = [] # list of running time for each k
    global count

    for k in range(1,15):

        count = 0
        list_k = [i for i in range(100*k, 0, -1)]
        p = 1
        r = len(list_k)
        n_list.append(r)

        start_time = time.clock()
        insertionSort(list_k)
        runTime = time.clock()-start_time
        runTime_list.append(runTime)

        steps_list.append(count)

    return n_list,steps_list,runTime_list

    raise NotImplementedError()

def bubbleSort(A):
    global count
    count = 0
    b = 0 # initialize a bin variable for temporary keeping of swapped item
    count += 1
    n = len(A) #length of list items
    count += 1
    for i in range(n-1):  # i from 0 to n-1
        count += 1
        for j in range(n-1,i,-1): # j from n-1 to 1(for first round)
            count += 1
            if A[j]< A[j-1]:
                count += 1
                b = A[j-1]
                count += 1
                A[j-1] = A[j]
                count += 1
                A[j] = b   # three-step swap
                count += 1
    return A
    raise NotImplementedError()

def get_BubbleSort_data():
    n_list = []  # list of input size, n = 100*k
    steps_list = [] # list of step for each k
    runTime_list = [] # list of running time for each k
    global count

    for k in range(1,15):

        count = 0

        list_k = [i for i in range(100*k, 0, -1)]
        p = 1
        r = len(list_k)
        n_list.append(r)

        start_time = time.clock()
        bubbleSort(list_k)
        runTime = time.clock()-start_time
        runTime_list.append(runTime)

        steps_list.append(count)

    return n_list,steps_list,runTime_list

    raise NotImplementedError()

#selectionSort on counter
def selectionSort(A):
    global count
    count = 0

    b = 0 # initialize a b as temporary item holder during swapping
    count += 1
    n = len(A)
    count += 1
    for i in range(n-1):  # i in 0 to n-1
        count += 1
        min_idx = i  # index of default minimal
        count += 1
        for j in range(i+1,n):   # j in i+1 to n
            count += 1
            if A[j] < A[min_idx]:
                count += 1
                min_idx = j     #update minimal index
                count += 1
            # swap A[i] with A[min_idx]
            b = A[min_idx]
            count += 1
            A[min_idx] = A[i]
            count += 1
            A[i] = b   # three-step swap
            count += 1
    return A
    raise NotImplementedError()

def get_SelectionSort_data():
    n_list = []  # list of input size, n = 100*k
    steps_list = [] # list of step for each k
    runTime_list = [] # list of running time for each k
    global count

    for k in range(1,15):

        count = 0

        list_k = [i for i in range(100*k, 0, -1)]
        p = 1
        r = len(list_k)
        n_list.append(r)

        start_time = time.clock()
        selectionSort(list_k)
        runTime = time.clock()-start_time
        runTime_list.append(runTime)

        steps_list.append(count)

    return n_list,steps_list,runTime_list

    raise NotImplementedError()


### combining four sorts

M = get_MergeSort_data()
I = get_InsertionSort_data()
B = get_BubbleSort_data()
S = get_SelectionSort_data()

#
# ## First: steps comparison
# M_steps = M[1]
# I_steps = I[1]
# B_steps = B[1]
# S_steps = S[1]
#
# x = M[0]  # input size the same
#
# x_M = x
# y_M = M_steps
# plt.plot(x_M,y_M, label = "MergeS_step")
#
# x_I = x
# y_I = I_steps
# plt.plot(x_I,y_I, label = "InsertionS_step")
#
# x_B = x
# y_B = B_steps
# plt.plot(x_B,y_B, label = "BubbleS_step")
#
# x_S = x
# y_S = S_steps
# plt.plot(x_S,y_S, label = "SelectionS_step")
#
#
# # naming the x axis
# plt.xlabel('input size (n)')
# # naming the y axis
# plt.ylabel('number of steps')
# # giving a title to my graph
# plt.title('Growth of steps comparison')
#
# # show a legend on the plot
# plt.legend()
#
# # function to show the plot
# plt.show()


## Second: runTime comparison

M_runTime = M[2]
I_runTime = I[2]
B_runTime = B[2]
S_runTime = S[2]

x = M[0]  # input size the same

x_M = x
y_M = M_runTime
plt.plot(x_M,y_M, label = "MergeS_runTime")

x_I = x
y_I = I_runTime
plt.plot(x_I,y_I, label = "InsertionS_runTime")

x_B = x
y_B = B_runTime
plt.plot(x_B,y_B, label = "BubbleS_runTime")

x_S = x
y_S = S_runTime
plt.plot(x_S,y_S, label = "SelectionS_runTime")


# naming the x axis
plt.xlabel('input size (n)')
# naming the y axis
plt.ylabel('running time (s)')
# giving a title to my graph
plt.title('Growth of running time comparison')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
