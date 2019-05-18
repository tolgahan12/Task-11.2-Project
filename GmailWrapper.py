#!/usr/bin/env python
 
from imapclient import IMAPClient, SEEN
 
SEEN_FLAG = 'SEEN'
UNSEEN_FLAG = 'UNSEEN'
 
class GmailWrapper:
    def __init__(self, host, userName, password):
        self.host = host
        self.userName = userName
        self.password = password
        self.login()
 
    def login(self):
        print('Logging in as ' + self.userName)
        server = IMAPClient(self.host, use_uid=True, ssl=True)
        server.login(self.userName, self.password)
        self.server = server

    def getIdsBySubject(self, subject, unreadOnly=True, folder='INBOX'):
        self.setFolder(folder)  
 
        self.searchCriteria = [UNSEEN_FLAG, 'SUBJECT', subject]
 
        if(unreadOnly == False):
            self.searchCriteria.append(SEEN_FLAG)
 
        return self.server.search(self.searchCriteria)
 
    def markAsRead(self, mailIds, folder='INBOX'):
        self.setFolder(folder)
        self.server.set_flags(mailIds, [SEEN])
 
    def setFolder(self, folder):
        self.server.select_folder(folder)
