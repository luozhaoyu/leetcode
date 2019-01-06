#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    rmq.py
    ~~~~~~~~~~~~~~

    A brief description goes here.
"""

def main(argv):
    N = 10
    M = 5
    arrs = [10, 20, 30, 40, 11, 22, 33, 44, 15, 5]
    lrs = [[0, 5], [1, 2], [8, 9], [0, 9], [4, 6]]
    def get_segment_tree(arrs, left, right):
        tree = {}
        length = right - left + 1
        if length <= 2:
            tree['min'] = min(arrs[left], arrs[right])
            tree['left'] = left
            tree['right'] = right
        else:
            tree['left_tree'] = get_segment_tree(arrs, left, left+length/2)
            tree['right_tree'] = get_segment_tree(arrs, left+length/2, right)
            tree['left'] = left
            tree['right'] = right
            tree['min'] = min(tree['left_tree']['min'], tree['right_tree']['min'])
        return tree

    def search_segment_tree(tree, left, right):
        print "searching [%d, %d]" % (left, right)
        if left == tree['left'] and right == tree['right']:
            return tree['min']
        else:
            if not tree.has_key['left_tree']:
                return min(tree[left: right])
            else:
                print "\tnot match, this tree is [%d, %d]" % (tree['left'], tree['right'])
                return min(search_segment_tree(tree['left_tree'], left, tree['left_tree']['right']),
                    search_segment_tree(tree['right_tree'], tree['right_tree']['left'], right))

    tree_root = get_segment_tree(arrs, 0, len(arrs)-1)
    print search_segment_tree(tree_root, 0, len(arrs) - 3)


    for i in lrs:
        l, r = i
        tmp = arrs[l: r+1]
        print search_segment_tree(tree_root, l, r)


if __name__ == '__main__':
    import sys
    main(sys.argv)
