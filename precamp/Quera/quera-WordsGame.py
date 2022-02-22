
sentence = '"hEllO My FriEnDs!!! thIS i$s A tE%sT For your #p#r#o#b#l#e#m a'

def check_one_word(sentence):
    words = sentence.split(' ')
    specials = '~!@#$%^&*()_+|}{":?><`'
    strinj = ''
    
    for word in words:
        counter = 0
        specials_in_s = [letter for letter in word if letter in specials]
        if len(specials_in_s) < len(word)/2:
            print(strinj.join(letter for letter in word if letter not in specials), end=' ')


check_one_word(sentence)
