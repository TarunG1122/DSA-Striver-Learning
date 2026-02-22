# learning basic recursion

def learning_recursion(n):

    if n == 0:
        return

    learning_recursion(n-1)
    print(n)

learning_recursion(5)



def learning_recursion(n):

    if n == 0:
        return
    print(n)
    learning_recursion(n-1)


learning_recursion(5)