import math



def pressure_ratio(boostPSI):
    '''
    Returns pressure ratio in bar.

    Parameters:
    boostPSI (double): Boost PSI
    
    Returns:
    double: Pressure Ratio (bar, or number of atmospheres of pressure produced)
    '''
    
    return (14.7 + boostPSI) / 14.7


def airflow_rate(cid, rpm, Ev):
    '''
    Returns NA airflow rate of given displacement, RPM. Formula is CID * RPM * 0.5 * Ev

    Parameters:
    cid (int): Cubic Inch Displacement 
    rpm (int): Revolutions per Minute
    Ev (double): Volumetric Efficiency (Note 0.85 can be used as a rough estimate)
    
    Returns:
    double: Airflow rate in CFM
    '''
    return (cid * rpm * Ev) / (1728 * 2)

# Don't forget that boost airflow rate = NA airflow rate * Pressure Ratio


def L_to_cid(L):
    '''
    Change L to CID, because who lists motors in CID anymore.

    Inputs:
    L (double): Engine displacement in liters

    Returns:
    double: Engine displacement in CID
    '''
    return L * 61.0237

    
def alt_air_pressure(h):
    '''
    Calculates air pressure (inHG) from altitude (feet).

    Inputs:
    h (int): height in feet

    Returns:
    double: air pressure in inHg
    '''
    return 29.92 * math.exp(-0.0000366 * h)

def calc_ve(eng):
    """ 
    Okay so I didn't realize that other model relies on mdot to calculate Veff, because mdot also requires
    """



class Engine:
    """A class to model an engine and hold all it's info."""

    def __init__(self, L, alt, rpm_low, rpm_hi):
        self.cid = L_to_cid(L)
        self.rpmrange = (rpm_low, rpm_hi)
        self.airpressure = alt_air_pressure(alt)

    


if __name__ == '__main__':
    saab = Engine(2.0, 5200, 2000, 6000)
    print(saab.cid)

"""
Plan of attack:
    What a bummer. The last model I was chasing my own tail, looking to model mdot for Veff, when mdot relies on Veff. I need to read my other book.


"""
