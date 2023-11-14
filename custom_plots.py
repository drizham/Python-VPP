import matplotlib.pyplot as plt
import numpy as np
from src.UtilsMod import VPPResults,_get_vmg, _get_cross, cols, stl, KNOTS_TO_MPS

results = VPPResults('results')

fig, ax = plt.subplots(3, 1, figsize=(8, 9))
wind = results.twa_range
twinx = ax[1].twinx()
twinx2 = ax[2].twinx()
target_speed = []; target_speed2 = []
target_beat = []; target_gybe = []
for i in range(len(results.tws_range)):
    vmg, ids = _get_vmg(results.store[i, :, :, :], results.twa_range)
    for k in range(results.Nsails):
        # index where sail cross over occurs
        idx = _get_cross(results.store[i, :, :, :], k)
        # prevents putting legend everywhere
        lab = "_nolegend_"
        if k==0: lab = f"{results.tws_range[i]/KNOTS_TO_MPS:.1f}"
        # plot TWA vs boat speed
        ax[0].plot(wind[idx[0]:idx[1]],results.store[i, idx[0]:idx[1], k, 0],
                    color=cols[k%7],lw=np.where(i<7,1.5,2.5),linestyle=stl[i%7],label=lab)
    # add VMG points
    for pts in range(2):
        ax[0].plot(wind[vmg[pts]],results.store[i, vmg[pts], ids[pts], 0],
                    "o",color=cols[ids[pts]%7],lw=1,markersize=4,mfc="None")
    target_speed.append(results.store[i, vmg[0], ids[0], 0])
    target_speed2.append(results.store[i, vmg[1], ids[1], 0])
    target_beat.append(wind[vmg[0]])
    target_gybe.append(wind[vmg[1]])
    # add legend only on first axis
    ax[0].legend(title=r"TWS (knots)")
# target beat axis
twinx.plot(results.tws_range/KNOTS_TO_MPS, target_speed,"-",color=cols[0],lw=1,label="Target Speed")
ax[1].plot(results.tws_range/KNOTS_TO_MPS, target_beat,"-",color=cols[1],lw=1,label="Target Beat")
ax[1].legend(); twinx.legend()
# target gybe axis
twinx2.plot(results.tws_range/KNOTS_TO_MPS, target_speed2,"-",color=cols[0],lw=1,label="Target Speed")
ax[2].plot(results.tws_range/KNOTS_TO_MPS, target_gybe,"-",color=cols[1],lw=1,label="Target Gybe")
ax[2].legend(); twinx2.legend()
ax[0].set_xlim(0,180)
ax[0].set_xlabel(r"True Wind Angle ($^\circ$)")
ax[0].set_ylabel(r"Target Boat Speed (knots)")
twinx.set_ylabel(r"Target Boat Speed (knots)")
ax[1].set_ylabel(r"Beat Angle (knots)")
ax[1].set_xlim(0,max(results.tws_range/KNOTS_TO_MPS))
ax[1].set_ylabel(r"Beat Angle ($^\circ$)")
plt.tight_layout()
# if save:
    # plt.savefig(fname, dpi=96)
plt.show()