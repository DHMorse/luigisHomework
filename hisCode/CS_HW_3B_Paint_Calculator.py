# CS_HW_3B_Paint_Calculator
# Luke Norvell

def calculate_paint(width, height):
    print("Area =",(width*height),"square feet")
    print((width*height/350),"gallons of paint required")

print("Paint Calculator")
width = float(input("Width in feet? "))
height = float(input("Height in feet? "))
print("")
calculate_paint(width, height)