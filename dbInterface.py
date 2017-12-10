class History(object):
    def __init__(self, name, userID):
        self.name = name
        self.userID = userID

    def logMessage(self, lastMessage):
        if len(history) > 10:
            self.history.pop()
        self.history.append(lastMessage)

    def getLastMessages(self, num):
        lastMessages = [history[len(history) - num] for index in b]
