def lowerChar(char):
    if ord(char) >= ord('A') and ord(char)<=ord('Z'):
        return chr(ord(char)+32)
    else:
        return char
def lowerString(string):
   result=''
   for i in string:
      result=result+lowerChar(i)
   return result