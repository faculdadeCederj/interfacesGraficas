#! usr/bin/env python
# coding: UTF-8
#
## @package DNAStrandTest
#
# Class for testing the DNAStrand matching.
#
# @author William Souza
# @since 05/02/2020
#
#

import sys
import unittest
import DNAStrand

##
# Class for testing certain aspects of the behavior of
# DNAStrand.
# This class tests all DNAStrand methods with different inputs,
# and prints OK if the class passes all the tests.
class DNAStrandTest(unittest.TestCase):
    ##
     # Two DNAStrand objects to be used in the tests.
     #
    d1 = DNAStrand.DNAStrand('TCAT')
    
    ## DNAStrand object to be used in the tests.
    d2 = DNAStrand.DNAStrand('AGAGCAT')

    ##
     # Test for isValid method, should return a boolean indicating
     # if the string given has only valid chars for
     #  the strand (true) ou not (false).
     # Two strands where tested, both with valid outputs.
    def test_isValid(self):
        msg = 'isValid() should return the given boolean'
        self.assertEqual(self.d1.isValid(), True, msg)
        self.assertEqual(self.d2.isValid(), True, msg)

    ##
     # Test for createComplement method, should return a string with 
     # the complement (all char matching with the given strand).
     # Two strands where tested expecting correct complements.
    def test_createComplement(self):
        msg = 'createComplement() should return a string with the strand complement'
        self.assertEqual(self.d1.createComplement().strand, 'AGTA', msg)
        self.assertEqual(self.d2.createComplement().strand, 'TCTCGTA', msg)

    ##
     # Test for findMatchesWithLeftShift method, should return a string with the
     # matching chars in uppercase and the non-matching in lowercase, when the 'other'
     # strand is shifted left.
     # One relation between strands was tested, with different shift values, 
     # looking towards negative indexes, 0 index and positive.
    def test_findMatchesWithLeftShift(self):
        msg = 'findMatchesWithLeftShift() should return a string with the matches in uppercase'
        self.assertEqual(self.d1.findMatchesWithLeftShift(self.d2, -10), '', msg)
        self.assertEqual(self.d1.findMatchesWithLeftShift(self.d2, -1), '', msg)
        self.assertEqual(self.d1.findMatchesWithLeftShift(self.d2, 0), 'TCat', msg)
        self.assertEqual(self.d1.findMatchesWithLeftShift(self.d2, 1), 'tcat', msg)
        self.assertEqual(self.d1.findMatchesWithLeftShift(self.d2, 2), 'TCaT', msg)
        self.assertEqual(self.d1.findMatchesWithLeftShift(self.d2, 10), 'tcat', msg)

    ##
     # Test for findMatchesWithRightShift method, should return a string with the
     # matching chars in uppercase and the non-matching in lowercase, when the 'other'
     # strand is shifted right
     # One relation between strands was tested, with different shift values, 
     # looking towards negative indexes, 0 index and positive.     
    def test_findMatchesWithRightShift(self):
        msg = 'findMatchesWithRightShift() should return a string with the matches in uppercase'
        self.assertEqual(self.d1.findMatchesWithRightShift(self.d2, -10), '', msg)
        self.assertEqual(self.d1.findMatchesWithRightShift(self.d2, -1), '', msg)
        self.assertEqual(self.d1.findMatchesWithRightShift(self.d2, 0), 'TCat', msg)
        self.assertEqual(self.d1.findMatchesWithRightShift(self.d2, 1), 'tcaT', msg)
        self.assertEqual(self.d1.findMatchesWithRightShift(self.d2, 2), 'tcat', msg)
        self.assertEqual(self.d1.findMatchesWithRightShift(self.d2, 10), 'tcat', msg)

    ##
     # Test for findMaxPossibleMatches method, should return an integer representing
     # the maximum number of matches, independent of how many shifts are made with the 
     # strands.
     # One test was made, with the two strands given.
    def test_findMaxPossibleMatches(self):
        msg = 'findMaxPossibleMatches() should return an int with max possible matches'
        self.assertEqual(self.d1.findMaxPossibleMatches(self.d2), 3, msg)

    ##
     # Test for countMatchesWithLeftShift method, should return an integer representing
     # the number of matches between the strands, when other is shifted left.
     # One relation between strands was tested, with different shift values, 
     # looking towards negative indexes, 0 index and positive.  
    def test_countMatchesWithLeftShift(self):
        msg = 'countMatchesWithLeftShift() should return an int with the matches when other is shifted left'
        self.assertEqual(self.d1.countMatchesWithLeftShift(self.d2, -10), 0, msg)
        self.assertEqual(self.d1.countMatchesWithLeftShift(self.d2, -1), 0, msg)
        self.assertEqual(self.d1.countMatchesWithLeftShift(self.d2, 0), 2, msg)
        self.assertEqual(self.d1.countMatchesWithLeftShift(self.d2, 1), 0, msg)
        self.assertEqual(self.d1.countMatchesWithLeftShift(self.d2, 2), 3, msg)
        self.assertEqual(self.d1.countMatchesWithLeftShift(self.d2, 10), 0, msg)

    ##
     # Test for countMatchesWithRightShift method, should return an integer representing
     # the number of matches between the strands, when other is shifted right.
     # One relation between strands was tested, with different shift values, 
     # looking towards negative indexes, 0 index and positive.  
    def test_countMatchesWithRightShift(self):
        msg = 'countMatchesWithRightShift() should return an int with the matches when other is shifted right'
        self.assertEqual(self.d1.countMatchesWithRightShift(self.d2, -10), 0, msg)
        self.assertEqual(self.d1.countMatchesWithRightShift(self.d2, -1), 0, msg)
        self.assertEqual(self.d1.countMatchesWithRightShift(self.d2, 0), 2, msg)
        self.assertEqual(self.d1.countMatchesWithRightShift(self.d2, 1), 1, msg)
        self.assertEqual(self.d1.countMatchesWithRightShift(self.d2, 2), 0, msg)
        self.assertEqual(self.d1.countMatchesWithRightShift(self.d2, 10), 0, msg)
    ##
     # Test for letterCount method, should return an integer representing the number of
     # times the given character appears in the strand.
     # Were tested uppercase, lowercase and invalid letters.
    def test_letterCount(self):
        msg = 'letterCount() should return an int representing the number of occurrences of the given character \
                in the string'
        self.assertEqual(self.d1.letterCount('A'), 1, msg)
        self.assertEqual(self.d1.letterCount('a'), 1, msg)
        self.assertEqual(self.d2.letterCount('a'), 3, msg)
        self.assertEqual(self.d1.letterCount('f'), 0, msg)
        self.assertEqual(self.d1.letterCount('Y'), 0, msg)
        

    ##
     # Test for matches method, should return true if characters given matches 
     # and false if not.
     # Where tested uppercase, lowercase, valid and invalid characters.
    def test_matches(self):
        msg = 'matches() should return a boolean True if the ch given matches, and False if not'
        self.assertEqual(self.d1.matches('A', 'T'), True, msg)
        self.assertEqual(self.d1.matches('A', 't'), True, msg)
        self.assertEqual(self.d1.matches('A', 'z'), False, msg)
        self.assertEqual(self.d1.matches('A', 'Z'), False, msg)
        self.assertEqual(self.d1.matches('a', 'T'), True, msg)
        self.assertEqual(self.d1.matches('a', 't'), True, msg)
        self.assertEqual(self.d1.matches('a', 'z'), False, msg)
        self.assertEqual(self.d1.matches('a', 'Z'), False, msg)

        self.assertEqual(self.d1.matches('T', 'A'), True, msg)
        self.assertEqual(self.d1.matches('t', 'A'), True, msg)
        self.assertEqual(self.d1.matches('z', 'A'), False, msg)
        self.assertEqual(self.d1.matches('Z', 'A'), False, msg)
        self.assertEqual(self.d1.matches('T', 'a'), True, msg)
        self.assertEqual(self.d1.matches('t', 'a'), True, msg)
        self.assertEqual(self.d1.matches('z', 'a'), False, msg)
        self.assertEqual(self.d1.matches('Z', 'a'), False, msg)


if __name__ == '__main__':
    unittest.main()

