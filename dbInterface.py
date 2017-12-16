class History(object):
    def __init__(self, name, userID):
        self.name = name
        self.userID = userID
        self.history = []

    def logMessage(self, lastMessage):
        if len(self.history) > 10:
            self.history.pop()
        self.history.append(lastMessage)

    def getLastMessages(self, num):
        historyWanted = int(num)

        if historyWanted > len(self.history):
            historyWanted = len(self.history)

        lastMessages = self.history[--historyWanted:]
        return lastMessages
