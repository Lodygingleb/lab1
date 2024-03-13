import unittest
from comp import Comp, NetworkInterface
from net import Net
from dns import DNS

import unittest

class TestNetworkInterface(unittest.TestCase):
    def test_setConnections(self):
        net = Net()
        addr = "192.168.1.1"
        iface = NetworkInterface()
        iface.setConnections(net, addr)
        self.assertEqual(iface.net, net)
        self.assertEqual(iface.addr, addr)

    def test_setDns(self):
        dns = DNS()
        iface = NetworkInterface()
        iface.setDns(dns)
        self.assertEqual(iface.dns, dns)

    def test_resolve(self):
        iface = NetworkInterface()
        addr = "192.168.1.1"
        iface.resolve(addr)
        self.assertEqual(iface.addr, addr)

class TestComp(unittest.TestCase):
    def test_get_comp(self):
        comp = Comp()
        dns = DNS()
        addr = "192.168.1.1"
        comp_obj = "test comp"
        dns.setComp(addr, comp_obj)
        comp.iface.dns = dns
        self.assertEqual(comp.get_comp(addr), comp_obj)

    def test_get_comp_inner(self):
        com1 = Comp()
        net1 = Net()
        net1.setConnection("152.34.5.5")
        com1.iface.setConnections(net1, "152.35.5.5")
        com2 = Comp()
        net2 = Net()
        net2.setConnection("152.35.5.5")
        net2.setConnection("152.33.5.5")
        com2.iface.setConnections(net1, "152.34.5.5")
        com3 = Comp()
        net3 = Net()
        net3.setConnection("152.34.5.5")
        com3.iface.setConnections(net1, "152.33.5.5")
        dns = DNS()
        dns.setComp("152.33.5.5", com3)
        dns.setComp("152.34.5.5", com1)
        dns.setComp("152.35.5.5", com2)
        com1.iface.setDns(dns)
        com2.iface.setDns(dns)
        com3.iface.setDns(dns)

        self.assertEqual(com1.get_comp("152.33.5.5"), com3)


class TestDNS(unittest.TestCase):
    def test_setComp(self):
        dns = DNS()
        addr = "192.168.1.1"
        comp_obj = "test comp"
        dns.setComp(addr, comp_obj)
        self.assertEqual(dns.addresses[addr], comp_obj)

    def test_getComp(self):
        dns = DNS()
        addr = "192.168.1.1"
        comp_obj = "test comp"
        dns.setComp(addr, comp_obj)
        self.assertEqual(dns.getComp(addr), comp_obj)

class TestNet(unittest.TestCase):
    def test_setConnection(self):
        net = Net()
        addr = "192.168.1.1"
        net.setConnection(addr)
        self.assertEqual(net.connections[0], addr)


if __name__ == '__main__':
    unittest.main()
