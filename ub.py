#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Brief Summary
Attributes:

Google Python Style Guide:
    http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
"""
__copyright__ = "Zhaoyu Luo"



def find_friends(user_id):
    pass


class Friend(object):
    def __init__(self, name, mutual=1):
        self.name = name
        self.mutual = mutual


class Heap(object):
    def insert(friend):
        pass

    def pop(self):
        pass


def insert_heap(min_heap, friend):
    if not min_heap:
        min_heap.append(friend)
        return min_heap

    current_index = min_heap[0]
    while True:



def find_top_k_frineds(user_id):
    layer_1_friends = find_friends(user_id)
    layer_2_friends = {}
    min_heap = Heap()
    for friend in layer_1_friends:
        user_id = friend.user_id
        if friend in layer_2_friends:
            layer_1_friends[friend].mutal += 1
        else:
            friend.mutual = 1
            layer_1_friends[friend] = friend
            min_heap.insert(friend)

    res = []
    # TODO: find top k
    for i in range(k):
        res.append(min_heap.pop())



def main():
    """Main function only in command line"""
    from sys import argv



if __name__ == '__main__':
    main()
