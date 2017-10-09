# Required methods : Invoke browser, Enter the URL, Quit or Close the Browser.
from    selenium   import webdriver
from    Constants  import *
import  unittest
from    selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class InvokeBrowser(object, Cons):
    
    def setUp1(self, urlValue,browserValue):
       
        print 'in bowsersetup and urlValue:', urlValue
        capabilities = {}
        inst=super(InvokeBrowser, self).funcConstants(urlValue,browserValue) 
        print "inst[0]and inst[1]", inst[0],inst[1]
        browserType=inst[0]
        urlType    =inst[1]                     

        if inst[0] == 'Firefox':
            capablities             = DesiredCapabilities.FIREFOX.copy()
            capablities["version"]  = "41.0"
            capablities["platform"] = "LINUX"
            print "I am in def browserSetUp.setUp1"
            global driver
            self.driver = webdriver.Firefox()
            #self.driver = webdriver.Remote(desired_capabilities=capablities, command_executor = "http://localhost:4444/wd/hub")
            self.driver  = webdriver.Remote(desired_capabilities=capablities, command_executor = "http://192.168.237.161:5566/wd/hub")
            driver       = self.driver
            driver.maximize_window()
            driver.get(urlType)
            return driver
           

        elif  BP_Constants['browser'] == browser[1]:
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()

        elif  BP_Constants['browser'] == browser[2]:
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()

        else:
            print "The browser is not supported kindly check with supported browser @ <www.google.com> have a nice day>"

    def test_Url(self):
        pass

    def teardown1(self):
        driver.quit()
#----------------------------
if __name__ == "__main__":
    inst = InvokeBrowser()
    print inst
    inst.setUp()
    #inst.test_Url()
    #inst.teardown()
