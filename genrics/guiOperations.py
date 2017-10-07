from   selenium                                 import webdriver
from   selenium.webdriver.support.select        import Select
from   selenium.webdriver.support.wait          import WebDriverWait
from   selenium.webdriver.support               import expected_conditions as EC
from   selenium.webdriver.common.by             import By
from   selenium.webdriver.common.action_chains  import ActionChains
from   Constants import *
import re
#from   browserSetUp                             import InvokeBrowser

class  operation(object):
    # obatain the element page object
    '''Contains all the GUI operations and results which obtained by performing the GUI operations'''

    def InvokeBrowserAndMaximize(self,browser=None,url=None):
        global driver 
        browser             = browser + '()'
        webdriverBrowser    = 'webdriver.' + browser
        self.driver         = webdriverBrowser 
        driver              = eval(self.driver)
        driver.get(url)
        driver.maximize_window()
        return driver
    
    def readers(self,filename):# name of the CSV file.
        self.filename=filename
        import csv
        openfile = open(self.filename, "a+")
        reader   = csv.reader(openfile)
        EleobjLoc= {}
        for row in reader:
            EleobjLoc[row[0]]=row[1]
        print 'hello', EleobjLoc
        return EleobjLoc
            

    def elePageObj(self, filename):#, pageObjType=None, InspctPageObj=None):
        self.filename=filename
        print "filename", filename
        '''
        elePageObj class will return the pageElementObject of GUI on which GUI operations needs to be performed
        ex:
        pageObjType is type of the PageElementObject : Xpath or Css or id or name or tagName etc.
        '''
        import csv
        ElementObj={}
        fo=open(self.filename, "a+")      # fo is the file object for the file reader 
        reader=csv.reader(fo)        # Reader creates the object containting the data of the csv file 
        for row in reader:
            
            #pageElementObjects = ['^xpath', '^id', '^name','^css', '^link_text', '^partial_link_text', '^partial_class_name','^tag_name'] 
            pageElementObjects = ['xpath', 'id', 'name','css', 'link_text', 'partial_link_text', 'partial_class_name','tag_name'] 
            
            for x in pageElementObjects:
                
                regExp = re.compile(row[1])
                regExp = re.match(regExp, x)
                if regExp is not None:
                    
                    regExpString = regExp.group()
                    a = 'driver.find_element_by_' 
                    b = regExpString
                    c = a + b               
                    value  = c+'(' +'"'+row[2]+ '"' + ')'
                    pageElementObject = 'WebDriverWait(driver, 10).until(lambda driver:' +  value + ')'
                    ElementObj[row[0]]=pageElementObject
        return ElementObj

    def filePath(self, file):
        from os import environ
        path=environ['TAFTOOLSET']
        path=path + '/' + file
        return path 
        
    def send_keys(self, parm):
        print "send keys"
        self.parm = parm 
        evalPageElementObject.clear()
        evalPageElementObject.send_keys(parm)


    def click(self):
        print "evalPageElementObj:", evalPageElementObject
        evalPageElementObject.click()


    # Action_Chains - hovering over the menu object an select:
    def Action_Chains(self, menu, submenu1 = None, submenu2 = None, submenu3=None, submenu4= None):
        global actions
        actions = ActionChains(driver)
        actions.move_to_element(menu)
        actions.click(submenu1)
        actions.perform()
        
    def rightClick(self):
        actions = ActionChains(driver)       
        act     = actions.context_click(evalPageElementObject)
        act.perform()

    def getAtttribute(self, pageElementObject, name):
        value = evalPageElementObject.get_attribute(name)
        print  value

    def DoubleClick(self):
        
        #Double-clicks an element.
        #on_element: The element to double-click. If None, clicks on current mouse position.
        actions = ActionChains(driver)       
        act     = actions.context_click(evalPageElementObject)
        act.perform()
    


    def drag_and_drop(self, source=None, target=None):
        #  Holds down the left mouse button on the source element, then moves to the target element and releases
        #  the mouse button.Args
        #  source: The element to mouse down.
        #  target: The element to mouse up.
        actions = ActionChains(driver)
        act = actions.drag_and_drop(source, target)
        act.perform()
     
      # Moving between windows and frames
    def switch_to_window(self, winNumber=0):# when all the window handles are captured as list;the number to which the driver should be switched is provided in num
        self.winNumber =   winNumber
        allWinHandle   =   driver.window_handles
        mainWinHandle  =   allWinHandle[winNumber]
        print "allWindowhandle:", mainWinHandle 
        if handle     !=  mainWinHandle:
            driver.switch_to_window(handle)
            
     
     
    def switch_to_frame(self, frameName):
        driver.switch_to_frame(frameName)
      
    # Handling pop Up's
    def switch_to_alert(self, action): 
        act = driver.switch_to.alert
        print "act", act
        try:
            if action == 'accept':
                print "in Accept"
                act.accept()
            elif  action == 'dismiss': 
                print "in Dismiss"
                act.dismiss()
                
            else : 
                print "need to know more"
        except:
            print "Error"   

 
    def select(self, selectBy, index=None, text=None, value=None):
        from selenium.webdriver.support.ui import Select
        select = Select(evalPageElementObject)
        try:
            if selectBy == index:
                select.select_by_index(index)
            elif  selectBy == visible_text:   
                select.select_by_visible_text("text")
            elif  selectBy == value: 
                select.select_by_value(value)        
            else:
               print "Inappropriate parameter passed"
         
        except AttributeNotPassed:
            print  "AttributeNotPassed"


 
if __name__=="__main__":
    inst     = operation()
    filePath = inst.filePath("objectRepository_Login.csv")
    #man      = inst.readers(filePath) 
    #print man

    #filePath = inst.filePath("objectRepository_Login.csv")
    casio    = inst.elePageObj(filePath)
    #casio    = inst.elePageObj("object.csv")
    print"casio", casio
    #print"filePath", filePath  
   
   
    
    
         
