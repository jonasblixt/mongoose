import model
import re

class KicadPCB(model.PCB):
    def __init__(self, filename, stackup):
        model.PCB.__init__(self, stackup)

        self.parsing_errors = 0
        process_nets = True

        self.r_thickness = re.compile(".+thickness\ ([0-9\.]+)\)")
        self.r_net = re.compile(".+\(net\ ([0-9]+)\ \"?([^\"]+)\"?\)")

        # Segments regex
        #
        # group 1 = Start X
        # group 2 = Start Y
        # group 3 = End X
        # group 4 = End Y
        # group 5 = Width
        # group 6 = Layer
        # group 7 = net

        self.r_seg = \
                re.compile("\ +\(segment\ \(start\ ([0-9\.]+)\ ([0-9\.]+)\)" +
                           "\ \(end\ ([0-9\.]+)\ ([0-9\.]+)\)\ " +
                           "\(width\ ([0-9\.]+)\)\ " +
                           "\(layer\ ([a-zA-Z0-9\.]+)\)\ " +
                           "\(net\ ([0-9]+)\).*")

        # Via regex
        #
        # group 1 = x
        # group 2 = y
        # group 3 = size
        # group 4 = drill
        # group 5 = Start layer
        # group 6 = Stop layer
        # group 7 = net

        self.r_via = re.compile("\ +\(via\ " +
                "\(at\ ([0-9\.]+)\ ([0-9\.]+)\)\ " +
                "\(size\ ([0-9\.]+)\)\ " +
                "\(drill\ ([0-9\.]+)\)\ " +
                "\(layers\ ([a-zA-Z0-9\.]+)\ ([a-zA-Z0-9\.]+)\)\ " +
                "\(net\ ([0-9]+)\).*")

        with open(filename, "r") as f:
            while True:
                line = f.readline()

                if not line:
                    break

                if "(general" in line:
                    self.process_general_section(f)
                if ("(net" in line) and process_nets:
                    self.process_net(line)
                if "(net_class" in line:
                    process_nets = False
                if "(segment" in line:
                    self.process_segment(line)
                if "(via" in line:
                    self.process_via(line)

        self.process()

    def process_via(self, line):
        m = re.match(self.r_via, line)

        if m:
            x = float(m.group(1))
            y = float(m.group(2))
            dia = float(m.group(3))
            drill = float(m.group(4))
            start_layer = m.group(5)
            stop_layer = m.group(6)
            net = int(m.group(7))

            via = model.Via(self, x, y, dia, drill, start_layer,
                            stop_layer, net)
            self.add_via(net, via)

    def process_segment(self, line):
        m = re.match(self.r_seg, line)

        if m:
            sx = float(m.group(1))
            sy = float(m.group(2))
            ex = float(m.group(3))
            ey = float(m.group(4))
            w = float(m.group(5))
            layer_str = m.group(6)
            net_idx = int(m.group(7))
            #print("s %f,%f -> %f,%f w=%.2f, net=%i %s"%(sx, sy, ex, ey, w,
            #    net_idx, self.nets[net_idx].name))
            seg = model.Segment(self, sx, sy, ex, ey, w, layer_str)
            self.add_segment(net_idx, seg)
    def process_net(self, line):
        m = re.match(self.r_net, line)

        if m:
            self.add_net(int(m.group(1)),
                        model.Net(int(m.group(1)), m.group(2)))

    def process_general_section(self, f):
        pc = 1

        while True:
            line = f.readline()
            pc += line.count("(")
            pc -= line.count(")")

            m = re.search(self.r_thickness, line)

            if m:
                print("PCB Thickness = %s mm"%(m.group(1)))
                self.pcb_thickness = float(m.group(1))

            if pc == 0:
                return

