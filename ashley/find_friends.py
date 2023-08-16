#!/usr/bin/python

sin_addr = dict()

# Open the dump
with open("sorted_email.txt", "r") as f:
    key = "zz"
    # Parse the dump line by line
    for addr in f:
        # When the first two letters change
        if addr[0:2] != key:
            # Create a new entry in the dictionary
            key = addr[0:2]
            sin_addr[key] = list()
        # Add the address to the dictionary corresponding entry
        sin_addr[key].append(addr[:-1])

print "[ok] Load data base"

def is_in(sin_addr, addr):
    """
        Tells whether @p addr is present in the 
        dictionary @p sin_addr or not.

    """
    # Get the key of the dictionary where the address mught be
    key = addr[0:2]
    # Lower bound of the search space
    lo = 0
    # Higher bound of the search space
    hi = len(sin_addr[key]) - 1

    while lo < hi:
        mid = (hi + lo) / 2
        if lo == mid or hi == mid:
            return sin_addr[key][lo] == addr or sin_addr[key][hi] == addr
        if sin_addr[key][mid] == addr:
            return True
        elif sin_addr[key][mid] < addr:
            lo = mid
        else:
            hi = mid
    return sin_addr[key][lo] == addr

# Two basic tests to ensure the seach works
assert is_in(sin_addr, "cfp@grehack.fr") == False
assert is_in(sin_addr, "pope@vatican.com") == True

print "[ok] Test search in data"

# List of email addresses matching
found = list()
# Number of matches
n = 0
# Total of email addresses tested
t = 0
# Open my personal address book
with open("addr.txt", "r") as f:
    # For each address
    for addr in f:
        # Avoid mistakes in parsing : ignoring non-address lines
        if "@" not in addr:
            continue
        # Increment total
        t += 1
        # Check if the address is in the dump
        if addr[:-1] in sin_addr:
            n += 1
            found.append(addr[:-1])
    
    print "[ok] Search match between address book and silly emails"
    print
    if n == 0:
        print "({0}/{1}) No match found. Your address book is made of respectable people.".format(n, t)
    else:
        print "{0} matchs found: {1}".format(n, found)
