from abc import ABC,abstractmethod
'''
class E(metaclass=ABCMeta):
    def __init__(self,e_id):
        self.e_id=e_id
    @abstractmethod
    def monthely_sal(self):
        print("hi how r u")
    @abstractmethod
    def ms(self):
        return self.e_id
class T(E):
    def __init__(self,e_id,b_name):
        super().__init__(e_id)
        self.__b_name=b_name
    def getn(self):
        return self.__b_name
        
d=E(3)
b=T(2,'anshu')
b.monthely_sal()
d.ms()
print(b.getn())
'''
class shape(ABC):
    def diag(self):
        print("this is base method")
    @abstractmethod
    def poly(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass
class triangle(shape):
    def __init__(self,height,base,hypataneous):
        self.__height=height
        self.__base=base
        self.__hyp=hypataneous
    def poly(self):
        return 'this is right anlge triangle'
    def area(self):
        return 0.5*self.__base*self.__height
    def perimeter(self):
        return self.__height+self.__base+self.__hyp
class square(shape):
    def __init__(self,side1):
        self.__side1=side1
    def poly(self):
        return 'this is 4 sided polygon'
    def area(self):
        return self.__side1*self.__side1
    def perimeter(self):
        return 4*self.__side1
class rectangle(shape):
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    def poly(self):
        return 'this is rectangle'
    def area(self):
        return self.__length*self.__breadth
    def perimeter(self):
        return 2*(self.__length+self.__breadth)

t=triangle(2,3,4)
print(t.poly())
print(t.area())
print(t.perimeter())
sq=square(4)
print(sq.poly())
print(sq.area())
print(sq.perimeter())
r=rectangle(3,4)
print(r.poly())
print(r.area())
print(r.perimeter())
