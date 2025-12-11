
import sys
from itertools import product

# (0,1,2,3) -> "0123"
def list2str(xs) : return ''.join(map(str, xs))

# "0123" -> [0,1,2,3]
def str2list(s) : return list(map(int, list(s)))

# (123, 4) -> "0123"
def int2str(i, n) : return str(i).zfill(n)

# "6174" -> "6174"
def f(s, n) :
    xs = str2list(s)
    mx = int(list2str(sorted(xs, reverse=True)))
    mn = int(list2str(sorted(xs)))

    return int2str(mx - mn, n)

# compute dictionary d[rep] -> (cycle, elements) of fixpoints
def fixpoints(n) :

    d = {}
    for xs in product(range(10), repeat = n) :
        seq = [] # sequence: s, f(s), f(f(s)), ...

        s = list2str(xs)
        seq.append(s)
        fs = f(s, n)
        while fs not in seq : # while not in a cycle...
            seq.append(fs)
            fs = f(fs, n)

        a = seq.index(fs) # index of first element of cycle

        cyc = sorted(seq[a:]) # clip segment, it's a cycle
        rep = min(cyc) # representative element
        elems = set(seq) # elements in it's "class"
        assert len(elems) == len(seq)

        if rep in d : # update dictionary
            assert cyc == d[rep][0]
            d[rep][1] |= elems
        else :
            d[rep] = [cyc, elems]

    return d

# Main
#----------------------------------------------------------------------

n = int(sys.argv[1]) # number of digits
d = fixpoints(n)

print('rep,cycle,size,elements')
for x in d :
    cyc = ' '.join(d[x][0])
    els = d[x][1]

    print(x, cyc, len(els), ' '.join(sorted(els)[:5])+' ...', sep = ',')
