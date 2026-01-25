import numpy as np

def safe_divide(Num,Denom):
    try:
        return Num/Denom
    except ZeroDivisionError:
        return 0.
    
def per_9(IP:np.float64=0.):
    return IP/9.

def K9(K:np.float64=0.,
       IP:np.float64=0.):
    return safe_divide(K/per_9(IP))

def BB9(BB:np.float64=0.,
       IP:np.float64=0.):
    return safe_divide(BB/per_9(IP))

def K_pct(K:np.float64=0.,
          TBF:np.float64=0.):
    return safe_divide(K,TBF)

def BB_pct(BB:np.float64=0.,
          TBF:np.float64=0.):
    return safe_divide(BB,TBF)

def K_pct_minus_BB_pct(K:np.float64=0.,
                       BB:np.float64=0.,
                       TBF:np.float64=0.):
    return K_pct(K,TBF) - BB_pct(BB,TBF)

def BAA(H:np.float64=0.,
        TBF:np.float64=0.):
    return safe_divide(H,TBF)

def HR9(HR:np.float64=0.,
       IP:np.float64=0.):
    return safe_divide(HR,per_9(IP))

def BABIP(
        H:np.float64=0.,
        HR:np.float64=0.,
        AB:np.float64=0.,
        K:np.float64=0.,
        SF:np.float64=0.):
    return safe_divide((H-HR),(AB-K-HR+SF))

def LOB_pct(
        H:np.float64=0.,
        HR:np.float64=0.,
        BB:np.float64=0.,
        HBP:np.float64=0.,
        R:np.float64=0.):
    return safe_divide((H+BB+HBP-R),(H+BB+HBP-(1.4*HR)))

def LOB_pct(
        H:np.float64=0.,
        HR:np.float64=0.,
        BB:np.float64=0.,
        HBP:np.float64=0.,
        R:np.float64=0.):
    return safe_divide((H+BB+HBP-R),(H+BB+HBP-(1.4*HR)))

#GB% (Ground Ball Percentage): The percentage of a pitcher’s balls in play that are ground balls, calculated as GB/BIP.

#HR/FB (Home Run to Fly Ball Rate): Percentage of a pitcher’s fly balls that go for home runs, calculated as HB/FB (even though some HR are line drives).

def ERA(ER:np.float64=0.,
        IP:np.float64=0.):
    return safe_divide(ER,per_9(IP))

def WHIP(BB:np.float64=0.,H:np.float64=0.,IP:np.float64=0.):
    return safe_divide(BB+H,IP)


# def FIP (Fielding Independent Pitching): An estimate of a pitcher’s ERA based on strikeouts, walks/HBP, and home runs allowed, assuming league average results on balls in play.
# ((13*HR)+(3*(BB+HBP))-(2*K))/IP + constant

# xFIP (Expected Fielding Independent Pitching): An estimate of a pitcher’s ERA based on strikeouts, walks/HBP, and fly balls allowed, assuming league average results on balls in play and home run to fly ball ratio.

# WAR (Wins Above Replacement): A comprehensive statistic that estimates the number of wins a player has been worth to his team compared to a freely available player such as a minor league free agent based on FIP