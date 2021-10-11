#Instruction
# You are given a string and your task is to swap cases. 
# In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    x = ""
    for char in s:
        if char.isupper() == True:
            x+=(char.lower())
        else:
            x+=(char.upper())
    return x
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
