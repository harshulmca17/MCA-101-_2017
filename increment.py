def increment(x):

   '''
    Objective        : To compute the increment of given number.
    Input Variables  :
             x  : The number inputted by user.
    Return value     : Incremented value of given number.   
    '''
    #Approach        : Return x+1
   x += 1
   return x


def sum(x,y):

    '''
    Objective        : To calculate the sum of given two numbers.
    Input Variables  :
                  x  : First number inputted by user.
                  y  : First number inputted by user.
    Return value     : Sum of given two numbers. 

    '''
    #Approach        : Use increment function to compute the sum of given two numbers.

    assert x >=0 and y >= 0

    if(y==0):
       return x

    else:

        return sum(increment(x),y-1)


def main():

    '''
    Objective       : making use of sum function
    Input Variables :
                  x : A number inputted for incrementation
                  y : A number inputted for incrementation

    '''
    #Appoach : to compute sum using incrementation and recursion

    x = int(input("Enter value of X:  "))
    y = int(input("Enter value of Y:  "))
    print("Sum of the values :  ", sum(x,y))



if __name__ == '__main__':
    main()

