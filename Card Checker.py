def check(S): 

    S_new = S.replace(' ', '')                                          #This removes the spaces at index 4, index 9 and index 14 of the string
    x = 0                                                               #initialising the value of x to be used to sum the elements in the string

    while len(S) != 19 or  S[4] != ' ' or S[9] != ' ' or S[14] != ' ':  #First condition checked. This returns False if there are no spaces at index 4, index 9 or index 14 and true if the entered card number conforms to the rules.
        return False

    if S_new.isdigit() is False:                                        # Second condition to checkif the card number consists of digits
        return False
        
    for i in range (0, len(S_new)):
        x = x + int((S_new)[i])
        i = i + 1
    if x%10 == 0:                                                        #This checks if the sum of the digits is divisible by 10
        return True
    else:
        return False
    
   



   
