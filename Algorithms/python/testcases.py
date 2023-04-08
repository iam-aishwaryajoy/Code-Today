class Testcase:
    def __init__(self):
        testcases = []
        testcases.append({'input': {'data': [6,5,4,3,2], 'query':2}, 
                            'output':4,'problem':"Query is last index"})
        testcases.append({'input': {'data': [7,5,3], 'query':7}, 
                            'output':0,'problem':"Query is first index"})
        testcases.append({'input': {'data': [3, -1, -9, -127] , 'query':-1 }, 
                            'output':1 , 'problem':" Query is negative"})
        testcases.append({'input': {'data': [6] , 'query':6 }, 
                            'output':0 , 'problem':" Query is only one element"})
        testcases.append({'input': {'data': [9, 7, 5, 2, -9], 'query':4 }, 
                            'output':-1 , 'problem':" Query is missing"})
        testcases.append({'input': {'data': [], 'query':7 }, 
                            'output':-1 , 'problem':" Data is empty"})
        testcases.append({'input': {'data': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 
                            'query':6 }, 'output': 2, 'problem':" Query is duplicate"})
        testcases.append({'input': {'data': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 
                            'query':3 }, 'output': 7, 'problem':" Query is not duplicate but data is"})
        self.testcase = testcases
        self.large_test = {'input': {'data': list(range(10000000, 0, -1)),
                            'query': 2 },'output': 9999998, 'problem':"Large list"}
