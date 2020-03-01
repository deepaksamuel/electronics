# This program demonstrated the development of signals
# in a op-amp with negative feedback using feedback theory
# as explained in Sedra Smith Chapter 7
# You will see that in this example, the output automatically
# stabilizes to the expected from feeback theory
# One important thing to remember in this simulation is that
# you are simulating a dynamical system and therefore, you cannot
# put it values as you get from your formulas. All systems take time
# to respond and therefore an op-amp cannot swing its voltage from 0 to
# 1000 V in one instant -it takes some time to do that and it does so only in
# steps of small voltages and in during those steps, things evolve differently

# In the following problem from SS Pg 764 Problem 7.1, A is taken to be 10^4
# beta is 0.1 making the closed loop gain to be 10 (assuming A*beta large, which it is, in this case)
# So we expect, the output voltage to be equal to 10 * Vs. We have take Vs to be 5 V and therefore
# we must see a output voltage close to 50 V.
# Next, we must also see that the voltage difference must be close to zero.
# For this to work, we must take care of large voltage swings and remember to 
# make such swings happen in steps. Here we have put the steps to be 0.1 
# So voltage increments or decrements will take place in steps of 0.1 V
# If the step is very large, you will see that the resolution will be very poor.
#    
#%%
import numpy as np
import matplotlib.pyplot as plt



A = 10000 # open loop gain
B = 0.1
Vs = 5.0 # volts
Vo = -10 # initial value of output
out = []
t = []
diff =[]
step = 0.1
for i in range(1,100000):
    #print(i)
    if i == 0:
        diff2 = 0
    else:
        diff2 = Vs - B*Vo
    #print(Vo,diff2)
    if A*diff2 > Vo:
        Vo = Vo + step 
    else:
        Vo = Vo - step
    t.append(i)
    out.append(Vo)
    diff.append(diff2)
    #print(Vs, Vo, B*Vo )

plt.plot(t,out)
plt.show()
print(np.mean(out))


# %%
