for i in range(1,11):
    for j in range(1,11):
        print( repr(i*j).rjust(3), end="\t")
        #repr returns the printed representation of the object.
        # rjust right justifies a string by the value you want
    print(end="\n")