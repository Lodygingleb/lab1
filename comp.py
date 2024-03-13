"Computer"

class NetworkInterface:
    def __init__(self):
        self.addr = None
        self.dns = None
        self.net = None

    def setConnections(self, net, addr):
        self.net = net
        self.addr = addr

    def setDns(self, dns):
        self.dns = dns

    def resolve(self, addr):
        self.addr = addr

class Comp:
    def __init__(self):
        self.iface = NetworkInterface()

    def get_comp(self, addr):
        if (self.iface.dns.getComp(addr) is None):
            for i in self.iface.net.connections:
                return self.iface.dns.getComp(self.iface.net.connections[i])
        else:
            return self.iface.dns.getComp(addr)


        #self.__localDb = None

  #  def setLocalDb(self, db):
       # self.__localDb = db