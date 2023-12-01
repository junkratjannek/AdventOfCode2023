def main(): 
    file = open ("day1\input.txt", "r")
    full_sum = 0
    for line in file: 
        datatype_list_nums = []
        datatype_list_letters = []
        for character in line: 
            if character.isnumeric(): 
                datatype_list_nums.append(character)
            else: 
                datatype_list_letters.append(character)
        
        full_sum += get_only_first_and_last_element_sum(datatype_list_nums)

    print(full_sum)

def get_only_first_and_last_element_sum(datatype_list_nums): 
    length_of_numlist = len(datatype_list_nums)
    sum_of_nums = str(datatype_list_nums[0]) + str(datatype_list_nums[length_of_numlist-1]) 
    sum_of_nums = int(sum_of_nums)
    print
    return sum_of_nums
 

if __name__ == "__main__": 
    main()