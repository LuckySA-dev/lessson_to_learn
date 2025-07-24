def find_sum_pair(my_list:list,sum:int):
    if my_list is None or len(my_list) < 2:
        return []
    
    if sum < 1:
        raise ValueError("Error sum values must be more then 0!")
    
    for index,n in enumerate(my_list):
        if (my_list[index] + my_list[index+1]) == sum:
            return my_list[index], my_list[index+1]
        else:
            return []
            
def main():
    my_list = list(map(int, input("Enter Number (space-separate): ").strip().split()))
    sum = int(input("What's Number you need to find sum : "))
    total = find_sum_pair(my_list, sum)
    print(total)

if __name__ == "__main__":
    main()