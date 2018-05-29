class SweetPotato:

    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []

    def __str__(self):
        msg = "地瓜的生熟程度为:" + self.cookedString
        msg += "\t等级为:" + str(self.cookedLevel)
        if len(self.condiments) > 0:
            msg += "\t作料为:"        
            for temp in self.condiments:
                msg += temp + ","
            #msg = msg[:-1]
            msg = msg.rstrip(",")
        else:
            msg += "\t没有作料"
        return msg  

    def cook(self,times):
        self.cookedLevel += times
        if self.cookedLevel>8:
            self.cookedString = "焦了"
        elif self.cookedLevel>5:
            self.cookedString = "熟了"
        elif self.cookedLevel>3:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"

    def addCondiments(self,temp):
        self.condiments.append(temp)


digua = SweetPotato()
print(digua)
digua.cook(1)
digua.addCondiments("番茄酱")
print(digua)
digua.cook(3)
digua.addCondiments("孜然")
print(digua)
digua.cook(3)
digua.addCondiments("辣椒酱")
print(digua)
digua.cook(4)
print(digua)

