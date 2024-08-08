# Palindrome을 판단하는 프로그램

def palindrome(text):
    return text == text[::-1]

str= input("Enter text: ")
if palindrome(str):
    print ("Yes, it is a palindrome")
else:
    print ("No, it is not a palindrome")
