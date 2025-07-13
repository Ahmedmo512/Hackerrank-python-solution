# Task: Read N commands and perform list operations like insert, append, remove, etc.
# For every 'print' command, output the current list state.


# Sample Input 0      ------------->>>>      # Sample Output 0

# 12                                         # [6, 5, 10]
# insert 0 5
# insert 1 10                                # [1, 5, 9, 10]
# insert 0 6  
# print
# remove 6                                   # [9, 5, 1]
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

if __name__ == '__main__':
   
    N = int(input())
    my_list=[]
    
    for i in range (N) :
        
        ## take first order and so on 
        request=input().strip().lower().split()
       
    ### first word represent the order (append | insert | print | sort )
        order=request[0]
        
        if order=="append":
            
            ## integer num at index 1 following the word
            integer_num =int(request[1])
            my_list.append(integer_num)
        
        elif order=="insert":
            
            ## index is index 1 & integer num is index 2
            index,integer_num=int(request[1]),int(request[2])
            my_list.insert(index,integer_num)    
       
        elif order=="remove":
            integer_num =int(request[1])
            my_list.remove(integer_num)
            
        elif order=="print":
            print(my_list)
            
        elif order=="sort":
            my_list.sort()
            
        elif order=="reverse":
            my_list.reverse()
            
        elif order=="pop":
            my_list.pop()

      
