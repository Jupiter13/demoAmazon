import unittest
from   selenium                                      import  webdriver
from   selenium.webdriver.support.wait               import  WebDriverWait 
from   selenium.webdriver.support.select             import  Select
from   selenium.webdriver.support                    import  expected_conditions as EC 
from   selenium.webdriver.common.action_chains       import  ActionChains
from   selenium.webdriver.common.by                  import  By 
from   genrics.browserAndUrl                         import  Cons
from   genrics.guiOperations                         import  operation
import time

'''
This script contains multiple testcases and multiple testcase in single script could be handled much better using "@classmethod"  decorator as it avoids the reopening of browser window again and again for every testcase.Now in present script using @classmethod casusing error since all he gui operations and explict webdriver wait ex: webdriverwait(driver,10).until(driver.find_element_by_loctype('element Locator')) are made genric.All you need to do is updated the csv file for element locator type > import and call them in your script.
'''


class amaLogin(unittest.TestCase, Cons, operation):
    '''
    1.Invoke browser 2.enter the url 3.Maximize window.
    '''
    def setUp(self):
        global driver
        a=Cons('amazon', 'Firefox')
        b=a.funcConstants()
        print 'b', b[0], b[1]
        driver=super(amaLogin,self).InvokeBrowserAndMaximize(b[0],b[1])
        print 'driver', driver
        
        
    def testCase_login(self):
        '''
        1.Obtain all the GUI elements objests of Login Screen. 
        2.Execute all the 7 test case.
        '''
        # TEST CASE 1
        # email :      password:
        #Step 1 :Invoke the amazon homepage and click sign in button
        print "TC1 - email :   pwd:  "

        csvFilePath             = super(amaLogin, self).filePath("objectRepository_Login.csv")
        pageElementObject       = super(amaLogin, self).elePageObj(csvFilePath)
        #print "pageElementObject", pageElementObject
        LoginButtonClick        = pageElementObject['loginButton']
        LoginButtonClick        = eval(LoginButtonClick)
        LoginButtonClick.click()  
                          
        # Step 2 : LOGIN PAGE should be invoked;and click sign-in button without user id/email  and password.
        # a)GUI Standardization Testing. 
        # b)Functional Testing.
         
        elementObjEmail         = pageElementObject['elementObjEmail']
        elementObjPassword      = pageElementObject['elementObjPassword']
        elementObjSignIn        = pageElementObject['elementObjSignIn']
        
        #Eval func is used to evaluate the String
        global elementObjEmailLoc
        global elementObjPasswordLoc
        global elementObjSignInLoc
 
        elementObjEmailLoc      = eval(elementObjEmail)
        elementObjPasswordLoc   = eval(elementObjPassword)   
        elementObjSignInLoc     = eval(elementObjSignIn)   
        elementObjSignInLoc.click()
       
        print 'elementObjPasswordLoc',elementObjPasswordLoc 
        #Error message after Sign-in without Email(user id) and Password(pwd).  
        errorEmail              = pageElementObject['errorEmail']        
        errorPwd                = pageElementObject['errorPwd']
        
        # Since the obtained webdriver wait has XPATH having the keyword 'contains' the text was not completey read from CSV
        #;thus the below lines add up to the string, to obtain the complete webdriverwait statement. 
        str1=errorEmail
        str2=errorPwd
        str3=',\'Enter your email or mobile phone number\')]"))'  
        str4=',\'Enter your password\')]"))'
        strnew1=str1.replace(str1[96:151],str3)
        strnew2=str2.replace(str2[96:123],str4)
        errorEmailLoc              = eval(strnew1)
        errorPwdLoc                = eval(strnew2)
         
        # Assert the Error text message. 
        a=errorEmailLoc.size
        b=errorEmailLoc.text
        c=errorPwdLoc.text
        d=errorEmailLoc.get_attribute('text')
        print 'a,b,c,d',a,b,c,d
        errorMsgEmail ='Enter your email or mobile phone number' 
        errorMsgPwd   ='Enter your password' 
        driver.save_screenshot('homePage.png')
        try:
            assert errorMsgEmail==b
            assert errorMsgPwd==c

        except :
            print 'Assert Error'
        
       
        ## TEST CASE 2 :
        ## email/usr id:       password=password123
        #print "TC2 - email :   pwd:password123"
        #csvFilePath2             = super(amaLogin, self).filePath("objectRepository.csv")
        #pageElementObject2       = super(amaLogin, self).readers(csvFilePath2)
        ##elementObjEmailLoc.clear() 
        ##elementObjEmailLoc.send_keys(pageElementObject2['email'])  
        #elementObjPasswordLoc.clear() 
        #elementObjPasswordLoc.send_keys(pageElementObject2['password'])
        #elementObjSignInLoc
        #elementObjSignInLoc.click()
     
        ## ASSERT ERROR MESSAGE 
        #try:                        
        #    assert errorMsgEmail==b
        #                           
        #except :
        #     print 'Assert Error'

 
        ## TEST CASE 3:
        ## email/usr id:'hirebells@gmail.com'       password:

        #print "TC3 - email :hirebells@gmail.com   pwd:  "
        #csvFilePath2             = super(amaLogin, self).filePath("objectRepository.csv")
        #pageElementObject2       = super(amaLogin, self).readers(csvFilePath2)
        #print 'elementObjeEmailLoc',elementObjEmailLoc
        #elementObjEmailLoc.clear() 
        #elementObjEmailLoc.send_keys(pageElementObject2['email'])  
        #elementObjPasswordLoc.clear() 
        ##elementObjPasswordLoc.send_keys(pageElementObject2['password'])
        #elementObjSignInLoc
        #elementObjSignInLoc.click()
        #c=errorPwdLoc.text
        #                                                                                  
        ## ASSERT ERROR MESSAGE
        #try:
        #    assert errorMsgPwd==c            
        #except:
        #     print 'Assert Error'

        ## Test Case 4:                                                                               
        ## email/usr id:'hirebells@gamil.com'   password='wrongPassword'
        #print "TC4- email :hirebells@gmail.com   pwd:wrongPassword"
        #                                                                                          
        #csvFilePath2             = super(amaLogin, self).filePath("objectRepository.csv")        
        #pageElementObject2       = super(amaLogin, self).readers(csvFilePath2)
        #elementObjEmailLoc.clear() 
        #elementObjEmailLoc.send_keys(pageElementObject2['email'])  
        #elementObjPasswordLoc.clear() 
        #elementObjPasswordLoc.send_keys(pageElementObject2['wrongPassword'])
        #elementObjSignInLoc
        #elementObjSignInLoc.click()
        #                                                                                  
        ## ASSERT ERROR MESSAGE
        #
        ##b=errorEmailLoc.text 
        #try:                        
        #   # assert errorMsgEmail==b
        #    assert errorMsgPwd==c
        #                   
        #except :
        #     print 'Assert Error'
    

        # Test Case 5:
        # email/usr id:'wrongEmail'   password=password123
        print "TC5 - email :wrongEmail  pwd:password123"
        csvFilePath2                 = super(amaLogin, self).filePath("objectRepository.csv")
        pageElementObject2           = super(amaLogin, self).readers(csvFilePath2)
        elementObjEmailLoc           = eval(elementObjEmail)
        elementObjPasswordLoc        = eval(elementObjPassword)   
        elementObjSignInLoc          = eval(elementObjSignIn)   
        windowHandle                 = driver.window_handles
        print "pageElementObject2", pageElementObject2
        elementObjEmailLoc.clear() 
        elementObjEmailLoc.send_keys(pageElementObject2['incorrectEmail'])  
        elementObjPasswordLoc.clear()
        print 'pageEleObj2[passwrd]',pageElementObject2['password'] 
        elementObjPasswordLoc.send_keys(pageElementObject2['password'])
        elementObjSignInLoc.click()
                                                                                          
        # ASSERT ERROR MESSAGE
        #string                ='We cannot find an account with that email address'
        errorEmailPassword     =pageElementObject['errorEmailPassword3']
        errorEmailPassword     =eval(errorEmailPassword) 
        errorEmailActString    =errorEmailPassword.text
        print 'errorEmailActString',errorEmailActString 
        string ='To better protect your account, please re-enter your password and then enter the characters as they are shown in the image below.' 
        try:                        
            assert errorEmailActString==string                            
        except :
             print 'Assert Error'
        
        
        #TEST CASE 6: 
        #email/usr id :'hirebells@gamil.com'   password='password123'
        print 'driver', driver 
        print " Test Case 6"
        driver.save_screenshot('file1.png')
        time.sleep(10)
        driver.back()
        time.sleep(10)
        driver.save_screenshot('afterback.png')
        time.sleep(10)    
        page=driver.title
        print 'page', page
        list1=['Amazon Sign In','Problem loading page'] 
        if page==list1[1]:

            tryAgain=pageElementObject['errorPageTryAgain']
            tryAgainEle=eval(tryAgain)                             
            tryAgainEle.click()
            moto=driver.switch_to_alert()
            moto.accept() 
            driver.switch_to_window(windowHandle[0])
            driver.save_screenshot('pageError.png')
            elementObjEmailLoc      = eval(elementObjEmail)                                 
            elementObjPasswordLoc   = eval(elementObjPassword)   
            elementObjSignInLoc     = eval(elementObjSignIn)             
            elementObjEmailLoc.clear()                                                                   
            #print "pageElementObject2['email'] pageElementObject2['password']",pageElementObject2['email'],pageElementObject2['password']
            elementObjEmailLoc.send_keys(pageElementObject2['email'])  
            elementObjPasswordLoc.clear() 
            elementObjPasswordLoc.send_keys(pageElementObject2['password'])
            elementObjSignInLoc.click()
            time.sleep(10)
            str="amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"
            str5=pageElementObject['loggedIn'] 
            str1=""
            str5=str5.replace(str5[96:100],str1)                        
            str6=',\'Hello, hirebells\')]' 
            strLoggedIn=str5+str6 
            loggedInElement           = eval(strLoggedIn)
            signOutElement            = pageElementObject['signOut']
            signOut                   = eval(signOutElement)
            signOutAction             = super(amaLogin,self).ActionChains(loggedInElement,signOut)
        
        else:
            #print "right pwd and email" 
            #print 'elementObjEmailLoc',elementObjEmailLoc
            elementObjEmailLoc      = eval(elementObjEmail)                                 
            elementObjPasswordLoc   = eval(elementObjPassword)   
            elementObjSignInLoc     = eval(elementObjSignIn)             
            elementObjEmailLoc.clear()                                                                   
            #print "pageElementObject2['email'] pageElementObject2['password']",pageElementObject2['email'],pageElementObject2['password']
            elementObjEmailLoc.send_keys(pageElementObject2['email'])  
            elementObjPasswordLoc.clear() 
            elementObjPasswordLoc.send_keys(pageElementObject2['password'])
            elementObjSignInLoc.click()
            time.sleep(10)
            #print "hello how are you"                         
            #print 'driver.title1',driver.title     
            str="amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"
            #self.assertEqual(driver.title,str)  
            str5=pageElementObject['loggedIn'] 
            #print 'str5', str5                 
            str1=""
            str5=str5.replace(str5[96:100],str1)                        
            str6=',\'Hello, hirebells\')]"))' 
            strLoggedIn=str5+str6 
            print 'strLoggedIn',strLoggedIn
            loggedInElement           = eval(strLoggedIn)
            print 'loggedInElement',loggedInElement
            signOutElement            = pageElementObject['signOut']
            signOut                   = eval(signOutElement)
            #print 'signOut', signOut
            signOutAction             = super(amaLogin,self).ActionChains(loggedInElement,signOut)
               
        
        # Test Case 7:
        # email/usr id:'wrongEmail'  password='wrongPassword'
        print "TC7 - email :wrongEmail   pwd:wrongPassword"
        print "driver", driver
        #csvFilePath2            = super(amaLogin, self).filePath("objectRepository.csv")
        #pageElementObject2      = super(amaLogin, self).readers(csvFilePath2)
        elementObjEmailLoc      = eval(elementObjEmail)                                               
        elementObjPasswordLoc   = eval(elementObjPassword)   
        elementObjSignInLoc     = eval(elementObjSignIn)             
        elementObjEmailLoc.clear() 
        elementObjEmailLoc.send_keys(pageElementObject2['wrongEmail'])  
        elementObjPasswordLoc.clear() 
        elementObjPasswordLoc.send_keys(pageElementObject2['wrongPassword'])
       
        elementObjSignInLoc.click()
        errorEmailPassword=pageElementObject['errorEmailPassword3']
        errorEmailPassword=eval(errorEmailPassword) 
        print 'errorEmailPassword', errorEmailPassword
        textString               = errorEmailPassword.text
        print 'textString', textString
        errorEmailPasswordString = "   To better protect your account, please re-enter your password and then enter the characters as they are shown in the image below."
                                                                                          
        # ASSERT ERROR MESSAGE
        
        try:                        
            assert errorEmailPassword==textString
                           
        except :
             print 'Assert Error'

        
    def tearDown(self):
        driver.close()
       

        
if __name__ == "__main__":
    unittest.main()
