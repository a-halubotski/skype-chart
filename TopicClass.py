"""
Skype topic class
"""
#pylint: disable-msg=C0103,C0111

import datetime

class Message:
    """ Message in a topic """
    def __init__(self, contactId, messageDateTime):
        self._contactId = contactId
        self._messageDateTime = messageDateTime

    @property
    def contactId(self):
        return self._contactId

    @property
    def time(self):
        return self._messageDateTime

    def __str__(self):
        return 'Message: {contactId=%s, time=%s}' % (self._contactId, self._messageDateTime)

    def inRange(self, days):
        """ Checks if the message was sent withing specified days range """
        return self._messageDateTime >= datetime.datetime.now() - datetime.timedelta(days=days)

class Topic:
    """ Skype topic/conversation """

    def __init__(self, topicId):
        self._topicId = topicId
        self._messages = []

    def append(self, line):
        try:
            self._messages.append(self.sanitize(line))
        except:
            # could be parsing or index access errors
            pass

    def sanitize(self, line):
        fields = line.strip().split(',')
        dt = datetime.datetime.utcfromtimestamp(int(fields[5][:10]))
        return Message(fields[2].replace('"', ''), dt)

    @property
    def messages(self):
        return self._messages

    def accepts(self, line):
        return line.find(self._topicId) > 0

    def recentMessages(self, days=30):
        return [msg for msg in self._messages if msg.inRange(days=days)]
