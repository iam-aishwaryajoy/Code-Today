class Tester:
    def __init__(self):
        self.inc = 1
        self.result = True

    def test(self, test, out):
        print("Test No:", self.inc)
        print("===========")
        if len(test['input']['data']) <20:
            print("Input:", test['input']['data'])
        print("Expected Output:", test['output'])
        print("Actual Output:", out)

        print("Problem statement:", test['problem'])
        if out == test['output']:
            print("Test result: PASSED")
            self.result = True
        else:
            print("Test result: FAILED")
            self.result = False
        self.inc = self.inc + 1

        print("                             ")
        
