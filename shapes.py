
from cmath import pi
import math

#Question_one
class Circle:

  #radius (r)
    def __init__(self):
        self.radius=float(input("Enter radius(r): "))


   #formula A=πr2
    def area_of_circle(self):
        return math.pi* self.radius * self.radius 

   #formula C=2πr  
    def circumference_of_circle(self):
        return 2* math.pi* self.radius



 #Question_two
class Square:

  #side (a)
    def __init__(self):
        self.a = float(input("Enter side(a): "))


  #formula A=a2
    def area_of_square(self):
       return  self.a * self.a

  #formula P=4a 
    def perimeter_of_square(self):
       return  4* self.a


       
# #Question_three
class Rectangle:

  #(w,l)
      def __init__(self):
        self.w = float(input("Enter width(w): "))
        self.l = float(input("Enter lenght(l): "))

        
  #A=wl
      def area_of_rectangle(self):
           return  self.w* self.l

  #formula P=2(l+w)      
      def perimeter_of_rectangle(self):
           return 2*(self.l + self.w)



# #Question_four
class Sphere:

  #sphere (r)
      def __init__(self):
        self.r = float(input("Enter (r): "))


  #formula A=4πr2
      def surfaceArea_of_sphere(self):
          return 4* math.pi* self.r* self.r

  #formula V = 4/3(πr3)      
      def volume_of_sphere(self):
          return 4/3*(math.pi* self.r* self.r* self.r)
   