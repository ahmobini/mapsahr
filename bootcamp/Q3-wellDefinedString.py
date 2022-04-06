#the following code is not working quite true for the first output, but that is the logic anyways.

def unstable(s):
    assert '?' not in s, s
    return s.find('11')==-1 and s.find('00')==-1

def well_defined(s):
    lst = list(s)
    while lst:
        finalindex=lst.pop()
        if '?' in finalindex:
            lst.append(finalindex.replace("?", '0'))
            lst.append(finalindex.replace("?", '1'))
        elif unstable(finalindex):
            return True
    return False

if __name__=="__main__":
    print(well_defined('1?0'))
    print(well_defined('0??10'))
    print(well_defined('???'))
