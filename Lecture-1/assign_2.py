user_input = input("Enter Number (space-separate): ").strip().split()
my_list = [int(x) for x in user_input]
number = int(input("What's Number you need to find sum : "))

for index,n in enumerate(my_list):
    if (my_list[index] + my_list[index+1]) == number:
        print(my_list[index], my_list[index+1])
        break

