def swap_case(s):
    return ''.join(i.lower() if i.isupper() else i.upper() if i.islower() else i for i in s)


# proble url
# https://www.hackerrank.com/challenges/swap-case/problem