def calculator(num1,operator,num2):
   if operator=="+":
     return num1+num2
   elif operator=="-":
      return num1-num2
   elif operator=="*":
      return num1*num2
   elif operator=="/":
      return num1/num2
   else:
      return "Math Error"

while True:
   try:
      num1=float(input("enter your first number:"))
      operator=input("enter your operator(+,-,*,/):")
      num2=float(input("enter your second number:"))

      Answer=calculator(num1,operator,num2)
      print("Answer:", Answer)


   except ValueError:
      print("please correct your input (only numbers and operators are allowed)")


   choice=str(input("continiue?(yes or no):").lower())
   if choice.lower()=="no":       
      print("closed")
      break   
