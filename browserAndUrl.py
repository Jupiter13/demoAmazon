#! /usr/bin/python 
# section1 : Browser Page Constant
import pdb
import re

class Cons(object):
    #def __init__(self,urlValue): 
    #    
    #    global urlValue
    #    self.urlValue=urlValue 
    '''
    returns browser value and URL value
    '''


    def __init__(self,urlValue=None,browserValue=None):
        self.urlValue=urlValue
        self.browserValue=browserValue
     
    def funcConstants(self):
        print "i am in funcConstants and the urlValue and browserValue are:",self.urlValue,self.browserValue
        
        global browser
        global BP_Constants
        global url 
        
        BP_Constants=0
        browser   = ['Firefox','Chrome','Ie']
        rebrowser = ['^Firefox','^Chrome','^Ie']
        reUrl     = ['^gmail','^python','^amazon','tizag']
        url       = ['http://www.gmail.com','http://www.python.org','http://www.amazon.com','http://www.tizag.com/javascriptT/javascriptconfirm.php'] 

        for b in rebrowser:
            reExp                   =   re.compile(b)
            reExpMatch              =   re.match(reExp,self.browserValue)
            if reExpMatch          !=   None: 
                reExpValue          =   reExpMatch.group()
                print "reExpValue",     reExpValue
                global browserName
                browserName         =   reExpValue
                break
           
            

        for u in reUrl:
            reComp             = re.compile(u)
            reExpU             = re.match(reComp, self.urlValue)
            if reExpU != None:
                reExpUValue    = reExpU.group()
                if reExpUValue =='gmail':
                    global urlName
                    urlName    =url[0]
                    return browserName, urlName
                
                elif reExpUValue=='python':
                    #global urlName
                    urlName=url[1]
                    return browserName, urlName
                                                             
                elif reExpUValue=='amazon':
                    #global urlName
                    urlName=url[2]
                    return browserName, urlName
                 
                elif reExpUValue=='tizag':
                    #global urlName
                    urlName=url[3]
                    return browserName, urlName
                    
            else:
                print "add the website to the list"


if __name__== "__main__":
    man     = 'gmail'
    inst    = Cons('python','Firefox')
    print "inst",inst
    jack    = inst.funcConstants()
    print "jack", jack



'''
OP:
inst <__main__.Cons object at 0xb768d7ec>
i am in funcConstants and the urlValue and browserValue are: python Firefox
reExpValue Firefox
add the website to the list
jack ('Firefox', 'http://www.python.org')
'''















































