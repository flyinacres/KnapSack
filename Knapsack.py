__author__ = 'rfischer'


# _least_remainder is the smallest remainder found to this point
_least_remainder = 0
# _vals is a list of values--use cur to access the correct one
_vals = ()
# _max_multiples is the max number of times the current value can go into the target value
_max_multiples = ()
# _target is the value that we are trying to reach
_target = 100

# total_val is the total of all higher recurses
# cur is the index of the current value/multiple
def increment_all(total_val, cur):
    new_total = total_val
    while new_total <= _target:
        if new_total == _target:
            return 0
        elif _target - new_total < _least_remainder:
            _least_remainder = _target - new_total

        # Only care about the return if it is an exact match
        # Otherwise _least_remainder may be updated but we must continue checking
        if cur + 1 < len(_vals):
            if increment_all(new_total, cur+1) == 0:
                return 0

        new_total = total_val + _vals[cur]

    return _least_remainder

def expected_sum(s, k):
    # Handle exact matches and all too large
    smaller = 0
    remainders = set()
    for e in s:
        z = k%e
        remainders.add(z)
        if not z:
            return k
        if e < k:
            smaller = 1


    if not smaller:
        return 0

    best_remainder = min(list(remainders))

    # Get possible best solutions when remainder is modulo another value (nx + my = k)
    for e in remainders:
        for f in s:
            if not e%f:
                return k

    # Perhaps multiple  numbers add to a good result
    t = sorted(list(s), reverse=True)
    w = [0]*len(t)
    # get the sum of the weighted values
    test = sum([a*b for a,b in zip(t,w)])
    if test == k:
        return k
    if 0 < k - test < best_remainder:
        best_remainder = k - test
    # if test > k:
    #    stop current weight, reset it, and move to next attempt

    # go to next weight in current set

    # is less than k then check for mininu increase the next weight
    # else
    print "test is " + str(test)
    for e in t:
        for f in s:
            if 0 < k - (e + f) < best_remainder:
                best_remainder = k - (e + f)

    return k - best_remainder




T = input()

for i in range(0, T):
    n,_k = [int(x) for x in raw_input().split(' ')]
    A = [int(x) for x in raw_input().split(' ')]
    _s = set()
    _s.update(A)

    print expected_sum(_s, _k)





