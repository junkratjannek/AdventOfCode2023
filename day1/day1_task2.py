def main(): 
    file = open ("day1\input.txt", "r")
    digits_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, 1:1 , 2:2 , 3:3 , 4:4, 5:5 , 6:6, 7:7, 8:8, 9:9}
    full_sum = 0
    for line in file:
        datatype_list_nums = []
        for element in digits_dict: 
            if element in line:   
                datatype_list_nums.append(digits_dict[element]) 
        full_sum += get_only_first_and_last_element_sum(datatype_list_nums)

    print(full_sum)

def get_only_first_and_last_element_sum(datatype_list_nums): 
    length_of_numlist = len(datatype_list_nums)
    sum_of_nums = str(datatype_list_nums[0]) + str(datatype_list_nums[length_of_numlist-1]) 
    sum_of_nums = int(sum_of_nums)
    return sum_of_nums


string = "seven331fivekfrqbd"
summe = 0
datatype_list_nums = []
digits_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "1":1 , "2":2 , "3":3 , "4":4, "5":5 , "6":6, "7":7, "8":8, "9":9}
for element in digits_dict: 
    if element in string:   
        datatype_list_nums.append(digits_dict[element]) 

print(datatype_list_nums) 

# summe += get_only_first_and_last_element_sum(datatype_list_nums)
# print(summe) 


# if __name__ == "__main__": 
#     main()