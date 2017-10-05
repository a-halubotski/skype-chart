"""
Skype history analyzer
"""
#pylint: disable-msg=C0103


import sys
import codecs
from TopicClass import Topic

def main():
    """ Main entrypoint """

    if sys.stdout.encoding != 'uft-8':
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

    topic = Topic('9f99004df4f849f5b0eb5a9d958f4c90', )

    try:
        with open('SkypeChatHistory2.csv', encoding='utf-8') as data:
            for line in data:
                if topic.accepts(line):
                    topic.append(line)

    except IOError as err:
        print('You got an error: ' + str(err) + " " + str(err.__cause__))

    # analyze

#    for fl in topic.conversations():
#        print(str(fl))

if __name__ == '__main__':
    main()
