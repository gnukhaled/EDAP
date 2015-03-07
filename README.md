# EDAP
#Efficient Dynamic Algorithms for hash generations and testing
We work on fixed length inputs , the more inputs the better the generations
Usage:

$ python EDAP.py inputfilename.txt number-of-hashes-to-generate


ehabs-MacBook-Pro:OhHaithere obzy$ wc -l test.txt ; head -n 3 test.txt 
     100 test.txt
P91TKwhEHx4
X7Q7mimh4iE
A9g6sYKNlGA
ehabs-MacBook-Pro:OhHaithere obzy$ python EDAP.py test.txt 10

 ______           _           _     _ _  _
(_____ \         | |         | |   (_) |(_)  _
 _____) )___ ___ | |__  _____| |__  _| | _ _| |_ _   _
|  ____/ ___) _ \|  _ \(____ |  _ \| | || (_   _) | | |
| |   | |  | |_| | |_) ) ___ | |_) ) | || | | |_| |_| |
|_|   |_|   \___/|____/\_____|____/|_|\_)_|  \__)\__  |
                                                (____/
         Ehab Hussein & Ahmed AbdelRahman



Keys: {U = Uppercase, l = Lowercase , n = Integers , @ = symbols}

[+] Finding Character types with positions in each word
l | U | U | U | n | l | l | U | U | U | l |  bXNS4rnVSEg
l | l | U | n | U | @ | U | U | U | l | l |  aqD9Z_GGCao
l | l | n | l | l | l | l | l | l | n | l |  fl3wgkztw9s
n | l | n | U | l | U | l | U | U | l | U |  3s2XsDfJBoY
U | U | U | l | n | U | @ | l | U | U | U |  NXMp7Y-dHYM
U | U | U | n | n | l | U | l | U | U | U |  XAN06jBmHYM
n | n | U | l | U | U | l | n | l | n | l |  12PzYIr9n1k
U | l | l | n | l | n | l | l | l | n | n |  Vmz6o6xeq78
l | l | U | U | U | l | U | U | U | l | l |  nzINYgNRRmw
l | U | U | l | l | l | @ | U | U | U | U |  vEMjaq_GZLU
U | U | U | n | l | U | l | U | l | l | U |  KDD1iDnOorE
U | l | l | U | U | U | n | l | U | l | U |  GvrTPM3tMcA
l | l | l | n | l | U | U | U | U | l | l |  hmi9dSKJVuk
U | U | l | n | l | U | U | l | l | l | l |  CDg8zJXrqzw
U | U | n | l | l | U | n | U | U | n | l |  QQ1giM1TB3k


……………….snip
[+]General Statistics
Full charset                : !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
Discarded charset           : !"#$%&'()*+,./:;<=>?@[\]^`{|}~
Final charset               : -0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz
Word Length                 : 11
PreAnalysis Max Combinations: 73786976294838206464
Lower Case index usage      : 100%
Lower Case index locations  : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Upper Case index usage      : 100%
Upper Case index locations  : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Digit index usage           : 100%
Digit index locations       : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NonAN index usage           : 90%
NonAN index locations       : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Counter statistics          : Uppercase: 455 , Lowercase: 446, Digits:168 , NonAlphaNumeric:31
All char Frequencies        : ('Found Character'  Repeated How many Times)
('O' 6) ('5' 9) ('F' 9) ('2' 10) ('p' 10) 

('t' 10) ('C' 11) ('T' 11) ('W' 12) ('b' 12) 

('j' 12) ('3' 13) ('L' 13) ('v' 14) ('z' 14) 

('-' 15) ('7' 15) ('J' 15) ('U' 15) ('a' 15) 

('u' 15) ('1' 16) ('P' 16) ('_' 16) ('c' 16) 

('f' 16) ('l' 16) ('q' 16) ('y' 16) ('x' 16) 

('R' 17) ('e' 17) ('i' 17) ('E' 18) ('D' 18) 

('K' 18) ('V' 18) ('Z' 18) ('S' 19) ('s' 19) 

('6' 20) ('8' 20) ('B' 20) ('G' 20) ('h' 20) 

('k' 20) ('o' 20) ('4' 21) ('9' 21) ('I' 21) 

('N' 21) ('g' 21) ('r' 21) ('A' 22) ('X' 22) 

('d' 22) ('m' 22) ('0' 23) ('M' 23) ('Y' 23) 

('Q' 24) ('n' 24) ('H' 25) ('w' 25) 

[+] Starting frequency with index analysis(vertical)
index:  0 {'@': 4, 'U': 40, 'l': 39, 'n': 17}
index:  1 {'@': 1, 'U': 44, 'l': 36, 'n': 19}
index:  2 {'@': 2, 'U': 53, 'l': 33, 'n': 12}
index:  3 {'@': 4, 'U': 40, 'l': 35, 'n': 21}
index:  4 {'@': 4, 'U': 35, 'l': 48, 'n': 13}
index:  5 {'@': 2, 'U': 39, 'l': 46, 'n': 13}
index:  6 {'@': 5, 'U': 43, 'l': 42, 'n': 10}
index:  7 {'@': 3, 'U': 43, 'l': 43, 'n': 11}
index:  8 {'@': 3, 'U': 40, 'l': 41, 'n': 16}
index:  9 {'@': 3, 'U': 34, 'l': 48, 'n': 15}
index:  10 {'@': 0, 'U': 44, 'l': 35, 'n': 21}

[+] Starting frequency with index analysis(horizontal)
12PzYIr9n1k {'@': 0, 'U': 3, 'l': 4, 'n': 4}
-WowwFJYOi4 {'@': 1, 'U': 5, 'l': 4, 'n': 1}
nGAK-vBraMY {'@': 1, 'U': 6, 'l': 4, 'n': 0}
GVaFN53Gd70 {'@': 0, 'U': 5, 'l': 2, 'n': 4}
68QrxLPXSgc {'@': 0, 'U': 5, 'l': 4, 'n': 2}
CDg8zJXrqzw {'@': 0, 'U': 4, 'l': 6, 'n': 1}
AdV5zir8AaQ {'@': 0, 'U': 4, 'l': 5, 'n': 2}
vkW6QWoCR0I {'@': 0, 'U': 6, 'l': 3, 'n': 2}
 

………………..snip


[+]Gathering relationship between each finalcharset and each word it was found in with their positions
"12PzYIr9n1k" = 10  values {'r': [6], '9': [7], 'I': [5], 'k': [10], 'n': [8], '1': [0, 9], 'P': [2], '2': [1], 'Y': [4], 'z': [3]} 


"-WowwFJYOi4" = 10  values {'W': [1], 'F': [5], 'i': [9], 'J': [6], '-': [0], 'o': [2], 'O': [8], 'w': [3, 4], 'Y': [7], '4': [10]} 


"nGAK-vBraMY" = 11  values {'A': [2], 'a': [8], 'B': [6], 'G': [1], 'M': [9], 'K': [3], '-': [4], 'n': [0], 'r': [7], 'v': [5], 'Y': [10]} 


"GVaFN53Gd70" = 10  values {'a': [2], 'd': [8], 'G': [0, 7], 'F': [3], 'N': [4], '0': [10], '3': [6], '5': [5], '7': [9], 'V': [1]} 


……………………snip


[+]Calculating weights of each char in each word
bXNS4rnVSEg : [ b : 4 ] [ X : 3 ] [ N : 4 ] [ S : 2 ] [ 4 : 1 ] [ r : 1 ] [ n : 3 ] [ V : 2 ] [ S : 4 ] [ E : 2 ] [ g : 5 ] MaxWeight = ( 31 ) 


aqD9Z_GGCao : [ a : 1 ] [ q : 3 ] [ D : 6 ] [ 9 : 5 ] [ Z : 2 ] [ _ : 2 ] [ G : 1 ] [ G : 5 ] [ C : 1 ] [ a : 2 ] [ o : 4 ] MaxWeight = ( 32 ) 


fl3wgkztw9s : [ f : 6 ] [ l : 1 ] [ 3 : 1 ] [ w : 3 ] [ g : 1 ] [ k : 2 ] [ z : 1 ] [ t : 3 ] [ w : 2 ] [ 9 : 1 ] [ s : 6 ] MaxWeight = ( 27 ) 


3s2XsDfJBoY : [ 3 : 4 ] [ s : 1 ] [ 2 : 1 ] [ X : 1 ] [ s : 3 ] [ D : 3 ] [ f : 1 ] [ J : 2 ] [ B : 3 ] [ o : 1 ] [ Y : 7 ] MaxWeight = ( 27 ) 


NXMp7Y-dHYM : [ N : 1 ] [ X : 3 ] [ M : 4 ] [ p : 2 ] [ 7 : 1 ] [ Y : 2 ] [ - : 2 ] [ d : 2 ] [ H : 6 ] [ Y : 2 ] [ M : 5 ] MaxWeight = ( 30 ) 




…………………..snip


[+]Gathering weight of character in each index

0 [('f', 6), ('3', 4), ('6', 4), ('A', 4), ('V', 4), ('b', 4), ('v', 4), ('y', 4), ('-', 3), ('G', 3), ('Q', 3), ('P', 3), ('n', 3), ('1', 2), ('2', 2), ('9', 2), ('8', 2), ('C', 2), ('E', 2), ('H', 2), ('K', 2), ('W', 2), ('Y', 2), ('X', 2), ('Z', 2), ('h', 2), ('m', 2), ('p', 2), ('r', 2), ('7', 1), ('B', 1), ('D', 1), ('J', 1), ('M', 1), ('L', 1), ('O', 1), ('N', 1), ('_', 1), ('a', 1), ('e', 1), ('d', 1), ('g', 1), ('k', 1), ('l', 1), ('q', 1), ('u', 1), ('x', 1), ('z', 1)] 


1 [('9', 5), ('n', 5), ('2', 4), ('H', 4), ('P', 4), ('7', 3), ('A', 3), ('G', 3), ('R', 3), ('W', 3), ('V', 3), ('X', 3), ('d', 3), ('i', 3), ('m', 3), ('q', 3), ('v', 3), ('5', 2), ('4', 2), ('C', 2), ('B', 2), ('D', 2), ('M', 2), ('Q', 2), ('k', 2), ('o', 2), ('t', 2), ('x', 2), ('1', 1), ('6', 1), ('8', 1), ('E', 1), ('F', 1), ('I', 1), ('J', 1), ('L', 1), ('O', 1), ('U', 1), ('Z', 1), ('_', 1), ('g', 1), ('j', 1), ('l', 1), ('p', 1), ('s', 1), ('r', 1), ('u', 1), ('z', 1)] 

…………………..snip

[+] Here are your new strings:(from smart generator)

Found new word: PPwnwFJEWu4 weight= 32  
Found new word: ArV6siTrA-A weight= 28  
Found new word: VnR6HkYe57c weight= 32  
Found new word: b1NStrnV6Eg weight= 21  
Found new word: 9HDO-aj0V8Y weight= 33  
Found new word: KHD1XDnOorE weight= 36  
Found new word: 3mkXsVs4-qo weight= 20  
Found word in wordList: kiMKaEkjTn4 weight= 29  
Found new word: hJatdSbJPuQ weight= 26  
Found word in wordList: nzINYgNRRmw weight= 30  

generated:8

VnR6HkYe57c
KHD1XDnOorE
ArV6siTrA-A
hJatdSbJPuQ
3mkXsVs4-qo
PPwnwFJEWu4
b1NStrnV6Eg
9HDO-aj0V8Y

----------------------------------------
sample uuid4 generation

generated:10
dec4ea81-4883-4c7e-a0cc-60a811fee6c6
a961ee4b-53da-401e-989c-804f57f0612c
de5053d3-f380-4b40-b74f-706e2acb96f8
2715a769-cb12-4a47-a6f8-0f8445cc6241
8344a443-7509-4941-b12e-413854d55eb0
0fc29681-f472-4d7c-9937-354d7595ea40
a44b78ee-9de3-4f84-8034-9573789643ef
14d5ee68-4492-4f31-be44-2384ffe57d1f


———————————————————

sample md5 generation

a1e2a7db29454fc27f5a6b21aac4ef47
a1e20abb984d75c6625560256cc44f7e
058981b1f69c10a9ce7bdfa9cdbb970a
1f21ae66d3d2ed7f4ef8ec4efd617fd0
5ca69b5ebc714706deaab1b7776131dd
1f51ac6647d5ed6ae3a88f4efb2b20de
abc30db5484d75c63395c1256ac3424e
f41ef68daa89f2606d6d7f1f2aa749fd
c81e728d9d4c2f406f067f8cca14862c


——————————
