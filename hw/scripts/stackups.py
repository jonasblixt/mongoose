# -*- coding: utf-8 -*-

import model

class JLCPCB6Layers(model.Stackup):
    def __init__(self):
        model.Stackup.__init__(self, "JLCPCB 6 Layers, shared panel")
        self.add_cu_layer(0.035, "F.Cu")
        self.add_pp_layer(0.1)
        self.add_cu_layer(0.0175, "In1.Cu")
        self.add_core_layer(0.565)
        self.add_cu_layer(0.0175, "In2.Cu")
        self.add_pp_layer(0.127)
        self.add_cu_layer(0.0175, "In3.Cu")
        self.add_core_layer(0.565)
        self.add_cu_layer(0.0175, "In4.Cu")
        self.add_pp_layer(0.1)
        self.add_cu_layer(0.035, "B.Cu")
