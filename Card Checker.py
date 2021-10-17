S = input()
def check(S): 

    S_new = S.replace(' ', '')  
    x = 0 
    i = 0

    while len(S) != 19 or  S[4] != ' ' or S[9] != ' ' or S[14] != ' ':
        return False

    if S_new.isdigit() is False:
        return False
        
    for i in range (0, len(S_new)):
        x = x + int((S_new)[i])
        i = i + 1
    if x%10 == 0:
        return True
    else:
        return False
    
   
print(check(S))


   