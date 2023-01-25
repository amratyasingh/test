def target_sum_tuple(lst, target):
    lt = []
    for i in range(len(lst)-1):
        for j in range(i+1, len(list_of_integer)):
            if i + j == target:
                lt.extend([i,j])
                return tuple(lt)
    
    return "No Possible Tuple"
        
list_of_integer = list(map(int, input("Enter the list seperated by space : ").split()))
target_number = int(input("Enter the target number : "))
print(target_sum_tuple(list_of_integer, target_number))