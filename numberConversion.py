 # ---***---***--- NUMBER CONVERSION ---***---***---

# -----Decimal-Binary ---------
a = 59
bin_a = bin(a) #Decimal to binary
dec_a = int(bin_a, 2) # Binary to decimal

print(bin_a)
print(dec_a)

# ------ Decimal - Octal -------
oct_a = oct(a)
dec_a2 = int(oct_a, 8)# Octal to decimal

print(oct_a)
print(dec_a2) 

# ------ Decimal - Hexadecimal -------
hex_a = hex(a)
dec_a3 = int(hex_a, 16)

print(hex_a)
print(dec_a3)

# ------ Unicode to Character -------
print(chr(82), chr(105), chr(97), chr(110), chr(97))

# ------ Character TO Unicode -------
print(ord('R'), ord('i'), ord('a'), ord('n'), ord('a'))