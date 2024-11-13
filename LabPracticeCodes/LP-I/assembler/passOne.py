'''
This assembler does not handle following:
    Instructions: BC, CMP
    Pointers: Pointers which are not declared'''

from mnemonics import IS,AD,DL

# Symbol table and literal table
SYMBOL = {}
LITERAL = {}


#Source Code File opening and reading
f = open("sourceCode.txt")
code = []
for line in f:
    line = line.replace(',', '')
    opcodeLine = line.split()
    code.append(opcodeLine)
f.close()



#Assembler Directive Function
def assmeblerDirective(line, word):
    # Location Counter Set
    global lc 
    if (word == "START"):
        try:
            lc = int(line[1]) 
        except (IndexError, ValueError):
            lc = 0     
    elif (word == "END"):
        for lit in LITERAL:
           if(LITERAL[lit]=='notset'):
               LITERAL[lit]= str(lc)
               lc+=1
    elif (word == "LTORG"):
        for lit in LITERAL:
            if(LITERAL[lit]=='notset'):
               LITERAL[lit]= str(lc)
               lc+=1
    elif (word == "ORIGIN"):
        if len(line) == 4 and line[2] == "+":
            symbol = line[1]
            increment = line[3]
            
            if symbol in SYMBOL:
                lc = int(SYMBOL[symbol]) 
            else:
                print("Symbol not found in SYMBOL table")
                return   
            try:
                increment_value = int(increment)
                lc += increment_value
            except ValueError:
                print("Increment value is not a valid number")
                return
        else:
            print("Invalid ORIGIN format")
            return
    elif (word == "EQU"):
        SYMBOL[line[0]] = SYMBOL[line[2]]       
                           
#Declarative Statements Function               
def declarativeStatement(line, word):       
    global lc
    for w in line: 
        if w.isdigit() == False and w not in DL:
            SYMBOL[w] = str(lc)            
    if (word == "DS"):
        if line[2].isdigit():
            lc+= int(line[2])   
        
# Intermediate code file
f1 = open("intermediateCode.txt", "w")


# PASS 1
for line in code:
    #f1.write(str(lc) + "\t")  
    for word in line:
        if word in IS:
            lc += 1
            f1.write("\t" + IS[word] + " ")
        elif word in AD:
            assmeblerDirective(line, word)
            f1.write("\t" + AD[word]+ " ")
        elif word in DL:
            declarativeStatement(line, word)
            lc+= 1
            f1.write("\t" + DL[word] + " ")
        elif ("='" in word):
            LITERAL[word] = 'notset' 
            f1.write(word + " ")       
        elif word.isdigit() and word in ['+'] == False: 
            if word not in SYMBOL:
             SYMBOL[word] = 'notset'
            f1.write(word + " ")        
        else: 
            f1.write(word + " ")          
    f1.write("\n")        


f1.close()
print(f'The location counter is {lc}')
print(SYMBOL)
print(LITERAL)
           
    