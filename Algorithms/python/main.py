from algorithms import *
from test import *
import logging as log
import time
from testcases import Testcase

if __name__ == "__main__":
    algorithm = SearchAlgorithm()
    tester = Tester()
    testcases = []
    result = True
    log.basicConfig(filename='Algorithm.log', level=log.DEBUG)

    #testcases = Testcase().testcase 
    #for test in testcases:
        #output = algorithm.binary_search(**test['input'])
        #tester.test(test, output)
        #if tester.result == False:
            #result = False
    
    #if result == True:
        #print("FULL TEST: PASSED")
    #else:
        #print("FULL TEST :FAILED")
    
    large_test = Testcase().large_test
    start_time = time.time()
    output = algorithm.binary_search(**large_test['input'])
    tester.test(large_test, output)
    print("Run time for binary search", (round(time.time() - start_time, 2)), "seconds")

    start_time = time.time()
    output = algorithm.linear_search(**large_test['input'])
    tester.test(large_test, output)
    print("Run time for linear search", (round(time.time() - start_time, 2)), "seconds")
    
