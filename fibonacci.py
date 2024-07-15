def myFibonacci(s):
    fibonacci = [0,1]

    for x in range(2,s): 
        fibonacci.append(fibonacci[-1]+fibonacci[-2])

    print(fibonacci)
