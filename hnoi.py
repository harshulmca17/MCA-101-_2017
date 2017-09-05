def hnoi(n, source, spare, target):

    '''
    Objective       : To print steps for tower of hnoi problem.
    Input Parameters:
                  n : no. of disks.
              source: name of the source disk
              target: name of the target disk.
               spare: name of the disk other then source and target disks.
    Output          : Steps of the solution.
    '''

    #Approach       : Using Recursion


    assert n>0

    if n==1:
        print("Move a disk from ",source, "to ", target)

    elif n == 0:
        return

    else:
        hnoi(n-1, source, target, spare)
        print("Move a disk from ",source, "to ", target)

        hnoi(n-1, spare, source, target)


hnoi(3,1,2,3)
