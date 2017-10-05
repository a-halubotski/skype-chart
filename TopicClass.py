"""
Skype topic class
"""
#pylint: disable-msg=C0103

import datetime

class Topic:
    """ Skype topic """

    def __init__(self, topicId):
        """ constructor """
        self._topicId = topicId
        self._conversations = []

    def append(self, line):
        """ append extracted data """
        self._conversations.append(self.sanitize(line))

    def sanitize(self, line):
        """ Extracts only required data """
        fields = line.strip().split(',')
        try:
            dt = datetime.datetime.utcfromtimestamp(int(fields[5][:10]))
            return (fields[2].replace('"', ''), dt)
        except IndexError:
            return None
        except OSError:
            print("OSError: " + str(fields[5]))
            return None

    def conversations(self):
        return self._conversations

    def accepts(self, line):
        return line.find(self._topicId) > 0
