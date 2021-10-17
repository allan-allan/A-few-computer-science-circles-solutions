#You have been hired by MeisterCard to write a function which checks if a given credit card number is valid. Your function check(S) should take a string S as input. 
#First, if the string does not follow the format "#### #### #### ####" where each # is a digit, then it should return False. 
#Then, if the sum of the digits is divisible by 10 (a "checksum" method), then the procedure should return True, else it should return False. 
#For example, if S is the string "9384 3495 3297 0123" then although the format is correct, the digit sum is 72 so you should return False


def check(S): 

    S_new = S.replace(' ', '')                                          #This removes the spaces at index 4, index 9 and index 14 of the string
    x = 0                                                               #initialising the value of x to be used to sum the elements in the string

    while len(S) != 19 or  S[4] != ' ' or S[9] != ' ' or S[14] != ' ':  #First condition checked. This returns False if there are no spaces at index 4, 
        return False                                                    #index 9 or index 14 and true if the entered card number conforms to the rules.

    if S_new.isdigit() is False:                                        # Second condition to checkif the card number consists of digits
        return False
        
    for i in range (0, len(S_new)):
        x = x + int((S_new)[i])
        i = i + 1
    if x%10 == 0:                                                        #This checks if the sum of the digits is divisible by 10
        return True
    else:
        return False
    
   



   
