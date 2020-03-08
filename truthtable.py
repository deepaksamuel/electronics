# This code demostrates the use of the ttg package which is helpful in generating TT
# In this code, I make use of the example in Pg 119 of Taub and Schilling to demontrate how redundant minterms can be avoided in a K-Map
#%%
import ttg
print(ttg.Truths(['A', 'B', 'C', 'D'],['A and (~C) and (~D)', '(~A) and (~B) and C', '(~B) and C and (~D)', 'A and (~B) and (~D)' ]))

# The final expression can be written as in eqn 3.20-8 (making use of eqn 3.20-6) 
print(ttg.Truths(['A', 'B', 'C', 'D'],[ '(A and (~C) and (~D)) or ((~A) and (~B) and C) or ((~B) and C and (~D))' ]))

# The final expression can also be written making use of eqn 3.20-7 
print(ttg.Truths(['A', 'B', 'C', 'D'],[ '(A and (~C) and (~D)) or ((~A) and (~B) and C) or (A and (~B) and (~D))' ]))

# The final expression can also be written making use of both eqn 3.30-6 and eqn 3.20-7 (sum)
# This has more terms than neccessary and therefore uses more logic gates. 
print(ttg.Truths(['A', 'B', 'C', 'D'],[ '(A and (~C) and (~D)) or ((~A) and (~B) and C) or (A and (~B) and (~D)) or ((~B) and C and (~D))' ]))

