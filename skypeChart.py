"""
Skype history analyzer
"""
#pylint: disable-msg=C0103,C0111

import sys
import codecs
import operator
from TopicClass import Topic

def groupByContactManualReduce(messages):
    result = {}
    for mm in messages:
        if mm.contactId in result:
            result[mm.contactId] = result[mm.contactId] + 1
        else:
            result[mm.contactId] = 1

    return result

def main():
    """ Main entrypoint """

    if sys.stdout.encoding != 'uft-8':
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

    topic = Topic('9f99004df4f849f5b0eb5a9d958f4c90')

    try:
        with open('data/SkypeChatHistory2.csv', encoding='utf-8') as data:
            for line in data:
                if topic.accepts(line):
                    topic.append(line)

    except IOError as err:
        print('You got an error: ' + str(err) + " " + str(err.__cause__))

    print("Messages in topic: %d" % len(topic.messages))

    recent = topic.recentMessages(days=90)

    stats = groupByContactManualReduce(recent)

    for k in sorted(stats.items(), key=operator.itemgetter(1)):
        print(str(k))

if __name__ == '__main__':
    main()
