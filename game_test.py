import game
import matplotlib.pyplot as plt
import numpy

W=1.08 # Wt
psi=0.4 #Ψ
thet=0.05 #θ
K=1000000
sigma=5/1000000 #σ
Uc=[[]]

Uc0=[]

Us=[[]]

Us0=[]

step=numpy.arange(0,1,0.001,dtype='float16')

color=['r','g','c','m','y','k']

sigmat=[1/1000000,2/1000000,3/1000000,4/1000000,5/1000000,6/1000000]
Wt=[1.02,1.04,1.06,1.08]
psit=[0.1,0.2,0.3,0.4]

#三个图对应修改的地方
for i in psit: # Wt，Ψt，σt
    Uc0 = []
    Us0 = []
    psi=i # W，Ψ，σ，这里没有t，为payoffMatrix传参
    for rho in step:
        rs=game.payoffMatrix(W,psi,sigma,rho)
        Pa=game.probilityOfFD(K,sigma,rho)
        P0=game.probilityOfND(K,sigma,rho)
        if Pa+P0>1:
            print("gg")
        tc,ts=game.payoff(rs, Pa, P0)

        Uc0.append(tc)
        Us0.append(ts)
    Uc.append(Uc0)
    Us.append(Us0)
    plt.xlim(xmax=1,xmin=0)
    plt.plot(step,Uc0,ls='--', c='%s'%color[int(i*10)+1],label='%.1f $U_C$'%i) # color索引要改
    plt.plot(step,Us0,'%s'%color[int(i*10)+1],label='%.1f $U_S$'%i) # color索引要改
    print(int(i*1000000)-1)

# for rho in step:
#     rs=game.payoffMatrix(W,psi,sigma,rho)
#     Pa=game.probilityOfFD(K,sigma,rho)
#     P0=game.probilityOfND(K,sigma,rho)
#     if Pa+P0>1:
#         print("gg")
#     tc,ts=game.payoff(rs, Pa, P0)
#
#     Uc0.append(tc)
#     Us0.append(ts)
# Uc.append(Uc0)
# Us.append(Us0)
# plt.xlim(xmax=1,xmin=0)
# plt.plot(step,Uc0,ls='--', c='%s'%color[1],label='$U_C$')
# plt.plot(step,Us0,'%s'%color[2],label='$U_S$')

plt.xlabel("Cheating probability",fontsize=12)
plt.ylabel("Utility",fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc = 3, prop = {'size':10})
plt.show()