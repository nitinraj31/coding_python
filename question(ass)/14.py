s = input("Enter a string: ")
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for k, v in freq.items():
    print(f"{k} : {v}")
