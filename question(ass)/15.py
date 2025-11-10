s = input("Enter a string: ").lower()
cleaned = ""

for ch in s:
    if ch.isalnum():
        cleaned += ch

if cleaned == cleaned[::-1]:
    print("Valid palindrome")
else:
    print("Not a palindrome")
