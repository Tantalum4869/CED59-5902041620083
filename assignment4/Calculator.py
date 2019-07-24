print("••••••••••CALCULATOR•••••••••••")
x = int(input("PLEASE ENTER VALUE X : "))
sign = ["+", "-", "*", "/"]
typing = input("PLESE SELECT OPERATOR +, -, *, / : ")
y = int(input("PLEASE ENTER VALUE Y : "))

class cal():
  x = 0
  y = 0
  def __init__(self, input_x,input_y):
    self.x = input_x
    self.y = input_y

  def plus(self):
    result = self.x + self.y
    print("   RESULT IS", self.x ,"+", self.y ,"=", result)
  def sub(self):
    result = self.x - self.y
    print("   RESULT IS", self.x ,"-", self.y ,"=", result)
  def mul(self):
    result = self.x * self.y
    print("   RESULT IS", self.x ,"x", self.y ,"=", result)
  def div(self):
    result = self.x / self.y
    print("   RESULT IS", self.x ,"/", self.y ,"=", result)

cal = cal(x, y)

if typing in sign:
  print("••••••••••YOUR ANSWER•••••••••••")
  if typing == "+":
    cal.plus()
  elif typing == "-":
    cal.sub()
  elif typing == "*":
    cal.mul()
  elif typing == "/":
    cal.div()
else:
  print("ERROR!•••PLEASE TRY AGAIN!!!")

#print("••••••••••CHAIYASIT 20083•••••••••••")

