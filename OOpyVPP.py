#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Marin Lauber"
__copyright__ = "Copyright 2020, Marin Lauber"
__license__ = "GPL"
__version__ = "1.0.1"
__email__  = "M.Lauber@soton.ac.uk"

import numpy as np

from src.YachtMod import Yacht, Keel, Rudder
from src.SailMod import Main, Jib, Kite
from src.VPPMod import VPP

if __name__ == "__main__":

    # test with YD-41 from Larsson
    Keel  =  Keel(Cu=1.00,Cl=0.78,Span=1.90)
    Rudder = Rudder(Cu=0.48,Cl=0.22,Span=1.15)

    # Sailset
    main = Main(P=16.60,E=5.60,Roach=0.1,BAD=1.)
    J1 = Jib(I=16.20,J=5.10,LPG=5.40,HBI=1.8)
    A1 = Kite(area=115.6,vce=9.55)

    # Yacht
    YD41 = Yacht(Lwl=11.90,Vol=6.05,
                 Bwl=3.18,Tc=0.4,
                 WSA=28.20,Tmax=2.30,
                 Amax=1.051,Mass=6500,
                 Ff=1.5,Fa=1.5,
                 Boa=4.2,Loa=12.5,
                 App=[Keel,Rudder],
                 Sails=[main,J1])

    vpp = VPP(Yacht=YD41)

    vpp.set_analysis(tws_range=np.linspace(5,35,7),
                     twa_range=np.linspace(30.0,180.0,34))

    vpp.run(verbose=False)
    vpp.polar(n=3,save=False)
