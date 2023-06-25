# format(): return a new string with tokens replaced
aa = 'Jose'
var = 34

# 2 arguments to replace 2 {} tokens
bb = '{} is {} years old'.format(aa, var)

print(bb)                     # jose is a 34 year old.

# 2 arguments to replace 2 named tokens
cc = '{name} is {age} years'.format(name=aa, age=var)
