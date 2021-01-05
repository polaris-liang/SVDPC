import numpy
import math

def comb(n,i):
    result = 1
    for j in range(1, i+1):
        result = result * (n-i+j) // j
    return result


def probilityOfFD(K,sigma,rho):
    Pa=comb(int(rho*K),int(sigma*K))/comb(K,int(sigma*K))
    return Pa


def probilityOfND(K, sigma, rho):
    a=comb(int((1-rho)*K),int(sigma*K))
    b=comb(K,int(sigma*K))
    P0=a/b
    if P0>1:
        print(P0)
    return P0

def payoffMatrix(W,psi,sigma,rho):
    B = 1.75
    phi = 0.5 #φ
    f = 1
    V = sigma
    if phi<=rho:
        F=f
    else:
        F=0

    Kb=2*B*rho
    Lb=4*B*rho
    rs=[[psi,-(1-rho)-F],[B+F,-Kb-psi-V],[psi,-(1-rho)],
        [B,-Kb-psi-V],[W,-(1-rho)],[B,-Lb-W-V]]
    return numpy.mat(rs)

def payoff(rs,Pa,P0):
    Us=Pa*(rs[0,0]+rs[0,1])+(1-Pa-P0)*(rs[2,0]+rs[2,1])+P0*(rs[4,0]+rs[4,1])
    Uc=Pa*(rs[1,0]+rs[1,1])+(1-Pa-P0)*(rs[3,0]+rs[3,1])+P0*(rs[5,0]+rs[5,1])
    return  Uc,Us

