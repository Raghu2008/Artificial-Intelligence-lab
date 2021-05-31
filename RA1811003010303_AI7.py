#!/usr/bin/env python
# coding: utf-8

# In[1]:


clause1 = []
clause2 = []

# enter the expression in clauses, one expression in one line
print("Enter clause 1:")
while True:
    inp = input()
    if inp == 'q':
        break
    clause1.append(inp)
    
print("\nEnter clause 2:")
while True:
    inp = input()
    if inp == 'q':
        break
    clause2.append(inp)

print("Clause 1: ", clause1)
print("Clause 2: ", clause2)

if len(clause1) != len(clause2):
    print("Clauses have different number of expression.")
    exit()



substitution_set = {}

for i in range(len(clause1)):
    expr1 = clause1[i]
    expr2 = clause2[i]

    if expr1 == expr2:
        substitution_set[expr1] = expr2
        continue

    if expr1.islower() and expr2.islower() and expr1 != expr2:

        # if yes, then expr1 is a function (f(x))
        if len(expr1) > 1:
            substitution_set[expr1] = expr2

        elif len(expr2) > 1:
            substitution_set[expr2] = expr1

        else:
            print("unification is not possible: ", expr1, "!=", expr2)
            exit()

    #the final case is when one is a value and other is a variable
    #here, we need to perform substitution and ofc check if this is feasible
    variable = ''
    const = ''
    if expr1.isupper():
        variable = expr1
        const = expr2
    else:
        variable = expr2
        const = expr1

    if variable in substitution_set and substitution_set[variable] != const:
        print("Subsitution set until here: ", substitution_set)
        print("Substitution of variable already exists in set and is different from current variable encountered", const, "!=", substitution_set[variable])
        exit()

    else:
        # like X/x - X->variable, x->const
        substitution_set[variable] = const


print("The unifier is: ", substitution_set)


# In[ ]:





# In[ ]:




