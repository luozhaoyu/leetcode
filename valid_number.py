# -*- coding: utf-8 -*-
"""
    valid_number.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""
import re

class Solution:

    # @param s, a string

    # @return a boolean

    def isNumber(self, s):
        s = s.strip().lower()
        if len(s) == 0:
            return False
        if s.count('.') > 1 or s.count('e') > 1:
            return False

        if s.startswith("-") or s.startswith("+"):
            s = s[1:]

        if s.isdigit():
            return True
        elif s.find("e") >= 0:
            front, back = s.split('e')
            #print front, back
            if self.isDecimal(front) and self.isIntegerWithFrontZero(back):
                return True
            else:
                return False
        elif self.isZero(s):
            return True
        else:
            return self.isDecimal(s)

    def isZero(self, s):
        if re.search(r"\.[0]+", s) or re.search(r"[0]\.", s) or s == "0":
            return True
        else:
            return False

    def isIntegerWithFrontZero(self, s):
        if s.startswith('-') or s.startswith('+'):
            s = s[1:]
        if re.search(r"^\d+$", s):
            return True
        else:
            return False

    def isDecimal(self, s):
        if s.startswith('-') or s.startswith('+'):
            s = s[1:]

        if re.search(r"^[0]{0,1}\.\d*[1-9]+\d*$", s):
            return True
        elif re.search(r"^[1-9]\d*\.{0,1}\d*$", s):
            return True
        else:
            return False


def _main(argv):
    s = Solution()
    print s.isNumber("3")
    print s.isNumber("0.1")
    print s.isNumber(".1")
    print s.isNumber(" 0.1")
    print s.isNumber("2e10")
    print -1, s.isNumber("-1")
    print "+1.0", s.isNumber("+1.0")
    print s.isNumber("46.0e7")
    print s.isNumber("46.e7")
    print s.isNumber("3.")
    print s.isNumber(".2e7")
    print s.isNumber(".0")
    print s.isNumber(".00")
    print s.isNumber("01.")
    print s.isNumber("3")

    print s.isNumber("1 a")
    print s.isNumber("abc")
    print s.isNumber("..2")
    print s.isNumber("3..2")
    print s.isNumber("")
    print s.isNumber(".")
    print s.isNumber(".  0e7")
    print s.isNumber(".0e7")
    print s.isNumber(".e7")
    print s.isNumber("e7")
    print s.isNumber("ee")
    print s.isNumber("0..")


if __name__ == '__main__':
    import sys
    _main(sys.argv)
