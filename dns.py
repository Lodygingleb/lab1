
class DNS:
    def __init__(self):
        self.addresses = {}

    def setComp(self, addr, comp):
        self.addresses[addr] = comp

    def getComp(self, addr):
        return self.addresses[addr]
