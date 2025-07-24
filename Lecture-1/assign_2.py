def find_sum_pair(my_list:list,number:int):
    for index,n in enumerate(my_list):
        if (my_list[index] + my_list[index+1]) == number:
            return my_list[index], my_list[index+1]
            
def main():
    my_list = list(map(int, input("Enter Number (space-separate): ").strip().split()))
    number = int(input("What's Number you need to find sum : "))
    total = find_sum_pair(my_list, number)
    print(total)

if __name__ == "__main__":
    main()