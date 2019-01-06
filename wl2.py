import string



class Word(object):

    def __init__(self, w, length=1):

        self.word = w

        self.previous = None

        self.length = length





def get_possible_str(s):

    res = set([s])

    for i in range(len(s)):

        for j in string.lowercase:

            res.add(s[:i] + j + s[i+1:])

    return res





class Solution:



    # @param start, a string

    # @param end, a string

    # @param dictionary, a set of string

    # @return a list of lists of string

    def findLadders(self, start, end, dictionary):

        ds = set(dictionary)

        ds.add(start)

        ds.add(end)

        words = {start: get_possible_str(start).intersection(ds),

            end: get_possible_str(end).intersection(ds)}

        for i in dictionary:

            words[i] = get_possible_str(i).intersection(ds)



        paths = [Word(start)]

        res = []

        found = -1

        appeared = set()

        while paths:

            w = paths.pop(0)

            if found != -1 and w.length > found:

                break

            #: current neighbors

            can_accesses = words[w.word]

            if end in can_accesses:

                if found == -1:

                    res.append(w)

                    found = w.length

                else:

                    if w.length <= found:

                        res.append(w)

                continue



            appeared.add(w.word)

            promising_words = can_accesses - appeared

            if found == -1:

                for pw in promising_words:

                    new_w = Word(pw, w.length + 1)

                    new_w.previous = w# -*- coding: utf-8 -*-
def _main(argv):
    import time
    s = Solution()
    datas = [["hit", "cog", ["hot","dot","dog","lot","log"]],
        ["a", "c", ["a","b","c"]],
        ["hot", "dog", ["hot","dog"]],
        ["hit", "cog", ["hot","cog","dot","dog","hit", "lot", "log"]],
        ["set", "oar", ["oar","sat","dip","sir","lap","tat","off"]],
        [
"nape", "mild", ["dose","ends","dine","jars","prow","soap","guns","hops","cray","hove","ella","hour","lens","jive","wiry","earl","mara","part","flue","putt","rory","bull","york","ruts","lily","vamp","bask","peer","boat","dens","lyre","jets","wide","rile","boos","down","path","onyx","mows","toke","soto","dork","nape","mans","loin","jots","male","sits","minn","sale","pets","hugo","woke","suds","rugs","vole","warp","mite","pews","lips","pals","nigh","sulk","vice","clod","iowa","gibe","shad","carl","huns","coot","sera","mils","rose","orly","ford","void","time","eloy","risk","veep","reps","dolt","hens","tray","melt","rung","rich","saga","lust","yews","rode","many","cods","rape","last","tile","nosy","take","nope","toni","bank","jock","jody","diss","nips","bake","lima","wore","kins","cult","hart","wuss","tale","sing","lake","bogy","wigs","kari","magi","bass","pent","tost","fops","bags","duns","will","tart","drug","gale","mold","disk","spay","hows","naps","puss","gina","kara","zorn","boll","cams","boas","rave","sets","lego","hays","judy","chap","live","bahs","ohio","nibs","cuts","pups","data","kate","rump","hews","mary","stow","fang","bolt","rues","mesh","mice","rise","rant","dune","jell","laws","jove","bode","sung","nils","vila","mode","hued","cell","fies","swat","wags","nate","wist","honk","goth","told","oise","wail","tels","sore","hunk","mate","luke","tore","bond","bast","vows","ripe","fond","benz","firs","zeds","wary","baas","wins","pair","tags","cost","woes","buns","lend","bops","code","eddy","siva","oops","toed","bale","hutu","jolt","rife","darn","tape","bold","cope","cake","wisp","vats","wave","hems","bill","cord","pert","type","kroc","ucla","albs","yoko","silt","pock","drub","puny","fads","mull","pray","mole","talc","east","slay","jamb","mill","dung","jack","lynx","nome","leos","lade","sana","tike","cali","toge","pled","mile","mass","leon","sloe","lube","kans","cory","burs","race","toss","mild","tops","maze","city","sadr","bays","poet","volt","laze","gold","zuni","shea","gags","fist","ping","pope","cora","yaks","cosy","foci","plan","colo","hume","yowl","craw","pied","toga","lobs","love","lode","duds","bled","juts","gabs","fink","rock","pant","wipe","pele","suez","nina","ring","okra","warm","lyle","gape","bead","lead","jane","oink","ware","zibo","inns","mope","hang","made","fobs","gamy","fort","peak","gill","dino","dina","tier"]

],

        ]

    for start, end, d in datas:
        begin = time.time()
        print start, end, len(d)
        print s.findLadders(start, end, d)
        end = time.time()
        print end - begin

if __name__ == '__main__':
    import sys
    _main(sys.argv)
