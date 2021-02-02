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
    """Calculate the volumetric efficiency of engine. Info from here: https://x-engineer.org/automotive-engineering/internal-combustion-engines/performance/calculate-volumetric-efficiency/
    
    Volumetric efficiency is the capacity of the engine to fill the available volume with air, or the ratio between air drawn in and volume available to draw.

    Total volume = num cylinders * total volume of 1 cylinder
        -While the total cylinder volume is displacement + clearance volume, the clearance is so low it typically is ignored in this calculation

    In indirect injection, air is mixed with fuel prior to being drawn in. Since the ratio is 1:14.7ish, normally it too is neglected.
        -The Saab is DI anyways, so it's 100% correct to ignore.
    
    The actual intake air volume can be calculated from the air mass (kg) and density (kg/m3):
        Volume of ai = mass of air / density of air
    
    1. Calculate air density
        If intake air pressure and temp are measured, intake air density is:
        Pa = za / (Ra * Ta)
            Pa (kg/m3) intake air density
            za (Pascals?) intake air pressure
            Ta (K) intake air temperature
            Ra (J/kgK) gas constant for dry air (equal to 286.9)

        Notes: I can't use actual data from the OBD2, because they are turbocharged. I need the Veff of the motor before the turbo, the turbo will bring them above 100% which is not what I'm looking for. So then...
            za should be the intake air pressure at my altitude
            Ta should be the temp at my engine intake, maybe I can estimate this or measure it?
            Ra is a constant


    2. Calculate the volumetric efficiency
        Veff = (mdota * Nr) / (Pa * Vd * Ne)
            Veff (%) what we're looking for!
            mdota (kg/s) air mass flow rate
                mdota = (Ma * Ne) / Nr
                    Ma (kg) air mass
                    Ne (rot/s) engine speed
                    Nr (unitless) number of crankshaft rotations for a complete cycle, 2 for a 4-stroke engine
            Pa (kg/m3) intake air density, calculated in step 1
            Vd (m3) volume of (1) cylinder

        Notes: I can model a graph of the Veff across RPM ranges. But doesn't it seem like it would be linear? Could come up with a 3d map of the Veff/Pa/Ne, still seems like it might be fairly linear but we will see, maybe I'm not looking at it hard enough.
    """



class Engine:
    """A class to model an engine and hold all it's info."""

    def __init__(self, L, alt, rpm_low, rpm_hi):
        self.cid = L_to_cid(L)
        self.rpmrange = (rpm_low, rpm_hi)
        self.airpressure = alt_air_pressure(alt)

    

    saab_cid = L_to_cid(saab_L)
    print(f'Saab in CID: (saab_cid)')


"""
Plan of attack:
    1. I need to calculate volumetric efficiency to move forward in the book. This is a pivotal figure in determining CFM. This is also going to be the first "big" part of this code.
        a. I'll need to figure out how to get MAF readings from the OBD2 in the saab.
        b. I'll have to write something to parse this data from a CSV
        c. Then that should give me the air mass which is needed for Ve




