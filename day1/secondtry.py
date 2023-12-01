string = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
string = string.split("\n") 

digits_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "1":1 , "2":2 , "3":3 , "4":4, "5":5 , "6":6, "7":7, "8":8, "9":9}
digits_dict2 = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
full_sum = 0

for line in string: 
    datatype_list_nums = []
    
    for key, value in digits_dict.items():
        if line.startswith(key):
            print(key, value)
    
    
    # for element in digits_dict2: 
    #     if element in line: 
    #         datatype_list_nums.append(digits_dict2[element])
    # # for character in line: 
    # #     if character.isnumeric(): 
    # #         datatype_list_nums.append(character)
    # # Analyse ob Zahl des ersten Strings ist vorbei
    # print(datatype_list_nums)
    # break           