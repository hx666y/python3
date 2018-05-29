class Ren:
    def __init__(self,name):
        self.name = name
        self.xue = 100
        self.qiang = None

    def __str__(self):
        return self.name + "剩余血量为:" + str(self.xue)   

    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)

    def andanjia(self,qiang,danjia):
        qiang.lianjiedanjia(danjia)

    def naqiang(self,qiang):
        self.qiang = qiang

    def kaiqiang(self,diren):
        if self.qiang:
            self.qiang.she(diren)
        else:
           print("请先拿枪")

    def diaoxue(self,shashangli):
        self.xue -= shashangli

class Danjia:
    def __init__(self,rongliang):
        self.rongliang = rongliang
        self.rongnaList = []

    def __str__(self):
        return "弹夹当前的子弹数量为:" + str(len(self.rongnaList)) + "/" + str(self.rongliang)

    def baocunzidan(self,zidan):
        if len(self.rongnaList) < self.rongliang:
            self.rongnaList.append(zidan)

    def chuzidan(self):
        if len(self.rongnaList) > 0:
            zidan = self.rongnaList[-1]
            self.rongnaList.pop()
            return zidan
        else:
            return None

class Zidan:
    def __init__(self,shashangli):
        self.shashangli = shashangli

    def shanghai(self,diren):
        diren.diaoxue(self.shashangli)

class Qiang:
    def __init__(self):
        self.danjia = None

    def __str__(self):
        if self.danjia:
            return "枪已装满弹夹"
        else:
            return "枪没有弹夹"

    def lianjiedanjia(self,danjia):
        if not self.danjia:
            self.danjia = danjia

    def she(self,diren):
        zidan = self.danjia.chuzidan()
        if zidan:
            zidan.shanghai(diren)
        else:
            print("没有子弹了")

class AK47(Qiang):
    def she(self,diren):
        i=0
        while i<5:
            super().she(diren)
            i+=1

#class AK47(Qiang):
#    def she(self,diren):
#        i = 0
#        while i<5:
#            zidan = self.danjia.chuzidan()
#            if zidan:
#                zidan.shanghai(diren)
#            else:
#                print("没有子弹了")
#            i+=1



laowang = Ren("老王")
danjia = Danjia(20)
zidan = Zidan(5)
print(danjia)
i=0
while i<10:
    laowang.anzidan(danjia,zidan)
    i+=1
print(danjia)
qiang = AK47()
print(qiang)
laowang.andanjia(qiang,danjia)
print(qiang)

# 创建一个敌人
diren = Ren("敌人")
print(diren)
laowang.kaiqiang(diren)
laowang.naqiang(qiang)
laowang.kaiqiang(diren)
print(diren)
print(danjia)
