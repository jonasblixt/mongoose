# -*- coding: utf-8 -*-

import kicad
import model
from stackups import JLCPCB6Layers
#from dram import lp4


# IMX8MM
# Diff pairs should be matched within 1ps

# CK_t/CK_c max 200 ps

# CA[5:0]
# CS[1:0]       min: CK_t - 25ps,  max: CK_t + 25ps
# CKE[1:0]

# DQS0_t/DQS0_c min: CK_t - 85ps, max CK_t + 85ps

# DQ[7:0]       min: DQS0_t - 10ps, max DQS0_t + 10ps
# DM0

# DQS1_t/DQS1_c min: CK_t - 85ps, max CK_t + 85ps

# DQ[15:8]      min: DQS1_t - 10ps, max DQS1_t + 10ps
# DM1

if __name__ == "__main__":

    pcb = kicad.KicadPCB("../mongoose.kicad_pcb", JLCPCB6Layers())

    # DiffPair(pcb, "_n","_p", max_delay_ps=200.0, max_skew_ps=1.0)

    for net_index in pcb.get_nets().keys():
        net = pcb.get_nets()[net_index]
        print(net.get_name() + " dly: %.2f ps"%(net.get_delay_ps()))
