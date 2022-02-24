def accum(s):
    counter = 0
    output = ""
    for letter in s:
        output += letter.upper() + letter.lower() * counter + '-'
        counter += 1
    return output[:-1]

print(accum(s='ZpglnRxqenU'))