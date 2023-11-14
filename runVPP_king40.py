#!/opt/miniconda3/bin/python
# -*- coding: utf-8 -*-
import numpy as np

from src.YachtMod import Yacht, Keel, Rudder
from src.SailMod import Main, Jib, Kite
from src.VPPMod import VPP
from src.UtilsMod import VPPResults

King40 = Yacht(Name="King 40 - Witchcraft",
               # if no data is avail assume it comes from YD40 dimensions
            Lwl=10.60, # https://sailboatdata.com/sailboat/king-40/?units=metric
            Vol=6.05, # NEED TO ESTIMATE # Vol : volume of canoe body (m^3)
            Bwl=3.70, # https://sailboatdata.com/sailboat/king-40/?units=metric
            Tc=0.4, # NEED TO ESTIMATE # Tc : Caonoe body draft (m)
            WSA=28.20, # NEED TO ESTIMATE WSA : Wtter surface area (m^2) (wetted surface area)
            Tmax=2.51, # Maximum draft of yacht (m) https://sailboatdata.com/sailboat/king-40/?units=metric
            Amax=1.051, # NEED TO ESTIMATE WSA Max section area (m^2)
            Mass=7100, # 7100kg? looks abit large (ballast is 3300kg)
            Ff=1.5, # NEED TO ESTIMATE Form factor
            Fa=1.5, # NEED TO ESTIMATE Aerodynamic Force coefficient
            Boa=3.7, # Beam overall (max beam) https://sailboatdata.com/sailboat/king-40/?units=metric
            Loa=12.1, # https://sailboatdata.com/sailboat/king-40/?units=metric
            # No keel and rudder dimensions
            App=[Keel(Cu=1.00, Cl=0.78, Span=1.90),
                  Rudder(Cu=0.48, Cl=0.22, Span=1.15)],
            Sails=[Main("MN1", P=16.00, E=5.25, Roach=0.1, BAD=1.0), # P, E from: https://sailboatdata.com/sailboat/king-40/?units=metric
                   Jib("J1", I=16.25, J=4.70, LPG=5.40, HBI=1.8), # I, J from https://sailboatdata.com/sailboat/king-40/?units=metric
                   Kite("A2", area=150.0, vce=9.55),
                   Kite("A5", area=75.0, vce=2.75)]
      )

vpp = VPP(Yacht=King40)

vpp.set_analysis(tws_range=np.arange(4.0,22.0,2.0),
                 twa_range=np.linspace(30.0,180.0,31))

# reduces sim conditions for testing 
#vpp.set_analysis(tws_range=np.arange(8.0, 11.0 ,1.0),
#                twa_range=np.linspace(30.0,90.0,2))


vpp.run(verbose=False)
print(f'Store type: {type(vpp.store)}')
print(vpp.store)
vpp.write('results')

vpp.polar(3, True)
vpp.SailChart(True)
