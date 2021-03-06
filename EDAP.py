
#ehab.hussein@ioactive.co.uk ;  @__obzy__
#ahmed@abdelrahman.net

from sys import argv, exit
import base64
import hashlib
import random
import re

hosts = []
customizedList = []

class Probability():
    def __init__(self):
        self.charset = list()
        #self.readwords = list(set([i for i in open(raw_input("enter filename: "),'r').xreadlines()]))
        self.readwords = list(set([i for i in open(argv[1],'r').xreadlines()]))
        self.alphaupperindexes = list()
        self.alphalowerindexes = list()
        self.integerindexes = list()
        self.nonalphanumindexes = list()
        self.frequencies = dict()
        self.fullkeyboard = list("`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?")
        self.discardedcharset = list()
        self.unusedindexes = list(range(len(max(self.readwords, key=len).strip())))
        self.finalcharset = list()
        self.countUpper = 0
        self.countLower = 0
        self.countDigits = 0
        self.countOther = 0
        self.pppc = 1
        self.word_dct = dict()

    def getdifflist(self,full,thelist):
        return list(set(full) - set(thelist))

    def getcharset(self):
        for word in self.readwords:
            for char in word.strip():
                if char not in self.charset:
                    self.charset.append(char)
        self.discardedcharset = self.getdifflist(self.fullkeyboard,self.charset)

    def getcase(self,char):
                if char.isupper():
                    return "U"
                elif char.islower():
                    return "l"
                elif char.isdigit():
                    return "n"
                elif not char.isupper() and not char.islower() and not char.isdigit():
                    return "@"
                else:
                    pass

    def getindexes(self):
        print "\n\nKeys: {U = Uppercase, l = Lowercase , n = Integers , @ = symbols}\n\n[+] Finding Character types with positions in each word"
        for word in self.readwords:
            word = word.strip()
            self.word_dct[word] = []
            for index,char in enumerate(word.strip()):
                if char.isupper():
                    print "U |",
                    self.countUpper+=1
                    self.word_dct[word] += 'U'
                    if index not in self.alphaupperindexes:
                        self.alphaupperindexes.append(index)
                elif char.islower():
                    print "l |",
                    self.countLower +=1
                    self.word_dct[word] += 'l'
                    if index not in self.alphalowerindexes:
                        self.alphalowerindexes.append(index)
                elif char.isdigit():
                    print "n |",
                    self.countDigits +=1
                    self.word_dct[word] += "n"
                    if index not in self.integerindexes:
                        self.integerindexes.append(index)
                elif not char.isupper() and not char.islower() and not char.isdigit():
                    print "@ |",
                    self.countOther +=1
                    self.word_dct[word] += '@'
                    if index not in self.nonalphanumindexes:
                        self.nonalphanumindexes.append(index)
                self.frequencies[char] = self.frequencies.get(char, 0) + 1
            print " "+word
        if len(self.getdifflist(self.unusedindexes,self.alphaupperindexes)) == 0 and \
            len(self.getdifflist(self.unusedindexes,self.alphalowerindexes)) == 0 and \
            len(self.getdifflist(self.unusedindexes,self.integerindexes)) == 0 and \
            len(self.getdifflist(self.unusedindexes,self.nonalphanumindexes)) == 0:
                print "All indexes have been used by all types of characters\n"
        self.finalcharset = self.getdifflist(self.fullkeyboard,self.discardedcharset)
        self.maxcombinationwordsgenerator = len(self.finalcharset) ** len(self.unusedindexes)

    def frequency_index_vertical(self):
        print "\n\n\n[+] Starting frequency with index analysis(vertical)"
        self.word_list_v = list()
        self.analysis_dct_v = dict()
        for key, val in self.word_dct.items():
            self.word_list_v += [val]
        for l in self.word_list_v:
            for i, w in enumerate(l):
                if not self.analysis_dct_v.get(i):
                    self.analysis_dct_v[i] = dict()
                    if not self.analysis_dct_v[i].get('U'):
                        self.analysis_dct_v[i]['U'] = 0
                    if not self.analysis_dct_v[i].get('l'):
                        self.analysis_dct_v[i]['l'] = 0
                    if not self.analysis_dct_v[i].get('n'):
                        self.analysis_dct_v[i]['n'] = 0
                    if not self.analysis_dct_v[i].get('@'):
                        self.analysis_dct_v[i]['@'] = 0
                self.analysis_dct_v[i][w] += 1
        for k,v in self.analysis_dct_v.items():
            print "index: ", k, v

    def frequency_index_horizontal(self):
        print "\n\n[+] Starting frequency with index analysis(horizontal)"
        self.word_list_h = list()
        self.analysis_dct_h = dict()
        for key, val in self.word_dct.items():
            self.word_list_h += [val]
        for w in self.readwords:
            word = w.strip()
            if not self.analysis_dct_h.get(word):
                self.analysis_dct_h[word] = dict()
                if not self.analysis_dct_h[word].get('U'):
                    self.analysis_dct_h[word]['U'] = 0
                if not self.analysis_dct_h[word].get('l'):
                    self.analysis_dct_h[word]['l'] = 0
                if not self.analysis_dct_h[word].get('n'):
                    self.analysis_dct_h[word]['n'] = 0
                if not self.analysis_dct_h[word].get('@'):
                    self.analysis_dct_h[word]['@'] = 0
            for char in word:
                if char.isupper():
                    self.analysis_dct_h[word]['U'] += 1
                elif char.isdigit():
                    self.analysis_dct_h[word]['n'] += 1
                elif char.islower():
                    self.analysis_dct_h[word]['l'] += 1
                elif not char.isupper() and not char.islower() and not char.isdigit():
                    self.analysis_dct_h[word]['@'] += 1
        for k,v in self.analysis_dct_h.items():
            print k, v

    def PrefinalAnalysis(self):
        print "\n\n[+]Calculating weights of each char in each word"
        self._charRelationMatrix= dict()
        self.wordweight = dict()
        self.maxweight = 0
        self.cweight = dict()
        for word in self.readwords:
            word = word.strip()
            for i, c in enumerate(word.strip()):
                if not self._charRelationMatrix.get(i):
                    self._charRelationMatrix[i] = dict()
                if not self._charRelationMatrix[i].get(c):
                    self._charRelationMatrix[i][c] = 0
                self._charRelationMatrix[i][c] += 1
        for word in self.readwords:
            word = word.strip()
            if not self.cweight.get(word):
                self.cweight[word] = dict()
            word = word.strip()
            for i, c in enumerate(word):
                if not self.cweight[word].get(c):
                    self.cweight[word][c] = dict()
                if not self.cweight[word][c].get(i):
                    self.cweight[word][c][i] = 0
                self.cweight[word][c][i] += self._charRelationMatrix[i][c]
        for word in self.readwords:
            word = word.strip()
            print word,":",
            for i, c in enumerate(word):
                self.maxweight += self.cweight[word][c][i]
                print "[", c, ":", self.cweight[word][c][i],"]",
            print "MaxWeight = (", self.maxweight, ")", '\n\n'
            self.maxweight = 0

        if not self.wordweight.get(word):
            self.wordweight[word] = dict()
        print "[+]Gathering weight of character in each index\n"
        for k,v in self._charRelationMatrix.items():
            print k, sorted(v.items(), key=lambda x: x[1], reverse=True), '\n\n'

    def charswithfriendswithwords(self):
        print "\n\n[+]Gathering relationship between each finalcharset and each word it was found in with their positions"
        self.charRelationMatrix= dict()
        for word in self.readwords:
            word = word.strip()
            self.charRelationMatrix[word]= dict()
            for i, c in enumerate(word):
                if not self.charRelationMatrix[word].get(c):
                    self.charRelationMatrix[word][c] = dict()
                    self.charRelationMatrix[word][c] = ([z for z,l in enumerate(word) if l == c])
        for k,v in self.charRelationMatrix.items():
            print "\"%s\""%k,"=",len(v)," values",v,"\n\n"

    def smartGenerator(self):
        self.maxweight = 0
        genIndex = list(range(len(max(self.readwords, key=len).strip())))
        self.smartDict = dict()
        self.strippedReadWords = []
        self.genList = ["" for i in genIndex]
        for word in self.readwords:
            word = word.strip()
            for i,c in enumerate(word):
                if not self.smartDict.get(c):
                    self.smartDict[c] = dict()
                if not self.smartDict[c].get(i):
                    self.smartDict[c][i] = dict()
                for ind, ch in enumerate(word):
                    if not self.smartDict[c][i].get(ind):
                        self.smartDict[c][i][ind] = set()
                    self.smartDict[c][i][ind].add(ch)
        indx = random.choice(genIndex)
        genIndex.remove(indx)
        self.genList[indx] = random.choice(self._charRelationMatrix[indx].keys())
        while genIndex:
            indx = random.choice(genIndex)
            randomC = random.choice(self._charRelationMatrix[indx].keys())
            for i, c in enumerate(self.genList):
                if c:
                    if randomC in self.smartDict[c][i][indx]:
                        self.maxweight += self._charRelationMatrix[indx][randomC]
                        self.genList[indx] = randomC
                        genIndex.remove(indx)
                        break
                    else:
                        break
        for word in self.readwords:
            self.strippedReadWords.append(word.strip())
        if "".join(self.genList) in self.strippedReadWords:
            print "Found word in wordList:", ''.join(self.genList) ,"weight= %d  "%self.maxweight
        else:
            print "Found new word:", ''.join(self.genList) ,"weight= %d  "%self.maxweight
            if "".join(self.genList) not in hosts:
                hosts.append("".join(self.genList))

    def patterngenerator(self):
        self.maxweight = 0
        self.threshold = 0
        self.firstchoice = ""
        genIndex = list(range(len(max(self.readwords, key=len).strip())))
        self.smartDict = dict()
        self.strippedReadWords = []
        self.genList = ["" for i in genIndex]
        self.wordpattern =  self.word_dct.values()
        for word in self.readwords:
            word = word.strip()
            for i,c in enumerate(word):
                if not self.smartDict.get(c):
                    self.smartDict[c] = dict()
                if not self.smartDict[c].get(i):
                    self.smartDict[c][i] = dict()
                for ind, ch in enumerate(word):
                    if not self.smartDict[c][i].get(ind):
                        self.smartDict[c][i][ind] = set()
                    self.smartDict[c][i][ind].add(ch)
        self.randompattern = random.choice(self.wordpattern)
        while not self.firstchoice:
            indx = random.choice(genIndex)
            self.firstchoice = random.choice(self._charRelationMatrix[indx].keys())
            if self.getcase(self.firstchoice)== self.randompattern[indx]:
                genIndex.remove(indx)
                self.genList[indx] = self.firstchoice
            else:
                self.firstchoice = ""
        while genIndex:
            if self.threshold == 1000:
                    return
            self.threshold += 1
            indx = random.choice(genIndex)
            randomC = random.choice(self._charRelationMatrix[indx].keys())
            for i, c in enumerate(self.genList):
                if c:
                    if randomC in self.smartDict[c][i][indx] and (self.getcase(randomC) == self.randompattern[indx]):
                        self.maxweight += self._charRelationMatrix[indx][randomC]
                        self.genList[indx] = randomC
                        genIndex.remove(indx)
                        break
                    else:

                        break
        for word in self.readwords:
            self.strippedReadWords.append(word.strip())
        if "".join(self.genList) in self.strippedReadWords:
            print "Found word in wordList:", ''.join(self.genList) ,"weight= %d  "%self.maxweight
        else:
            print "Found new word:", self.randompattern, ''.join(self.genList) ,"weight= %d  "%self.maxweight
            if "".join(self.genList) not in hosts:
                hosts.append("".join(self.genList))


    def randomgenerator(self):
        print "[+] Here are your new strings:(from random generator)\n"
        self.tokens = []
        self.newWord = []
        self.maxweight = 0
        self.genWord = ''
        self.strippedReadWords = []
        self.counter = 0
        for word in self.readwords:
            self.strippedReadWords.append(word.strip())
        while(True):
            self.counter +=1
            if self.counter == int(argv[2]):
                break
            self.genWord = ''
            for i in range(len(self.unusedindexes)):
                self.genWord += (random.choice(self._charRelationMatrix[i].keys()))
            if self.genWord in self.strippedReadWords:
                print "Found word:", self.genWord
            else:
                self.newWord.append(self.genWord)
        for word in self.newWord:
            hosts.append(word)
            print word,
            for i, c in enumerate(word):
                self.maxweight += self._charRelationMatrix[i][c]
            print "MaxWeight = (", self.maxweight, ")", '\n\n'
            self.maxweight = 0


    def customize(self):
        print "[+]Current supported methods"
        print "md5, sha1, sha224, sha256, sha384, sha512, base64\n"
        selection = raw_input("Your choice: ")
        if selection.strip()  == "base64":
            for i in hosts:
                customizedList.append(base64.b64encode(i))
        elif selection.strip() == "sha224":
            for i in hosts:
                customizedList.append(hashlib.sha224(i).hexdigest())
        elif selection.strip() == "sha256":
            for i in hosts:
                customizedList.append(hashlib.sha256(i).hexdigest())
        elif selection.strip() == "sha384":
            for i in hosts:
                customizedList.append(hashlib.sha384(i).hexdigest())
        elif selection.strip() == "sha512":
            for i in hosts:
                customizedList.append(hashlib.sha384(i).hexdigest())
        elif selection.strip() == "sha1":
            for i in hosts:
                customizedList.append(hashlib.sha1(i).hexdigest())
        elif selection.strip() == "md5":
            for i in hosts:
                md5sum = hashlib.md5()
                md5sum.update(i)
                customizedList.append(md5sum.hexdigest())

    def biggerlist(self):
        q = raw_input("do you want to join both lists?[Y/N]")
        if q.lower() == "y":
            print "[-] Using the merged list for all possible regex matches\n"
            z = hosts + self.readwords
            z = list(set(z))
            return z
        elif len(hosts)>=len(self.readwords):
            print "[-] Using the generated list, a possibility of a regex match is greater\n"
            return hosts
        elif len(hosts)<=len(self.readwords):
            print "[-] Using the original list, a possibility of a regex match is greater\n"
            return self.readwords

    def random_regex_generator(self):
        print "[+] Generating a list of all possible regular expressions."
        z = ""
        self.finalcasesregex = list()
        self.separated_charset = dict()
        self.build_regex = dict()
        regexlist = list()
        self.separated_charset["upper"] = ""
        self.separated_charset["lower"] = ""
        self.separated_charset["number"] = ""
        self.separated_charset["symbol"] = ""
        for i in self.analysis_dct_h:
            for q in i:
                z+= self.getcase(q)
            self.finalcasesregex.append(z.strip())
            z= ""
        self.finalcasesregex = list(set(self.finalcasesregex))
        for i in self.finalcharset:
            if self.getcase(i) == "U":
                self.separated_charset["upper"] += i.strip()
            elif self.getcase(i) == "l":
                self.separated_charset["lower"] += i.strip()
            elif self.getcase(i) == "n":
                self.separated_charset["number"] += i.strip()
            elif self.getcase(i) == "@":
                self.separated_charset["symbol"] += i.strip()
        upperregex = "["+''.join([i for i in self.separated_charset["upper"]]).replace("","|")[1:-1]+"]"
        lowerregex = "["+''.join([i for i in self.separated_charset["lower"]]).replace("","|")[1:-1]+"]"
        numregex = "["+''.join([i for i in self.separated_charset["number"]]).replace("","|")[1:-1]+"]"
        symbolregex = "["+''.join([i for i in self.separated_charset["symbol"]]).replace("","|")[1:-1]+"]"
        for i,j in enumerate(self.biggerlist()):
            self.build_regex[i] = ""
            for char in j.strip():
                if self.getcase(char) == "U":
                    self.build_regex[i] += upperregex
                elif self.getcase(char) == "l":
                    self.build_regex[i] += lowerregex
                elif self.getcase(char) == "n":
                    self.build_regex[i] += numregex
                elif self.getcase(char) == "@":
                    self.build_regex[i] += symbolregex
        for v in self.build_regex.values():
            regexlist.append(v)
        regexlist = list(set(regexlist))

        ##Test case
        for i in regexlist:
                for z in self.readwords: #change to hosts instead of self.readwords if you generate more than 200 urls from urls.txt
                    q = re.findall(i,z.strip())
                    if len(q) == 1:
                        print q," : Matched : ",i

    def printgeneralstats(self):
        print "\n\n[+]General Statistics"
        print "Full charset                :",''.join(sorted(self.fullkeyboard))
        print "Discarded charset           :",''.join(sorted(self.discardedcharset))
        print "Final charset               :", ''.join(sorted(self.finalcharset))
        print "Word Length                 :",len(self.unusedindexes)
        print "PreAnalysis Max Combinations:",self.maxcombinationwordsgenerator
        print "Lower Case index usage      : %d%%"%(100 * len(self.alphalowerindexes)/len(self.unusedindexes))
        print "Lower Case index locations  :",sorted(self.alphalowerindexes)
        print "Upper Case index usage      : %d%%"%(100 * len(self.alphaupperindexes)/len(self.unusedindexes))
        print "Upper Case index locations  :",sorted(self.alphaupperindexes)
        print "Digit index usage           : %d%%"%(100 * len(self.integerindexes)/len(self.unusedindexes))
        print "Digit index locations       :",sorted(self.integerindexes)
        print "NonAN index usage           : %d%%"%(100 * len(self.nonalphanumindexes)/len(self.unusedindexes))
        print "NonAN index locations       :",sorted(self.nonalphanumindexes)
        print "Counter statistics          : Uppercase: %d , Lowercase: %d, Digits:%d , NonAlphaNumeric:%d" %(self.countUpper ,self.countLower ,self.countDigits , self.countOther)
        print "All char Frequencies        : (\'Found Character\'  Repeated How many Times)"
        for i in (str(sorted(self.frequencies.items(), key=lambda x: x[1])).replace("[","").replace("]","").split(",")):
            print i.strip(),
            if self.pppc == 10:
                print "\n"
                self.pppc = 0
            self.pppc += 1


if __name__ == '__main__':
    print """
 ______           _           _     _ _  _
(_____ \         | |         | |   (_) |(_)  _
 _____) )___ ___ | |__  _____| |__  _| | _ _| |_ _   _
|  ____/ ___) _ \|  _ \(____ |  _ \| | || (_   _) | | |
| |   | |  | |_| | |_) ) ___ | |_) ) | || | | |_| |_| |
|_|   |_|   \___/|____/\_____|____/|_|\_)_|  \__)\__  |
           Efficient Dynamic Algorithms         (____/
         Ehab Hussein & Ahmed AbdelRahman
"""
    if len(argv) <4 :
        print"""
        Usages:
        $ pypy EDAP.py input-file.txt <number of generated hashes> random   [truly random based on charset , length , chars found] [unstrict]
        $ pypy EDAP.py input-file.txt <number of generated hashes> smart    [based on input , weight & positions] [strict]
        $ pypy EDAP.py input-file.txt <number of generated hashes> patterns [based on smart + char cases] [very strict]
        """
        exit()

    EDA = Probability()
    EDA.getcharset()
    EDA.getindexes()
    EDA.printgeneralstats()
    EDA.frequency_index_vertical()
    EDA.frequency_index_horizontal()
    EDA.charswithfriendswithwords()
    EDA.PrefinalAnalysis()
    if argv[3] == "smart":
        print "[+] Here are your new strings:(from smart generator)\n"
        for i in range(int(argv[2])):
            EDA.smartGenerator()
    if argv[3] == "patterns":
        print "[+] Here are your new strings:(from pattern  smart based generator)\n"
        for i in range(int(argv[2])):
            EDA.patterngenerator()
    if argv[3] == "random":
        EDA.randomgenerator()
    hosts = list(set(hosts))
    print "generated:%d\n\n\n\n\n"%(len(hosts))
    print '\n'.join(hosts),"\n\n"
    try:
        if argv[4] == "custom":
         EDA.customize()
         print '\n'.join(customizedList)
    except Exception,e:
        pass
    EDA.random_regex_generator()
