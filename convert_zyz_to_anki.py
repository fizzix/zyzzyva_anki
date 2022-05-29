import numpy
import string

filename = '9s_all_raw_defsym.txt'
writefile = '9s_all_anki.txt'


lines = open(filename).readlines()
wf = open(writefile, 'w')

wordlist = []
playlist = []

#For CSW and not TWL just check for #.  For new words, check for an instance of + without #
def selectLine(line):
    return True, line
    #goodLine = False
    #if '+' in line:
    #    goodLine = True
    #return '+' in line, line
    #return goodLine, line
    # while '+' in line:
        # ind = line.find('+')
        # if line[ind - 1] != '+':
            # goodLine = True
        # line = line[:ind] + line[ind+1:]
    # return goodLine, line


class wordset:
    def __init__(self, startstring):
        self.alphagram = startstring[3:-1]
        self.play = 50000
        self.csw = False
        self.numwords = 0
        self.answers = []

    def process_answer(self, line):
        line.decode('utf-8', 'ignore')
        [goodLine, adjustLine] = selectLine(line)
        temp = str.split(adjustLine)
        if goodLine:
            self.csw = True
            if int(temp[-1]) < self.play:
                self.play = int(temp[-1])
        ansstr = ''
        
        # reconstruct the string
        for segnum in range(1,len(temp)-1):
            if temp[segnum] == self.alphagram or temp[segnum] == self.alphagram+'*' or temp[segnum] == self.alphagram+'#':
                temp[segnum] = '-'
            ansstr += temp[segnum]
            if segnum < len(temp) - 2:
                ansstr += ' '
        self.answers.append(ansstr)
        self.numwords += 1

    def write_word(self, wf):
        ws = ''
        ws += self.alphagram
        ws += ' ('
        ws += str(self.numwords)
        ws += '); '
        if len(self.answers) == 1:
            ws += self.answers[0]
        else:
            for i in range(len(self.answers) - 1):
               
                    
                ws += self.answers[i]
                ws += ' <br>'
            ws += self.answers[-1]
        ws += '\n'
        wf.write(ws)

            
word = wordset('\n')            

for line in lines:

    if len(line) == 1:
        if word.csw:
            wordlist.append(word)
            playlist.append(word.play)

    if line[0] == 'Q':
        word = wordset(line)
    if line[0] == 'A':
        word.process_answer(line)
        
#process all the data
indices = numpy.argsort(playlist)

for index in indices:
    wordlist[index].write_word(wf)
