
def objtomodel():
  
  tscale = input("Enter the scale you want to calculate (as a whole number, drop the 1/): ")
  while True:
    try:
        scale = float(tscale)
        break
    except:
        tscale = input("That did not parse. Please Enter the scale you want to calculate: ")    
        pass

  sttruedimension = input("Enter the length of what you want to scale down in M:  ")
  while True:
    try:
        truedimension = float(sttruedimension)
        break
    except:
        sttruedimension = input("That did not parse. Please attempt input again:  ")    
        pass
  smallsize = (truedimension / scale)
  print("Your final size in CM: " + str(smallsize * 100))

def modeltoobj():
  stsmalldimension = input("Enter the length of what you want to scale up in CM:  ")
  while True:
    try:
        smalldimension = float(stsmalldimension)
        break
    except:
        stsmalldimension = input("That did not parse. Please attempt input again:  ")    
        pass
  stlargedimension = input("Enter the length of the real object in M:  ")
  while True:
    try:
        largedimension = float(stlargedimension)
        break
    except:
        stlargeimension = input("That did not parse. Please attempt input again:  ")    
        pass
  scalefact = largedimension / (smalldimension / 100)
  print("The scale of your model is: 1/" + str(scalefact))

tsel = input("If you want to scale from a real object down to a model, press 1. If you want to scale up a model, press 2.")
while True:
    try:
        sel = int(tsel)
        if sel == 1 or sel == 2:
            break
        tsel = input("You did not give a value of 1 or 2. Please try again: ")

    except:
        tsel = input("That did not parse. Please attempt selection again:  ")    
        pass
if sel == 1:
  objtomodel()
elif sel == 2:
  modeltoobj()
