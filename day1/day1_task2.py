def get_only_first_and_last_element_sum(datatype_list_nums): 
    sum_of_nums = str(datatype_list_nums[0]) + str(datatype_list_nums[-1]) 
    sum_of_nums = int(sum_of_nums)
    return sum_of_nums

def main():
    file = open("day1/input.txt", "r")
    full_sum = 0
    for element in file:
        datatype_list_nums = []
        length_of_string = len(element) 
        for i in range (0, length_of_string):
            try:  
                if element[i] == "o": 
                    if element[i+1] == "n": 
                        if element[i+2] == "e": 
                            datatype_list_nums.append(1)  
                            i += 2
                        i += 1 
                elif element[i] == "t": 
                    if element[i+1] == "w": 
                        if element[i+2] == "o": 
                            datatype_list_nums.append(2) 
                            i += 2
                        i += 1 
                    elif element[i+1] =="h": 
                        if element[i+2] == "r": 
                            if element[i+3] =="e": 
                                if element[i+4] == "e": 
                                    datatype_list_nums.append(3) 
                                    i += 4
                                i += 3
                            i += 2
                        i += 1        
                elif element[i] == "f": 
                    if element[i+1] == "o": 
                        if element[i+2] == "u": 
                            if element[i+3] == "r": 
                                datatype_list_nums.append(4) 
                                i += 3
                            i += 2
                        i += 1
                    if element[i+1] == "i": 
                        if element[i+2] == "v": 
                            if element[i+3] == "e": 
                                datatype_list_nums.append(5) 
                                i += 3 
                elif element[i] == "s": 
                    if element[i+1] == "i": 
                        if element[i+2] == "x": 
                            datatype_list_nums.append(6) 
                            i += 2
                        i += 1  
                    if element[i+1] == "e": 
                        if element[i+2] == "v": 
                            if element[i+3] == "e": 
                                if element[i+4] == "n": 
                                    datatype_list_nums.append(7) 
                                    i += 4 
                elif element[i] == "e": 
                    if element[i+1] == "i": 
                        if element[i+2] == "g": 
                            if element[i+3] == "h": 
                                if element[i+4] == "t": 
                                    datatype_list_nums.append(8) 
                                    i += 4         
                elif element[i] == "n": 
                    if element[i+1] == "i": 
                        if element[i+2] == "n": 
                            if element[i+3] == "e": 
                                datatype_list_nums.append(9)
                                i += 4 
                                
                elif element[i].isnumeric(): 
                    datatype_list_nums.append(int(element[i]))
            except: 
                pass   
        
        full_sum += get_only_first_and_last_element_sum(datatype_list_nums)
        
    print(full_sum) 
                
if __name__ == "__main__": 
    main()