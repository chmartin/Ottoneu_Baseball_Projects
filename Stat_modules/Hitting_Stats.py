import numpy as np

def safe_divide(Num,Denom):
    try:
        return Num/Denom
    except ZeroDivisionError:
        return 0.

def PA(AB:np.float64 = 0.,
       BB:np.float64 = 0.,
       HBP:np.float64 = 0.,
       SH:np.float64 = 0.,
       SF:np.float64 = 0.,
       CI:np.float64 = 0.):
    return AB+BB+HBP+SH+SF+CI

def TB(B1:np.float64,
       B2:np.float64,
       B3:np.float64,
       HR:np.float64,
       ):
    return B1+2*B2+3*B3+4*HR

def BB_pct(BB:np.float64 = 0.,
           PA:np.float64 = 0.): 
    return safe_divide(BB,PA)

def K_pct(K:np.float64 = 0.,
          PA:np.float64 = 0.): 
    return safe_divide(K,PA)

def ISO(B2:np.float64 = 0.,
        B3:np.float64 = 0.,
        HR:np.float64 = 0.,
        AB:np.float64 = 0.): 
    return safe_divide(((B2) + (2*B3) + (3*HR)),AB)

def BABIP(H:np.float64 = 0.,
        HR:np.float64 = 0.,
        AB:np.float64 = 0.,
        K:np.float64 = 0.,
        SF:np.float64 = 0.): 
    return safe_divide((H-HR),(AB-K-HR+SF))

def AVG(H:np.float64 = 0.,
          AB:np.float64 = 0.): 
    return safe_divide(H,AB)

def OBP(H:np.float64 = 0.,
        BB:np.float64 = 0.,
        HBP:np.float64 = 0.,
        SF:np.float64 = 0.,
        AB:np.float64 = 0.): 
    return safe_divide((H+BB+HBP),(AB+BB+HBP+SF))

def SLG(TB:np.float64 = 0.,
        AB:np.float64 = 0.
):
    return safe_divide(TB,AB)

# def wOBA(Weighted On Base Average): Combines all the different aspects of hitting into one metric, weighting each of them in proportion to their actual run value. While batting average, on-base percentage, and slugging percentage fall short in accuracy and scope, wOBA measures and captures offensive value more accurately and comprehensively.

# wRC+ (Weighted Runs Created Plus): The most comprehensive rate statistic used to measure hitting performance because it takes into account the varying weights of each offensive action (like wOBA) and then adjusts them for the park and league context in which they took place.

# BsR (Base Running Runs Above Average): Number of runs above or below average a player has been worth on the bases, based on stolen bases, caught stealing, extra bases taken, outs on the bases, and avoiding double plays. It is the combination of wSB, UBR, and wGDP.