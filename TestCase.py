import unittest
from unittest.mock import patch
from Problem1 import answer
from io import StringIO

def get_input(caseId):
    filename = 'testdata/testcase' + str(caseId) + 'input.txt'            
    data = []
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        for item in lines:
            data.append(item)
    return iter(data).__next__
    
def get_output(caseId):
    filename = 'testdata/testcase' + str(caseId) + 'output.txt'
    with open(filename, 'r') as f:
        return ''.join(f.readlines()) + '\n'

class Problem1UnitTest(unittest.TestCase):
    @patch("builtins.input", get_input(0))
    @patch('sys.stdout', new_callable = StringIO)
    def test_case_0(self, stdout):
        answer()
        self.assertEqual(stdout.getvalue(), get_output(0))

if __name__ == '__main__':
    unittest.main()