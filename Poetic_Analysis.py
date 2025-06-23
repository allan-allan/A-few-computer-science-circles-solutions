#A writer is working on their newest poem, Turing and the Machines. They have hired you to determine the word which appears the most times. 
#You can access the lines of the poem by calling input() repeatedly, and the last line contains the three characters ###. All lines consist of words separated by single spaces; 
#there are no digits or punctuation. Convert all the words to lower-case, and print the word that occurs the most times (we guarantee there will not be a tie).




def most_mentioned_word():                          #define the function most_mentioned_word
    
    poem = input()                                  #input the first line of the poem
    
    while poem.endswith('###') is False:            #check if the line entered ends with '###'. If not, proceed to the While loop
        poem = poem + " " + input()                 #Concatenate the line already stored in 'poem' with the second line that is to be input 
        poem_lower_case = poem.lower()              #change the poem to lowercase
        poem_elements = poem_lower_case.split()     #split the string into a list. This loop exits when the input is '###'
        
    count=0                                         #initialise the counter at 0
    
    for i in poem_elements:                         #initialise the for loop in the string
        current_frequency = poem_elements.count(i)  #current_frequency is the count for the list index being evaluated at the moment
        if current_frequency > count:               
            count = current_frequency               
            pos = i                                 #Identifies the index where the most frequent list element is located
            
    return pos                                      #rerurns the position identified above and exits the function
print(most_mentioned_word())                        #Calls the function for execution
