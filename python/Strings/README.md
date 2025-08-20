# we can use result = '' empty string 'and' can add it to i everytime but

# since strings in pyrhon are immutable that makes our solution very slow for larger string

# n(n*1)/2 -> it becomes n*2 problem

# so using a list append and then join is best solution

# but there are if list is very large we need to create a list then join might be slow

# but not very slow it is also efficient

# so we are using this iterator syntax which leverage join and also don't create complete list

377139 this is the rank after solving the problem
55 points to gold badge

solved python string mutation
369224 rank changed
45 points to gold badge

---

approach: we can approach it in two or three ways
one is built in methods
we we won't use since we are building logic
second is adding a string through slicing and adding it back like string[0:k] + character + string[k+1:]
so this is also works but for longer string it needs to create a sepeate string which might not be feasible for sometime
and also in loops also it is not feasible since there will be lot of garbage values for strings
so using list is better feasible for my solution
converting string to list by list(string) and changing and converting it to string through join
