def swap_case(s):
    return ''.join(i.lower() if i.isupper() else i.upper() if i.islower() else i for i in s)

# we can use result = ''  empty string 'and' can add it to i everytime but 
# since strings in pyrhon are immutable that makes our solution very slow for larger string
#  n(n*1)/2 -> it becomes n*2 problem
# so using a list append and then join is best solution
# but there are if list is very large  we need to create a list then join might be slow
# but not very slow it is also efficient
# so we are using this iterator syntax which leverage join and also don't create complete list   