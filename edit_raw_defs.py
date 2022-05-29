#go through one of the raw files and change the definitions 
#so that they mark collins words properly.
import bisect

data = open('9s_all_raw_csw15.txt').readlines()
words = open('all_csw_marked_alpha.txt').readlines()

wf = open('9s_all_raw_defsym.txt','w')

for line in data:

    if len(line) < 2:
        wf.write(line)
        continue
    if line[0:2] != 'A:':
        wf.write(line)
        continue
    #print line

    linesplit = line.split()
    for i in xrange(len(linesplit)):
        #Only care about stuff that is all uppercase
        seg = linesplit[i]
        if not seg.isupper():
            continue

        #We want just the word
        justtheword = ''
        wordlen = 0
        for letter in seg:
            if letter.isalpha():
                justtheword += letter
                wordlen += 1
        
        #ignore -s, -ed, -ing
        if justtheword == 'S' or justtheword == 'ED' or justtheword == 'ING':
            continue
            
        #The word is already marked
        if len(seg) > wordlen:
            if seg[wordlen] == '#':
                continue

        #find the appropriate spot in the word list
        k = bisect.bisect_left(words, justtheword)
        if k >= len(words):
            continue
        
        #figure out if it's british
        if words[k][0:wordlen] != justtheword:
            addsymbol = '*'
        elif words[k][wordlen] == '#':
            addsymbol = '#'
        else:
            continue

        #reconstruct the word
        newseg = justtheword + addsymbol
        if len(seg) > wordlen:
            newseg += seg[wordlen:]

        linesplit[i] = newseg

    #Remake the whole line
    newline = ' '.join(linesplit)
    wf.write(newline)
    wf.write('\n')

wf.close()
            
