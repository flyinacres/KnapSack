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
    global _least_remainder
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

        new_total = new_total + _vals[cur]

    return _least_remainder


T = input()

for i in range(0, T):
    n,_target = [int(x) for x in raw_input().split(' ')]
    A = [int(x) for x in raw_input().split(' ')]

    # Convert through a set to ensure only unique values
    _vals = list(set(A))

    _least_remainder = _target
    if increment_all(0, 0) == 0:
        print _target
    else:
        print _target - _least_remainder