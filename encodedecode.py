str=input("Enter a string: ")   # taking input
words=str.split(" ")    # string split function to a list 
print(words)  
coding=input("Enter 1 for encoding and 0 for decoding: ")
coding =True if coding=="1" else False   # short hand if else statement
if (coding):       # encoding step if 1 / True  ,  if/else structure
    nwords=[]   
    for word in words:    # for loop 
        if len(word)>=3:     
            r1="dfg"
            r2="rth"
            str=r1+word[1:]+word[0]+r2     # string slicing and concatenation      
            nwords.append(str)  # list operation , adds at the end
        else:
            nwords.append(word[::-1])     # appends at the end in the list
    print(" ".join(nwords))     # string method which converts and joins the list to a string using " " in between
else:    #decoding step if user enters 0 for decoding
    nwords=[]
    for word in words:   # for loop
        if len(word)>=3:
            strnew= word[3:-3]
            strnew= strnew[-1]+strnew[:-1]
            nwords.append(strnew)      
        else:
            nwords.append(word[::-1]) 
    print(" ".join(nwords))
               

