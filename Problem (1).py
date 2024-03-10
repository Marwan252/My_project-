def from_Decimal_to_Binary(num):
    num = int(num)
    binary_representation = ""
    while num > 0:
        remainder = num % 2
        binary_representation = str(remainder) + binary_representation
        num = num // 2
    return f"\nBinary representation: {binary_representation}\n"

def from_Decimal_to_Octal(num):
    octal_representation = ""
    num = int(num)
    while (num > 0):
        remainder = num % 8
        octal_representation = str(remainder) + octal_representation
        num = num // 8
    return f"\nOctal representation : {octal_representation}\n"

def from_Decimal_to_Hexadecimal(num):
    Hexadecimal_representation = ""
    num = int(num)
    while num > 0:
        remainder = num % 16       
        if remainder < 10 :
            Hexadecimal_representation = str(remainder) + Hexadecimal_representation
        elif remainder == 10 :
            Hexadecimal_representation = str("A") + Hexadecimal_representation
        elif remainder == 11 :
            Hexadecimal_representation = str("B") + Hexadecimal_representation
        elif remainder == 12 :
            Hexadecimal_representation = str("C") + Hexadecimal_representation
        elif remainder == 13 :
            Hexadecimal_representation = str("D") + Hexadecimal_representation
        elif remainder == 14 :
            Hexadecimal_representation = str("E") + Hexadecimal_representation
        elif remainder == 15 :
            Hexadecimal_representation = str("F") + Hexadecimal_representation

        num = num // 16   
    return f"\nHexadecimal representation is :  {Hexadecimal_representation}\n"

def check_binary_number(binary_num): # the function to check if the user input is a binary number or not
       while int(binary_num) >0:
           if int(binary_num)%10 != 1 and int(binary_num)%10 != 0:
              return False
           binary_num = int(binary_num)//10
           if binary_num == 0:
               return str(binary_num)

def binary_to_decimal(binary_num):
    result = 0
    counter = 0
    binary_num = int(binary_num)
    while binary_num>0:
        num = binary_num%10
        added_num = num*(2**counter)
        result += added_num
        binary_num = binary_num//10
        counter += 1
    return f"\nDecimal representation : {result}\n"

def binary_to_octal(binary_num):
    result = ""
    counter = 0
    if len(binary_num)%3 == 1:
        binary_num = "00" + binary_num 
    elif len(binary_num)%3 == 2:
        binary_num = "0" + binary_num    
    while counter < len(binary_num):
        three_digits = binary_num[counter:counter+3]
        dec_of_three_digits = binary_to_decimal(int(three_digits))  
        result += str(dec_of_three_digits)
        counter += 3           
    return f"\nOctal representation : {result}\n"           

def binary_to_hexadecimal(binary_num):
    result = ""
    counter = 0
    if len(binary_num)%4 == 1:
        binary_num = "000" + binary_num 
    elif len(binary_num)%4 == 2:
        binary_num = "00" + binary_num 
    elif len(binary_num)%4 == 3:
        binary_num = "0" + binary_num        
    while counter < len(binary_num):
        four_digits = binary_num[counter:counter+4]
        dec_of_four_digits = binary_to_decimal(int(four_digits))
        if dec_of_four_digits == 10:
            dec_of_four_digits = "A" 
        if dec_of_four_digits == 11:
            dec_of_four_digits = "B" 
        if dec_of_four_digits == 12:
            dec_of_four_digits = "C" 
        if dec_of_four_digits == 13:
            dec_of_four_digits = "D" 
        if dec_of_four_digits == 14:
            dec_of_four_digits = "E"
        if dec_of_four_digits == 15:
            dec_of_four_digits = "F"                                       
        result += str(dec_of_four_digits)
        counter += 4          
    return f"\nHexadecimal representation : {result}\n"

def octal_to_decimal(octal_num):
    if set(octal_num) - set('01234567'):
        return 'Invalid input. Please enter a valid octal number.'
    decimal_num = 0
    base = 1

    while octal_num:
        digit = int(octal_num[-1])
        decimal_num += digit * base
        base *= 8
        octal_num = octal_num[:-1]

    return f"\nDecimal representation : {decimal_num}\n"

def octal_to_binary(octal_num):
    if set(octal_num) - set('01234567'):
        return 'Invalid input. Please enter a valid octal number.'
    decimal = 0
    power = 3
    for digit in str(octal_num):
        decimal += int(digit) * (8 ** power)
        power -= 1

    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2

    return f"\nBinary representation : {binary}\n"

def octal_to_hexadecimal(octal_num):
    octal_to_decimal = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7
    }
    if set(octal_num) - set('01234567'):
        return 'Invalid input. Please enter a valid octal number.'
    # Converting the octal number to decimal
    decimal_num = 0
    for digit in octal_num:
        decimal_num = decimal_num * 8 + octal_to_decimal[digit]

    decimal_to_hexadecimal = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F'
    }

# Converting the decimal number to hexadecimal
    hexadecimal_num = ''
    while decimal_num > 0:
        decimal_num, remainder = divmod(decimal_num, 16)
        hexadecimal_num = decimal_to_hexadecimal[str(remainder)] + hexadecimal_num

    return f"\nHexadecimal representation : {hexadecimal_num}\n"
    
def hex_to_decimal(hex_num):
    decimal_num = 0
    power = 0

    hex_to_decimal_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
    }

    for digit in hex_num[::-1]:
        decimal_num += hex_to_decimal_map[digit] * (16 ** power)
        power += 1

    return f"\nDecimal representation : {decimal_num}\n"

def hex_to_bin(hex_num):
    binary_num = ""
    
    for digit in hex_num:
        if digit == '0':
            binary_num += '0000'
        elif digit == '1':
            binary_num += '0001'
        elif digit == '2':
            binary_num += '0010'
        elif digit == '3':
            binary_num += '0011'
        elif digit == '4':
            binary_num += '0100'
        elif digit == '5':
            binary_num += '0101'
        elif digit == '6':
            binary_num += '0110'
        elif digit == '7':
            binary_num += '0111'
        elif digit == '8':
            binary_num += '1000'
        elif digit == '9':
            binary_num += '1001'
        elif digit == 'A':
            binary_num += '1010'
        elif digit == 'a':
            binary_num += '1010'    
        elif digit == 'B':
            binary_num += '1011'
        elif digit == 'b':
            binary_num += '1011'
        elif digit == 'C':
            binary_num += '1100'
        elif digit == 'c':
            binary_num += '1100'
        elif digit == 'D':
            binary_num += '1101'
        elif digit == 'd':
            binary_num += '1101'
        elif digit == 'E':
            binary_num += '1110'
        elif digit == 'e':
            binary_num += '1110'
        elif digit == 'F':
            binary_num += '1111'
        elif digit == 'f':
            binary_num += '1111'
    
    return f"\nBinary representation : {binary_num}\n"

def hex_to_oct(hex_num):
    hex_values = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }

    decimal_num = 0
    for digit in hex_num:
        decimal_num = decimal_num * 16 + hex_values[digit]

    octal_num = ""
    while decimal_num > 0:
        octal_num = str(decimal_num % 8) + octal_num
        decimal_num = decimal_num // 8

    return f"\nOctal representation : {octal_num}\n"

def main():
    print("** numbering system converter **")
    print("A) Insert a new number")
    print("B) Exit program")
    choice_menu1 = input("Please select an option (A/B): ").upper()
    if choice_menu1 == "B":
        exit()
    elif choice_menu1 == "A":    
        #take the num and convert a number from
        num = (input("\nPlease enter the number : "))
        print("\n** Please select the base you want to convert a number from **")
        print("A) Decimal")
        print("B) Binary")
        print("C) Octal")
        print("D) Hexadecimal")
        from_base = input("Please select an option (A/B/C/D): ").upper()
        #convert a number to
        print("\n** Please select the base you want to convert a number to **")
        print("A) Decimal")
        print("B) Binary")
        print("C) Octal")
        print("D) Hexadecimal")
        to_base = input("Please select an option (A/B/C/D): ").upper()
        if from_base not in "ABCD" or to_base not in "ABCD":
            print("\nInvalid convert choices, please select a valid choice\n")
            main()
        #convert from Decimal to Binary
        if(from_base == "A" and to_base == "B"):
            print(from_Decimal_to_Binary(num))
        elif from_base == "A" and to_base == "C":
            print(from_Decimal_to_Octal(num))
        elif from_base == "A" and to_base == "D":
            print(from_Decimal_to_Hexadecimal(num))
        elif from_base == "B" and to_base == "A" :
            if check_binary_number(num) == False:
                print('\nInvalid binary number\n')
                main()
            print(binary_to_decimal(num))
        elif from_base == "B" and to_base == "C" :
            if check_binary_number(num) == False:
                print('\nInvalid binary number\n')
                main()
            print(binary_to_octal(num))
        elif from_base == "B" and to_base == "D" :
            if check_binary_number(num) == False:
                print('\nInvalid binary number\n')
                main()
            print(binary_to_hexadecimal(num))
        elif from_base == "C" and to_base == "A" :
            print(octal_to_decimal(num))
        elif from_base == "C" and to_base == "B" :
            print(octal_to_binary(num))
        elif from_base == "C" and to_base == "D" :
            print(octal_to_hexadecimal(num))
        elif from_base == "D" and to_base == "B" :
            print(hex_to_bin(num))
        elif from_base == "D" and to_base == "A" :
            print(hex_to_decimal(num))
        elif from_base == "D" and to_base == "C" :
            print(hex_to_oct(num))
        elif from_base == to_base:
            print("\nYou have chosen the same base, it will be the same number\n")
            main()    
        main()
    else:
        print("\nPlease insert a valid choice\n")
        main()    

main()


# Abdelrhman Ahmed Abdelmonem Ahmed   20230200
# Marwan Ali Mohamed Bebars           20230384
# Karim Mohammed Abdelaziz            20231124

    


        