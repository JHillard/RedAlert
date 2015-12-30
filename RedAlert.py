
# coding: utf-8

# In[ ]:



    


# In[1]:

#RedPhone; get Reddit messages on your phone
##Written by Jake Hillard
#Send all unread mail or mentions in your Reddit Inbox to your 
#phone as a text message.
#Convienient if you don't want to constantly check old accounts for new messages.

#To enable this script to send emails you'll need to go to: 
#https://www.google.com/settings/security/lesssecureapps

#This code heavily influence by the getting started documentation for PRAW. Thanks for being so thorough 
#http://praw.readthedocs.org/en/stable/index.html
#Email code done with help from:  http://naelshiab.com/tutorial-send-email-python/

clientSecret = 'not_a_secret'
redirURI = 'http://127.0.0.1:7117/authorize_callback'
clientID = '9F_OR6upn6Gkqw'
logFile = "pushedMsgs.log" 
configFile = "RedAlert.cfg"
jobFile = "RedAlert.job"
jobEdit = True
maxUsers = 10

try:
    import time
    import praw
    import requests
    import random
    import smtplib
    import sys
except: raise Exception("Couldn't import needed libraries. See www.RedAlert.readthedocs.org to see required packages to run this script")

class Job():
    def __init__(self, redditOblisk, job = 'M', waitTime = None, postID = None, subRT = None, keywords = None, userIndex = 0):
        self.msgKey = "M"  #keys to declare jobs. When declaring a job, give these
        self.keywordKey = "K"
        self.postKey = "P"
        
        s1 = "self.makeJob( userIndex=" +str(userIndex) + ", job='" + str(job) + "',waitTime ='" + str(waitTime) + "',postID='"
        s2 =  str(postID) +"',subRT='"+str(subRT)+"'" + ',keywords="'+str(keywords)+'")'
        
        self.execString = s1 + s2 + "\n"
        self.userIndex = userIndex
        self.job = job
        self.reddit = redditOblisk
        self.waitTime = waitTime
        self.postID = postID
        self.subRT = subRT
        self.keywords = keywords
        self.prevTime = time.time() 
        self.checkInputs()
        print("Job made: "+ self.toString() )
        
    def checkInputs(self):#makes sure each input to the job is formatted correctly, and throws error if not.
        if (self.job is self.keywordKey): 
            if (self.subRT is not None) and isinstance(self.subRT, str):
                if self.keywords is not None and isinstance(self.keywords, str):
                    self.keywords = self.keywords.lower()
                    self.subExist()
                    return
        if (self.job is self.msgKey):
            return
        if (self.job is self.postKey):
            if self.waitTime is not None:
                if self.postID is not None and isinstance(self.postID, str): return
        raise Exception("Inputs formatted incorrectly")
        
    def execute(self):
        if self.job is self.msgKey:
            self.checkMessages()
        elif self.job is self.keywordKey:
            self.checkKeywordSubreddit()
        elif self.job is self.postKey:
            if (time.time() - self.prevTime) > self.waitTime*60:
                self.checkPost()
                self.prevTime = time.time()
            
    def printVars(self):
        print(self.job)        
        print(self.postID)
        print(self.keyword)
        
    def getAll(self):
         return [self.job, self.waitTime, self.postID, self.subRT, self.keywords, self.userIndex] 

    def toString(self):
        if self.job is self.msgKey:
            return "Message Checker for u/" + self.reddit.get_me()._case_name
        elif self.job is self.keywordKey:
            return "Keyword Checker for r/" + self.subRT + " Keywords: " + self.keywords
        elif self.job is self.postKey:
            return "Post Monitor for " + self.reddit.get_submission(submission_id = self.postID).title + ". Sending every " + str(self.waitTime) + " seconds. On r/" + self.reddit.get_submission(submission_id = self.postID).subreddit.title 
        
    def pushDelivered(self, name):
        try:
            f = open (logFile,"r")
        except:
            return False
        while True:
            line = f.readline()
            if (line == str(name) + "\n"): 
                f.close()
                return True
            if not line:
                f.close()
                return False
            
    def recordSent(self, name):
        f = open(logFile, 'a')
        f.write(str(name) + "\n")
        f.close()

    def subExist(self):
        temp = self.reddit.get_subreddit(self.subRT) #to check if subreddit exists. If not, this throws exception.
        for submission in temp.get_hot(limit=10):  
             test = submission.selftext.lower().split(' ')
    
    def sendEmail(self, pushId, body):
        if self.pushDelivered(pushId): return 
        #Code help here from http://naelshiab.com/tutorial-send-email-python/
        print(body)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(emailAddr,emailPass)
        prefix = 'Content-Type: text/plain; charset="us-ascii"\nMIME-Version: NA\nContent-Transfer-Encoding: 7bit\nSubject:\nFrom: \nTo:\n\n'
        #prefix attaches the proper headers and encoding information so that the passed body gets sent through. Boy this was one hell of a bug.
        msg = prefix + body
        server.sendmail(emailAddr, pNum, msg) 
        server.quit()
        self.recordSent(pushId)
        print("Pushed to Phone:")
        print(body); print("\n\n-------------------------------------------------------\n\n")
    
    def phonePush(self, pushId, fLine, sLine, tLine):
        if self.pushDelivered(pushId): return 
        payload = {'value1' :fLine + "\n", 'value2': "\n" + sLine + "\n\n", 'value3': tLine + '\n'}
        t = requests.get(notifURL, params = payload)
        if t.status_code == 200:
            print("Pushed to Phone:")
            print(payload); print("\n")
            self.recordSent(pushId)
            return
        else: raise Exception("Couldn't send message")
            
    def checkMessages(self):#Sends any unread messages to you. Won't send an unread msg more than once.          
        for msg in self.reddit.get_unread():
            push = "rMessage from: "+ str(msg.author) + "\n" + str(msg.subject) + "\n" + str(msg.body)
            self.sendEmail( msg.name, push)
            #self.phonePush( msg.name, firstLine, secondLine, thirdLine)
             
    def checkPost(self):#Looks at post and pushes its title, its vote count, and how many comments it has
        submission = self.reddit.get_submission(submission_id = self.postID)
        fL = "Submission Update for: " + submission.title
        sL = "Up votes: " + str(submission.ups) +" Down votes: " + str(submission.downs)
        tL = "Number of Comments: " + str(submission.num_comments)
        push = fL + "\n" + sL + "\n" + tL
        print(push)
        print(type(push))   
        self.sendEmail(str(random.random()), push)
        #self.phonePush(str(random.random()), firstLine, secondLine, thirdLine)
                
    def checkKeywordSubreddit(self): #Monitors subreddit for posts with a specific keyword
        #keywords = "key key2 etc" seperate them by spaces.
        #TODO: make it so it searchs all submissions, not just first.
        subreddit = self.reddit.get_subreddit(self.subRT)
        for submission in subreddit.get_hot(limit=10):  
            text = submission.selftext.lower().split(' ') + submission.title.lower().split(" ")
            t = self.keywords.split(" ")
            if any(string in text for string in t ):
                push = "Keyword found in r/" + self.subRT + ":\n" + submission.title + "\n" + submission.selftext
                self.sendEmail(str(submission.id), push)
                #self.phonePush(str(submission.id), "", "Keyword found in " + self.subRT, submission.title + "\n" + submission.selftext )
  

class UserManager():
    def __init__(self):
        self.users = []
        self.jobList = []
        self.initConfig()        
        self.makeUser()        
        self.initJobs()
        
    def initConfig(self):
        try:
            config = open(configFile)
        except:
            self.genConfig()
            config = open(configFile)
        try: 
            exec(config.read())
        except:
            print("Error parsing config file. Deleting...")
            self.genConfig()
            self.initConfig()
        config.close()

    def genConfig(self):
        print("No config found, creating... ")
        config = open(configFile, 'a')
        config.close()
        config = open(configFile, 'w')        
        config.write("global emailAddr\n")
        config.write("global emailPass\n")
        config.write("global pNum \n" )
        config.write("global userAgent\n" )
        
        config.write( "emailAddr = '" + input("Email Address (did you enable access to your email?\nhttps://www.google.com/settings/security/lesssecureapps): \n")+ "'\n")
        config.write( "emailPass = '" + input("Email Password: ")+ "'\n")
        str1 = "Phone Number (must be in form 1234567890@{carrier address}:"
        str2 = "Ex: Verizon is @vtext.com (Check docs to find what works for you)"
        config.write( "pNum = '" + input(str1 + "\n" + str2 + "\n" )+ "'\n" )
        config.write( "userAgent  = 'RedAlert App for u/"+ strInp("Reddit user name: ") + "'\n")
        config.close()
      

    def initJobs(self):
        try:
            jobs = open(jobFile, "r")
        except:
            self.genJobs()
            jobs = open(jobFile, "r")
        try: 
            #TODO: Warn about running with elevated priviledges. We've imported sys here,
            #so typing in an rm command into the job file could fuck some shit
            line = "temp"
            while line:
                line = jobs.read()
                exec(line)
        except IndexError:
            print("Job file contains jobs for multiple users. Please authenticate those users now.\n")
            self.jobList = []
            self.makeUser()
            self.initJobs()
        except: raise
            #TODO: uncomment
            #raise Exception("Error parsing jobs file. Perhaps too many users? Please delete and reconfigure")
        jobs.close()
            
    def genJobs(self):
        print("No jobs founds, creating...")
        jobs = open(jobFile, 'a')
        jobs.close()
        jobs = open(jobFile,'w')
        jobs.write("self.makeJob()\n")
        jobs.close()
        print("New job file created.")
    
    def getUser(self, index):
        return self.users[index]
    
    def makeUser(self):
        #TODO: SWAP these
        self.users.append(self.authenticate())
        #self.users.append(praw.Reddit(user_agent = userAgent))
    def authenticate(self):
        try:
            r = praw.Reddit(user_agent = userAgent)
            r.set_oauth_app_info(client_id=clientID,
                               client_secret=clientSecret,
                               redirect_uri = redirURI)
            authURL = r.get_authorize_url('RedAlert access', 'privatemessages read identity', True)
            print(authURL)
            print("Open URL above and grant access, you'll be redirected to a dead webpage with an access code embedded in its URL" + 
                 "\nCopy that code and paste below (Ctrl + shift + v if running in terminal)")
            self.AccessCode = input("Access Code: ")
            self.authenticatedUser = accessInformation = r.get_access_information(self.AccessCode)
            print("Reddit Authenticated Successfully\n")
        except:
            raise Exception("Reddit Failed to authenticate. Please restart and try again. Was the code pasted incorrectly?")
        return r
            
    def execUserJobs(self,index):
        for i,job in enumerate(self.jobList):
            if job.userIndex == index: self.jobList[i].execute()

    def execAllJobs(self):
        for job in self.jobList:
            job.execute()

    def delUser(self, index):
        for i,job in enumerate(self.jobList):
            if job.userIndex == index: delJob(i)
        del self.users[index]

    def delJob(self, index):
        if index >= len(self.jobList): 
            print("Index larger than job list. No changes made.")
            return
        del self.jobList[index]
        self.writeJobs()

    def writeJobs(self):
        f = open(jobFile, "w")
        for job in self.jobList:
            f.write(job.execString)
        f.close()
    
    def listUsers(self):
        print("Users: ")
        #TODO: fix none display error
        for i, user in enumerate(self.users):
            print("\t" + str(i) + ": " + user.get_me()._case_name) 

    def listSubRPosts(self, subRT): #Lists posts on a subreddit with their title, vote counte, and ID. 
                                    #Usefull for checkPost() which requires an ID.
        subreddit = self.users[0].get_subreddit(subRT)
        for submission in subreddit.get_hot(limit=10):
            print(submission.title)
            print("Up votes: " + str(submission.ups) +" Down votes: " + str(submission.downs) )
            print("ID: " + submission.id + "\n\n")
        #TODO add error: Requires an active SingleUser() to call this line.
            
    def listJobs(self):
        [print("\t" + str(i) + ": " + job.toString()) for i,job in enumerate(self.jobList) ]
                
               
            
    def makeJob(self, userIndex = 0, job = 'M', waitTime = 0, postID = None, subRT = None, keywords = None):
        self.jobList.append(Job(self.users[userIndex], userIndex = userIndex, job = job, waitTime = waitTime, postID= postID, subRT = subRT, keywords = keywords))   
    
    

    def makeKeywordJob(self, subRT, keywords, userIndex=0):
        self.makeJob(job = 'K', subRT = subRT, keywords = keywords, userIndex = userIndex)   
        
    def makeSubMonitor(self, postID, waitTime, userIndex=0):  
        self.makeJob(job = "P", postID = postID, waitTime = waitTime, userIndex = userIndex)

    def printJobFile(self):
        f = open(jobFile, "r")
        line = "temp"
        while line:
            line = f.readline()
            print(line)
        f.close()


def strInp(display):
    returnString = ""
    while True:
        returnString = input(display)
        if '"' in returnString:
            print("Don't put" + ' a " in there. That breaks things. If you really need it, use the custom job input.')
            
        elif returnString: return returnString
        print("Invalid string input.")
def intInp(display):
    returnString = ""
    while True:
        returnString = input(display)
        if returnString:
            try:
                returnInt = int(returnString)
                return returnInt
            except: None
        print("Invalid integer input")

def menu():
    if jobEdit:
        while True:
            print("Job File Contents: ")
            r.printJobFile()
            print("You are now editing the job file.\nCurrent jobs:")
            r.listJobs()
            print("What would you like to do?\n\t1.Add job\n\t2.Delete Job\n\t3.Add User\n\t4.Run RedAlert")
            menu = intInp("")
            if menu == 4: break
            if menu == 1: addJobs()
            if menu == 3: r.makeUser()
            if menu == 2: 
                r.listJobs()
                index = intInp("Enter job index you'd like to delete (Choose out-of-bounds index to exit): ")
                r.delJob(index)
def addJobs():
    print("What task do you want to add:\n\t1.Message checker\n\t2.Subreddit Keyword Monitor\n\t3.Submission Monitor\n\t4.Custom Job Entry\n\t5.Back")
    menu = intInp("")
    if menu == 1:
        UI = maxUsers
        while UI >= len(r.users):
            print(r.listUsers())
            UI = intInp("User index: ")
            if(UI >= len(r.users)): print("Index must be a valid user ")
        r.makeJob(userIndex = UI  )  
        r.writeJobs()
        print("Message checker added for user " + r.users[UI].get_me()._case_name )
    if menu == 2: 
        subRT = strInp("Subreddit: ")
        keywords = strInp("Keywords (seperate by spaces): ")
        try: r.makeKeywordJob(subRT, keywords)
        except: print("Bad Subreddit. No changes made.")
        r.writeJobs()
        print("Keyword Monitor (" + keywords + ") added to subreddit r/" + subRT)
    if menu == 3: 
        subRT = input("Subreddit to display posts (enter to skip): ")
        if subRT:
            try: r.listSubRPosts(subRT)
            except: print("Bad Subreddit. None displayed") 
        pID = strInp("Post ID: ")
        upFreq = intInp("Update frequency (in minutes): ")
        try: r.makeSubMonitor(pID, upFreq)
        except: print("Bad Post ID. No changes made")
        r.writeJobs()
    if menu == 4:
        execString = input("Custom job (Advanced):")
        try:
            exec(execString)
            r.writeJobs()
        except:
            print("Job String:" + execString + "\n") 
            print("Bad Job string. Perhaps incorrect custom job?")





print("Compiled Methods")  


# In[7]:

r = UserManager()
menu()
print("RedAlert running!")

while True:
    r.execAllJobs()