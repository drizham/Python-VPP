#!/opt/miniconda3/bin/python
# -*- coding: utf-8 -*-
import numpy as np

from src.YachtMod import Yacht, Keel, Rudder
from src.SailMod import Main, Jib, Kite
from src.VPPMod import VPP
from src.UtilsMod import VPPResults

YD41 = Yacht(Name="B0_MK1", # Name Boat Zero MK1
            Lwl=9.122, # Lwl : waterline length (m)
            Vol=2.270, # 6.05, # Vol : volume of canoe body (m^3)
            Bwl=2.232, #3.18, # Bwl : waterline beam (m)
            Tc= 0.245, #0.4, # Tc : Caonoe body draft (m)
            WSA=16.195, # 28.20, # WSA : Wtter surface area (m^2) (wetted surface area)
            Tmax=2.1, #2.30, # Maximum draft of yacht (m)
            # Estimating Amax, 1.051 / 1.3^2 = 0.5911
            Amax= 0.5911, #1.051, #MISSING Amax  : Max section area (m^2)
            # scaling mass 6500/ (1.3 ^3)
            # 6500 / 2.37 = 2742kg
            Mass=2742, #Need an estimate Mass : total mass of the yacht (kg)
            Ff=0.858, #1.5, # avail in coeff sheet, need a name though
            Fa=0.655, #1.5, # avail in coeff sheet, need a name though
            Boa=3.1, # 4.2, #Bmax in spreadsheet; most likely beam over all
            Loa=9.126, # 12.5, # most likely length overall
            # Running the first iteration with Keel & Rudder data below from
            # the default YD40
            App=[Keel(Cu=1.00, Cl=0.78, Span=1.90), # App : appendages (Appendages object as list, i.e [Keel(...)] )
                  Rudder(Cu=0.48, Cl=0.22, Span=1.15)],
            Sails=[Main("MN1", P=12.5, #16.60,
            E=4.10,#5.60,
            Roach=0.1,
            BAD=1.25), # was 1.0 BAS/D boom above shear line/ deck

                   Jib("J1", I=11.9, #16.20,
                   J=3.6, #5.10,
                   LPG=3.4, #5.40,
                   HBI=1.7), #1.8
                   # 40->30 footer scale factor = 1.333, area scale factor is 1.333^2 = 1.77776
                   # Estimated area for kites is 150->84.37 & 75.-> 42.12
                   # vce, 9.55 -> 7.164; 2.75 -> 2.06
                   Kite("A2", area=84.37, vce=7.164), #Kite("A2", area=150.0, vce=9.55),
                   Kite("A5", area=42.12, vce=2.06)] #Kite("A5", area=75.0, vce=2.75)]
      )

vpp = VPP(Yacht=YD41)

vpp.set_analysis(tws_range=np.arange(4.0,22.0,2.0),
                 twa_range=np.linspace(30.0,180.0,31))

vpp.run(verbose=False)
vpp.write('results')
vpp.polar(3, True)
vpp.SailChart(True)
