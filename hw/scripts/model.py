# -*- coding: utf-8 -*-
import math

class Net(object):
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.length = 0.0
        self.delay_ps = 0.0
        self.segments = []
        self.vias = []
    def get_name(self):
        return self.name
    def add_segment(self, seg):
        self.segments.append(seg)
        self.length += seg.get_length_mm()
        self.delay_ps += seg.get_delay_ps()
    def add_via(self, via):
        self.vias.append(via)
        self.length += via.get_length_mm()
        self.delay_ps += via.get_delay_ps()
    def via_count(self):
        return len(self.vias)
    def get_delay_ps(self):
        return self.delay_ps
    def length(self):
        return self.length

class ElectricalObject(object):
    def __init__(self):
        self.delay_ps = 0.0
        self.length = 0.0
    def get_delay_ps(self):
        return self.delay_ps
    def add_delay_ps(self, dly):
        self.delay_ps += dly
    def get_length_mm(self):
        return self.length

class Pad(ElectricalObject):
    pass

class Segment(ElectricalObject):
    def __init__(self, pcb, sx, sy, ex, ey, w, layer_str):
        ElectricalObject.__init__(self)
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.w = w
        self.layer_str = layer_str

        self.length += math.sqrt(math.pow(ex - sx, 2) + \
                                 math.pow(ey - sy, 2))

        e_eff = 0.475 * pcb.stackup.get_er() + 0.68
        self.add_delay_ps(3.337*math.sqrt(e_eff))

class Via(ElectricalObject):
    def __init__(self, pcb, x, y, dia, drill, start_layer, stop_layer, net_id):
        ElectricalObject.__init__(self)
        self.x = x
        self.y = y
        self.dia = dia
        self.drill = drill
        self.start_layer = start_layer
        self.stop_layer = stop_layer
        self.net_id = net_id
        self.length = pcb.stackup.get_thickness()

        er = pcb.stackup.get_er()
        pcb_thickness_inch = pcb.stackup.get_thickness() / 25.4
        dia_inch = drill / 25.4
        dia_clearance_inch = dia / 25.4

        C_via_pF = (1.41 * er * pcb_thickness_inch * dia_inch) \
                   / (dia_clearance_inch - dia_inch)
        L_via_nH = pcb_thickness_inch * 5.08 * \
                (1 + math.log(4 * pcb_thickness_inch/dia_inch))

        delay_via_ps = math.sqrt(L_via_nH * C_via_pF)
        #print("Via  %.2f pF, %.2f nH %.2f ps "%(C_via_pF, L_via_nH,
        #            delay_via_ps))

        self.add_delay_ps(delay_via_ps)

class Layer(object):
    def __init__(self, layer_idx, thickness, er, kind):
        self.thickness = thickness
        self.layer_idx = layer_idx
        self.er = er
        self.kind = kind
    def get_thickness(self):
        return self.thickness
    def get_er(self):
        return self.er
    def get_index(self):
        return self.layer_idx

class Stackup(object):
    def __init__(self, name="Generic"):
        self.name = name
        self.layers_by_name = {}
        self.layers_by_index = {}
        self.layers = []
        self.er = 4.0
        self.cu_layer_count = 1
        self.thickness = 0.0
    def get_name(self):
        return self.name
    def get_er(self):
        return self.er
    def get_thickness(self):
        return self.thickness
    def add_cu_layer(self, thickness, layer_mapping_str):
        l = Layer(self.cu_layer_count, thickness, self.er, "Cu")
        self.layers_by_name[layer_mapping_str] = l
        self.layers_by_index[self.cu_layer_count] = l
        self.layers.append(l)
        self.cu_layer_count += 1
        self.thickness += thickness
        return l
    def add_pp_layer(self, thickness):
        self.layers.append(Layer(-1, thickness, -1.0, "pp"))
        self.thickness += thickness
    def add_core_layer(self, thickness):
        self.layers.append(Layer(-1, thickness, -1.0, "core"))
        self.thickness += thickness
    def get_layers(self):
        return self.layers
    def get_layer_by_index(self, idx):
        return self.layers_by_index[idx]
    def get_layer_by_name(self, name):
        return self.layers_by_name[name]
    def distance_from_to_layer(self, l1, l2):
        dist = 0.0
        start_measure = False
        i = 0

        while True:
            l = self.layers[i]
            if l.layer_idx == l2:
                break
            if start_measure:
                dist += l.thickness
            if l.layer_idx == l1:
                start_measure = True
            i = i + 1
        return dist

class PCB(object):
    def __init__(self, stackup):
        self.pcb_thickness = -1.0
        self.stackup = stackup
        self.nets = {}
    def add_segment(self, net_idx, seg):
        net = self.nets[net_idx]
        net.add_segment(seg)
    def add_net(self, name, net):
        self.nets[name] = net
    def add_via(self, net_idx, via):
        net = self.nets[net_idx]
        net.add_via(via)
    def get_nets(self):
        return self.nets
    def process(self):
        assert(self.pcb_thickness > 0.0)
        assert(len(self.nets.keys()) > 0)

        # Calculate distance added by via's
        for n in self.nets.keys():
            net = self.nets[n]
            for v in net.vias:
                segs = []
                for s in net.segments:
                    if (v.x == s.sx and v.y == s.sy) or \
                       (v.x == s.ex and v.y == s.ey):
                        segs.append(s)
                if len(segs) > 1:
                    l_start = self.stackup.get_layer_by_name(segs[0].layer_str)
                    l_end = self.stackup.get_layer_by_name(segs[1].layer_str)
                    net.length += \
                        self.stackup.distance_from_to_layer(l_start.layer_idx,
                                                            l_end.layer_idx)

        print("Found %u nets"%(len(self.nets.keys())))
