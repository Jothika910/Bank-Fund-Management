class RBI:
    def __init__(self):
        self.total=10000
        self.account=10
        super().__init__()
    def up_total_amount(self):
        self.total+=self.self.A
class SBI(RBI):
    def __init__(self):
        self.total1=1000
        self.A=0
        super().__init__()
class tamilnadu(SBI):
    def __init__(self):
        self.total2=1000
        self.A=0
        self.account=4
        super().__init__()
    def up_total_amount(self):
        self.total1+=self.A
    def up_local_total(self):
        self.total2+=self.A
    def up_rbi_total(self):
        self.total+=self.A
    def withdraw(self,a,b):
        if b=="W" and self.A==0:
            self.A=-a
        elif b=="D" and self.A==0:
            self.A+=a
        elif b=="W" and self.A!=0:
            self.A=-a
        elif b=="D" and self.A!=0:
            self.A+=a
class kerala(SBI):
    def __init__(self):
        self.total3=1000
        self.A=0
        super().__init__()
    def up_total_amount(self):
        self.total1+=self.total3
    def up_local_total(self):
        self.total3+=self.A
    def up_rbi_total(self):
        self.total += self.A
    def withdraw(self,a,b):
        if b=="W" and self.A==0:
            self.A=-a
        elif b=="D" and self.A==0:
            self.A+=a
        elif b=="W" and self.A!=0:
            self.A=-a
        elif b=="D" and self.A!=0:
            self.A+=a
class mumbai(SBI):
    def __init__(self):
        self.total4=1000
        self.A=0
        super().__init__()
    def up_total_amount(self):
        self.total1+=self.total4
    def up_local_total(self):
        self.total4+=self.A
    def up_rbi_total(self):
        self.total += self.A
    def withdraw(self,a,b):
        if b=="W" and self.A==0:
            self.A=-a
        elif b=="D" and self.A==0:
            self.A+=a
        elif b=="W" and self.A!=0:
            self.A=-a
        elif b=="D" and self.A!=0:
            self.A+=a

jo=tamilnadu()
print(jo.total,jo.total1,jo.total2)
jo.withdraw(700,"W")
jo.up_local_total()
jo.up_total_amount()
jo.up_rbi_total()
print(jo.total,jo.total1,jo.total2)
#with open(r"C:\Users\91962\OneDrive\Documents\jo.txt","w+") as b:
#    b.writelines(list([str(jo.total)+',',str(jo.total1)+',',str(jo.total2)+'\n']))
# = f[0].split(',')
#jo=tamilnadu()
#print(f)
#jo.total=int(f[0])
#jo.total1=int(f[1])
#jo.total2=int(f[2].replace('\n',''))

tony=kerala()
print(tony.total,tony.total1,tony.total3)
tony.withdraw(80,"W")
tony.up_local_total()
tony.up_total_amount()
jo.up_rbi_total()
print(tony.total,tony.total1,tony.total3)
#with open(r"C:\Users\91962\OneDrive\Documents\jo.txt","w+") as b:
#    b.writelines(list([str(tony.total)+',',str(tony.total1)+',',str(tony.total3)+'\n']))
#with open(r"C:\Users\91962\OneDrive\Documents\jo.txt","r") as b:
#    f=b.readlines()
#f = f[0].split(',')
#tony=kerala()
#print(f)
#tony.total=int(f[0])
#tony.total1=int(f[1])
#tony.total3=int(f[2].replace('\n',''))


cat =mumbai()
print(cat.total,cat.total1,cat.total4)
cat.withdraw(100,"D")
cat.up_local_total()
cat.up_total_amount()
jo.up_rbi_total()
print(cat.total,cat.total1,cat.total4)
#with open(r"C:\Users\91962\OneDrive\Documents\jo.txt","w+") as b:
#    b.writelines(list([str(cat.total)+',',str(cat.total1)+',',str(cat.total4)+'\n']))
#with open(r"C:\Users\91962\OneDrive\Documents\jo.txt","r") as b:
#    f=b.readlines()
#f = f[0].split(',')
#cat=mumbai()
#print(f)
#cat.total=int(f[0])
#cat.total1=int(f[1])
#cat.total4=int(f[2].replace('\n',''))
