import string
def is_palindrome(s):
        s = s.lower()
        s = s.translate(None, string.punctuation)
        s = s.replace(" ", " ")
        return s == s[:: -1]

        # idx = 0
        # while idx < len(greeting)  
        # print(greetings[idx])
        # idx +=1













is_palindrome = input("Enter text: ")
if is_palindrome(is_palindrome):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
  
  
# Driver code 
s = "malayalam"
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 
