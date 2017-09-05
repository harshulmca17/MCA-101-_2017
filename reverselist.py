def reverse(list1,list2=[]):
    '''
    objective: to return reversed list
    input    : list
    return   : reversed list
    approach : '''
    length=len(list1)
    if list1==[]:
        return list2
    else:
        list2.append(list1[length-1])
        return (reverse(list1[0:length-1]))
def main():
    list1=[1,2,3,4]
    print('initial list is',list1)
    print('reverse is',reverse(list1))
if __name__ == '__main__':
    main()
