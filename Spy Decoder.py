
raw_statement = input()                                                             #The input text to be decoded

def encoder():                                                                      #The encoding function, to be called later, values are defined in the first few lines
    shift_value = -6                                                                #The hard value by which the letters are shifted.
    decoded_str = ''                                                                #The new string with encoded values
    letters_in_alphabet = 26                                                        #Number of letters in the alphabet, to be used later
    order_for_space = 32                                                            #ASCII value for a space charachter               
    for i in range(0,len(raw_statement)):                                           #Loop to test the shifted value.
        str_index = raw_statement [i]
        ordered_index = ord(str_index)
        ordered_index = ordered_index + shift_value
        
        if ordered_index == 37:                                                     #Ensures that spaces in the input are maintained
            decoded_str = chr(order_for_space) + decoded_str

        elif ordered_index >= 65 and ordered_index <=90:                            #Ensures that letters between A and Z after conversion are properly handled as letters and not symbols
            decoded_str = chr(ordered_index) + decoded_str
            
        elif ordered_index < 65:                                                    #Ensures proper handling of converted letters that are greater than Z such that they loop back to A
            ordered_index = (ordered_index + letters_in_alphabet )
            decoded_str = chr(ordered_index) + decoded_str          
                       
        
    decoded_str_reversed = decoded_str[len(decoded_str)::-1]                         #Reverses the contents of the generated string
           
    return decoded_str_reversed                                                      #Ends the function definition
print(encoder())                                                                     #The function is called here
