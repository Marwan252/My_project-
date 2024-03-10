def binary_addition(binary_num1, binary_num2): # the function to the sum of two binary numbers
    if len(binary_num1) > len(binary_num2):
        for x in range(len(binary_num1)-len(binary_num2)):
            binary_num2 = str(0*x) + binary_num2
    elif len(binary_num1) < len(binary_num2):
        for x in range(len(binary_num2)-len(binary_num1)):
            binary_num1 = str(0*x) + binary_num1      
    binary_num1 = binary_num1[::-1]
    binary_num2 = binary_num2[::-1]         
    result = ""
    carry = 0
    for x in range(len(binary_num1)):
        if binary_num1[x] == "0" and binary_num2[x] == "0" and carry == 0:
            result += "0"
        elif binary_num1[x] == "0" and binary_num2[x] == "0" and carry == 1:
            result += "1" 
            carry = 0
        elif binary_num1[x] == "1" and binary_num2[x] == "0" and carry == 0:
            result += "1"       
        elif binary_num1[x] == "0" and binary_num2[x] == "1" and carry == 0:
            result += "1"
        elif binary_num1[x] == "1" and binary_num2[x] == "0" and carry == 1:
            result += "0"   
            carry = 1
        elif binary_num1[x] == "0" and binary_num2[x] == "1" and carry == 1:
            result += "0"   
            carry = 1         
        elif binary_num1[x] == "1" and binary_num2[x] == "1" and carry == 0:
            result += "0"   
            carry = 1    
        elif binary_num1[x] == "1" and binary_num2[x] == "1" and carry == 1:
            result += "1"   
            carry = 1    
    if carry == 1:
        result += "1"
        carry = 0        
    return result[::-1]  

def binary_subtraction(binary_num1,binary_num2):  # the function to calculate the subtraction of two binary numbers
    if int(binary_num2) > int(binary_num1):
        temp = binary_num1
        binary_num1 = binary_num2
        binary_num2 = temp
    if len(binary_num1) > len(binary_num2):
        for x in range(len(binary_num1)-len(binary_num2)):
            binary_num2 = str(0*x) + binary_num2
    elif len(binary_num1) < len(binary_num2):
        for x in range(len(binary_num2)-len(binary_num1)):
            binary_num1 = str(0*x) + binary_num1      
    binary_num1 = binary_num1[::-1]
    binary_num2 = binary_num2[::-1]         
    result = ""
    carry = 0
    for x in range(len(binary_num1)):
        if binary_num1[x] == "0" and binary_num2[x] == "0" and carry == 0:
            result += "0"
        elif binary_num1[x] == "1" and binary_num2[x] == "0" and carry == 0:
            result += "1" 
        elif binary_num1[x] == "1" and binary_num2[x] == "1" and carry == 0:
            result += "0"       
        elif binary_num1[x] == "0" and binary_num2[x] == "1" and carry == 0:
            result += "1"
            carry = -1
        elif binary_num1[x] == "1" and binary_num2[x] == "0" and carry == -1:
            result += "0"   
            carry = 0
        elif binary_num1[x] == "1" and binary_num2[x] == "1" and carry == -1:
            result += "1"   
            carry = -1
        elif binary_num1[x] == "0" and binary_num2[x] == "1" and carry == -1:
            result += "0"   
            carry = -1
        elif binary_num1[x] == "0" and binary_num2[x] == "0" and carry == -1:
            result += "1"   
            carry = -1          
    return str(int(result[::-1]))     
         
def insert_first_number():   # inserting the first binary number 
    binary_num1 = input("\nPlease insert a binary number: ")
    cheching_binary = check_binary_number(binary_num1)
    while cheching_binary == False:
        print("\nPlease insert a valid binary number: ")
        binary_num1 = input("\nPlease insert a binary number: ")
        cheching_binary = check_binary_number(binary_num1)
    menu_2(binary_num1)    
    return binary_num1      
     
def insert_second_number():   # inserting the second binary number 
    binary_num2 = input("\nPlease insert a second binary number: ")
    cheching_binary = check_binary_number(binary_num2)
    while cheching_binary == False:
        print("\nPlease insert a valid binary number: ")
        binary_num2 = input("\nPlease insert a second binary number: ")
        cheching_binary = check_binary_number(binary_num2)  
    return binary_num2            
         
def check_binary_number(binary_num): # the function to check if the user input is a binary number or not
       while int(binary_num) >0:
           if int(binary_num)%10 != 1 and int(binary_num)%10 != 0:
              return False
           binary_num = int(binary_num)//10
           if binary_num == 0:
               return str(binary_num)
            
def one_complement(binary_num):  # the function to get the one's complement of a binary number
    binary_num = list(binary_num)
    if binary_num[0] == "0":
        return ''.join(binary_num)
    else:
        for i in range(len(binary_num)):
            if binary_num[i] == '0':
                binary_num[i] = '1'
            elif binary_num[i] == '1':
                binary_num[i] = '0'
        one_complement = ''.join(binary_num)
        return one_complement

def two_complement(num):   # the function to get the two's complement of a binary number
    num = list(num)
    if num[0] == "0":
        return ''.join(num)
    else:
        for i in range(len(num)):
            if num[i] == '0':
                num[i] = '1'
            elif num[i] == '1':
                num[i] = '0'
        ones_comp = ''.join(num)
        result = ''
        carry = 1
        for bit in reversed(ones_comp):
            if carry == 1:
                sum_bit = (int(bit) + carry) % 2
                carry = (int(bit) + carry) // 2
                result = str(sum_bit) + result
            else:
                result = bit + result
        return result
               
def menu_1():   # the first menu of the program
    print("** binary calculator **")
    print("A) Insert new numbers")
    print("B) Exit")
    menu1_choice = input(">>> ").upper()
    if menu1_choice == "B":
        exit()
    elif menu1_choice == "A":
        insert_first_number()
    else:
        print("\nPlease insert a valid selection\n")
        menu_1()   
 
def menu_2(binary_num1):  # the second menu of the program
    print("\n** Please select the operation **")
    print("A) Compute one's complement")
    print("B) Compute two's complement")
    print("C) Addition")
    print("D) Subtraction")
    menu_2_choice = input(">>> ").upper()
    if menu_2_choice == "C": # calling the function binary_addition() 
       binary_num2 = insert_second_number()
       print(f'\nThe result of addition is {binary_addition(binary_num1,binary_num2)}\n')
       menu_1()
    elif menu_2_choice == "A":  # calling the function one_complement() 
        print(f'\nThe one complement is {one_complement(binary_num1)}\n')
        menu_1()
    elif menu_2_choice == "B":  # calling the function two_complement() 
        print(f'\nThe two complement is {two_complement(binary_num1)}\n')
        menu_1()        
    elif menu_2_choice == "D":  # calling the function binary_subtraction() 
       binary_num2 = insert_second_number() 
       print(f'\nThe result of subtraction is {binary_subtraction(binary_num1,binary_num2)}\n') 
       menu_1()       
    else:
        print("\nPlease insert a valid selection")
        menu_2(binary_num1)
               
menu_1()  # running the program


# Abdelrhman Ahmed Abdelmonem Ahmed 20230200
# Marwan Ali Mohamed Bebars         20230384
# Karim Mohammed Abdelaziz          20231124