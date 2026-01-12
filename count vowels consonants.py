# Day-3 count vowels and consonants in  given string
# define function
def count_vowels_consonants(s):
    v_count =0
    c_count =0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            v_count +=1
        else:
            if char.isalpha():
                c_count +=1
    return v_count, c_count

print(count_vowels_consonants(s="pythONcode"))