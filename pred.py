
def increment(num):
    '''
    Objective        : To increment the value of a integer by 1
    Input Parameters :
                 num : number to be incremented by one
    Return Value     : num + 1, successor of the given number
    '''
    
    #Approach: using '+' operator to add 1 to the input number
    
    return  num + 1

def pred(num,i = 0):
    
    '''
    Objective        : To find predecessor of a given number
    Input Parameters :
                 num : number of which predecessor needs to be found
    Return Value     : Predecessor of the given number
    
    '''
    
    #Approach: using function pred() reculsively

    
    if num == 0:
        return 0
    if increment(i) == num:
        return i
    else:
        i = increment(i)
        i =  pred(num,i)

    return i


        
def main():

     num= int(input("Enter a number:  "))
            
     print("Predecessor of the number:  ",pred(num))


if __name__ == '__main__':
    main()
           
