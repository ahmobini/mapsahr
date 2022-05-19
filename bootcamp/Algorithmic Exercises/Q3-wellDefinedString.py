#the following code is not working quite true for the first output, but that is the logic anyways.


class InputError(Exception):
	pass

def unstable(s):
    #assert '?' not in s, s
    #return s.find('11')==-1 and s.find('00')==-1
	
    assert isinstance(txt, str), 'alarm'
    if any(i not in '01?' for i in txt):
        raise InputError
    
    #not set(txt)<=set('01?')
    
    
def well_defined(s):
    lst = list(s)
    while lst:
        lastchar=lst.pop()
        if '?' == lastchar:
            #lst.append(lastchar.replace("?", '0'))
        elif    
            #lst.append(lastchar.replace("?", '1'))
        elif unstable(lastchar):
            return True
    return False

if __name__=="__main__":
    print(well_defined('1?0'))
    print(well_defined('0??10'))
    print(well_defined('???'))
    
