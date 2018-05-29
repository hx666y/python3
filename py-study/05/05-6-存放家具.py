class Home:
    def __init__(self, area):
        self.area = area
        self.light = "on"
        self.containsItem = []
    
    def __str__(self):
        msg = "家当前可用面积为:"+str(self.area)
        if len(self.containsItem)>0:
            msg += "\t家里的物品有:"
            for temp in self.containsItem:
                msg += temp.getName() + ","
            msg = msg[:-1]
            if self.light == "on":
                msg += "\t灯亮，所以物品可见"
            else:
                msg += "\t灯灭"
        return msg

    def addItem(self,item):
        needArea = item.getArea()
        if self.area > needArea:
            self.containsItem.append(item)
            self.area -= needArea

    def turnoff(self):
        self.light = "off"
        

class Bed(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        msg = self.name + "床的面积为:" + str(self.area)
        return msg

    def getName(self):
        return self.name

    def getArea(self):
        return self.area

home = Home(128)
print(home)

bed = Bed("席梦思",10)
print(bed)

home.addItem(bed)
print(home)

home.turnoff()
bed1 = Bed("竹板",5)
print(bed1)

home.addItem(bed1)
print(home)
