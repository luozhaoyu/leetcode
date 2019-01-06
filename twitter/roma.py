#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    roma.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""
def romanizer(l):
    result = []
    for i in l:
        res = []
        hundreds = i / 100
        tens = i % 100 / 10
        ones = i % 10
        if hundreds == 9:
            res.append('CM')
        elif hundreds >= 5:
            res.append('D' + 'C' * (hundreds - 5))
        elif hundreds == 4:
            res.append('CD')
        else:
            res.append(hundreds * 'C')

        if tens == 9:
            res.append('XC')
        elif tens >= 5:
            res.append('L' + 'X' * (tens - 5))
        elif tens == 4:
            res.append('XL')
        else:
            res.append(tens * 'X')

        if ones == 9:
            res.append('IX')
        elif ones >= 5:
            res.append('V' + 'I' * (ones - 5))
        elif ones == 4:
            res.append('IV')
        else:
            res.append(ones * 'I')
        res = ''.join(res).strip()
        result.append(res)
    return result


def main(argv):
    print romanizer([1, 3, 10, 40, 101])




if __name__ == '__main__':
    import sys
    main(sys.argv)
