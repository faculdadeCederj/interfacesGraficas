#!/usr/bin/env python
# coding: UTF-8
#
## @package DNAStrand
#
#   Playing with string matching.
#
#   @author Paulo Roma (structure, class, methods and main), William Souza (implementations, besides main)
#   @since 15/12/2019
#   @see https://www.sciencedirect.com/topics/medicine-and-dentistry/dna-strand
#
import sys


## 
# Class that implements a simple model of a DNA Strand, with a sequence of
# characters 'A', 'G', 'C', 'T'. 'A' char corresponds to 'T', and 'C' char to 'G',
# those chars form a base pair each. All the methods within this class are used
# for the manipulation and study of the DNAStrands. 
class DNAStrand:

    ## Valid DNA symbols.
    __symbols = 'ATCG'

    ##
    # Constructs a DNAStrand with the given string of data, 
    # normally consisting of characters 'A', 'C', 'G', and 'T'.
    # Raises a ValueError exception, in case of an invalid givenData strand.
    #
    # @param givenData string of characters for this DNAStrand.
    #
    def __init__(self, givenData):
        ## Strand of this DNA, in upper case.
        self.strand = givenData.upper()

        ## Test if the givenData is a valid strand and raises ValueError if is not
        if not self.isValid():
            raise ValueError



    ## Returns a string representing the strand data of this DNAStrand.
    def __str__(self):
        return self.strand


    ##
    # Returns a new DNAStrand that is the complement of this one,
    # that is, 'A' is replaced with 'T' and so on.
    #
    # @return complement of this DNA.
    #
    def createComplement(self):
        complement = ""

        for mol in self.strand:
            if mol == 'A':
                complement += 'T'
            elif mol == 'T':
                complement += 'A'
            elif mol == 'C':
                complement += 'G'
            else:
                complement += 'C'
        
        return DNAStrand(complement)
    

    ##
    # Returns a string showing which characters in this strand are matched with 'other', 
    # when shifted left by the given amount.
    #
    # @param other given DNAStrand.
    # @param shift number of positions to shift other to the left.
    # @return a copy of this strand, where matched characters are upper case and unmatched, lower case.
    #
    def findMatchesWithLeftShift(self, other, shift):
        matches = ''

        ## if shift is a negative value return an empty string
        if shift < 0:
            return matches

        ## adjust the strands len to use in for loop 
        shifted_strand = other.strand
        original_strand_len = len(self.strand)
        shifted_strand_len = len(shifted_strand)

        while shifted_strand_len < original_strand_len + shift:
            shifted_strand += ' '
            shifted_strand_len = len(shifted_strand)


        ## compare the strands and include the matching chars in uppercase
        # and the not matching in lowercase
        for index in range(original_strand_len):
            if self.matches(self.strand[index], shifted_strand[index + shift]):
                matches += self.strand[index]
            else:
                matches += self.strand[index].lower()

        return matches
    

    ##
    # Returns a string showing which characters in this strand are matched with 'other',
    # when shifted right by the given amount.
    #
    # @param other given DNAStrand.
    # @param shift number of positions to shift other to the right.
    # @return a copy of this strand, where matched characters are upper case and unmatched, lower case.
    #
    def findMatchesWithRightShift(self, other, shift):
        matches = ''

        ## if shift is a negative value return an empty string
        if shift < 0:
            return matches

        ## adjust the strands len to use in for loop 
        shifted_strand = ' ' * shift + other.strand
        original_strand_len = len(self.strand)
        shifted_strand_len = len(shifted_strand)

        while shifted_strand_len < original_strand_len + shift:
            shifted_strand += ' '
            shifted_strand_len = len(shifted_strand)

        

        ## compare the strands and include the matching chars in uppercase
        # and the not matching in lowercase 
        for index in range(original_strand_len):
            if self.matches(self.strand[index], shifted_strand[index]):
                matches += self.strand[index]
            else:
                matches += self.strand[index].lower()

        
        return matches
    

    ##
    # Returns the maximum possible number of matching base pairs,
    # when the given sequence is shifted left or right by any amount.
    #
    # @param other given DNAStrand to be matched with this one.
    # @return maximum number of matching pairs.
    #
    def findMaxPossibleMatches(self, other):
        COUNT = 0

        strand_len = len(self.strand)
        other_len = len(other.strand)

        ## getting the max matching with left shift
        for shift in range(other_len - 1):
            matches = self.countMatchesWithLeftShift(other, shift)
            if matches > COUNT:
                COUNT = matches

        ## getting the max matching between right and left shift
        for shift in range(strand_len - 1):
            matches = self.countMatchesWithRightShift(other, shift)
            if matches > COUNT:
                COUNT = matches
        
        return COUNT
    

    ##
    # Returns the number of matching pairs,
    # when 'other' is shifted to the left by 'shift' positions.
    #
    # @param other given DNAStrand to match with this strand.
    # @param shift number of positions to shift other to the left.
    # @return number of matching pairs.
    #
    def countMatchesWithLeftShift(self, other, shift):
        count = 0

        ## returns the string with matches
        shifted_strand = self.findMatchesWithLeftShift(other, shift)

        ## counts the matches (uppercase letters)
        count = sum(1 for char in shifted_strand if char.isupper())        
        return count
    

    ##
    # Returns the number of matching pairs,
    # when 'other' is shifted to the right by 'shift' positions.
    #
    # @param other given DNAStrand to be matched with this one.
    # @param shift number of positions to shift other to the right.
    # @return number of matching pairs.
    #
    def countMatchesWithRightShift (self, other, shift):
        count = 0

        ## returns the string with matches
        shifted_strand = self.findMatchesWithRightShift(other, shift)

        ## counts the matches (uppercase letters)
        count = sum(1 for char in shifted_strand if char.isupper())        
        
        return count
    

    ##
    # Determines whether all characters in this strand are valid ('A', 'G', 'C', or 'T').
    #
    # @return True if valid, and False otherwise.
    #
    def isValid(self):
        valid = True

        ## Test if the given strand has valid symbols
        for mol in self.strand:
            if mol not in self.__symbols:
                valid = False

        return valid
    

    ##
    # Counts the number of occurrences of the given character in this strand.
    #
    # @param ch given character.
    # @return number of occurrences of ch.
    #
    def letterCount(self,ch):
        count = 0

        for mol in self.strand:
            if ch.upper() == mol:
                count += 1

        return count
    

    ##
    # Returns True if the two characters form a base pair ('A' with 'T' or 'C' with 'G').
    #
    # @param c1 first character.
    # @param c2 second character.
    # @return True if they form a base pair, and False otherwise.
    #
    def matches(self, c1, c2):
        match = False

        if c1 in 'Aa':
            if c2 in 'Tt':
                match = True
        elif c1 in 'Tt':
            if c2 in 'Aa':
                match = True
        elif c1 in 'Cc':
            if c2 in 'Gg':
                match = True
        else:
            if c2 in 'Cc':
                match = True

 
        return match
    
## Main program for testing.
#
# @param args two DNA strands.
#
def main (args=None):

    if args is None:
       args = sys.argv

    if len(args) == 5:
       d = DNAStrand(args[1])
       d2 = DNAStrand(args[2])
       ls = int(args[3])
       rs = int(args[4])
    else:
       d = DNAStrand ("AGAGCAT")
       d2 = DNAStrand ("TCAT")
       ls = 2
       rs = 3

    print("Complement: %s" % d.createComplement()) 
    print("Count A in %s: %d" % (d, d.letterCount('A')))
    print("%s isValid: %r" % (d, d.isValid()))
    print("Strand: %s" % d2)
    print("RightShift: %s, %d = %s" % (d, rs, d2.findMatchesWithRightShift(d,rs)))
    print("Left Shift: %s, %d = %s" % (d, ls, d2.findMatchesWithLeftShift(d,ls)))
    print("Maximum Matches: %d" % d.findMaxPossibleMatches(d2))
    print("Number of matches left shift: %s, %d = %s" % (d2, ls+rs, d.countMatchesWithLeftShift(d2,ls+rs)))

if __name__ == "__main__":
   sys.exit(main())


