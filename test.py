## Question 2.2


import unittest
from main import isogram


class MyTestCase(unittest.TestCase):


# This test is to test that an isogram input will return true
def test_is_isogram(self):
else:
print('This is an isogram!')
return True
expected_output = true
self.assertTrue(True, uncopyrightable)


# This test is to test that a non-isogram input will return false


def test_non_isogram(self):
try:
if not word:
print('This is not an isogram')
return False
word = word.lower()
for i in word:
if word.count(i) > 1:
print('This is not an isogram')
return False
word = mississipi
expected_output = false
self.assertFalse(False, mississipi)


if __name__ == '__main__':
unittest.main()
