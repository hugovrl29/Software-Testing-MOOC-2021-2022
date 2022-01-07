#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import time
import random
import math
import os

#---------------------configuration-------------------
 

FuzzFactor = 10
nb_tests = 100
nb_crash = 0
fuzz_output= "/home/inno/Documents/mooc/8/fuzzer/results/output.py"
list_files = ["/home/inno/Documents/mooc/test1.py","/home/inno/Documents/mooc/test2.py"]
list_apps =['/usr/bin/python3']
crash_dico = {}
#-------------------------------------------------------


for test in range(nb_tests):
        

    file = random.choice(list_files)
    fh = open(file, 'rb')
    buf = bytearray(fh.read())
    fh.close()
    app = random.choice(list_apps)

    ## 5 line Miller fuzzer
    numwrites = random.randrange(math.ceil((float(len(buf)) / FuzzFactor))) + 1
    asciint_begin = 48
    asciint_end = 57
    for j in range(numwrites):
        
        rbyte = random.randrange(asciint_begin,asciint_end) #rbyte containt integers bytes, based on Ascii table
        rn = random.randrange(len(buf))
        
        if (buf[rn]  >= asciint_begin) and (buf[rn] <= asciint_end): #only number are fuzz
            buf[rn] = rbyte 

    # end Miller fuzzer
    
    file = open(fuzz_output, 'wb')
    
    file.write(str(buf))
    file.close()
    
    #file = random.choice(list_files)

    assert (open(fuzz_output).read() == str(buf))

    process = subprocess.Popen([app,fuzz_output])

    time.sleep(1)

    crashed = process.poll()

    if not crashed:
        print("sucess")
        #process.terminate()
    else:
        print("it's a crashed")
        nb_crash += 1
        crash_dico["crash_"+str(nb_crash)] = buf

if nb_crash == 0 :
    print('All tests are done without any crashes')
else:
    print("There are %d percents of successes and %d percents of crashes" % ((((nb_tests-nb_crash)*100)//nb_tests),((nb_crash*100)//nb_tests)))
    #print(crash_dico)

    print("%d files crashed" % nb_crash)
    print("%d files success" % (nb_tests - nb_crash))
