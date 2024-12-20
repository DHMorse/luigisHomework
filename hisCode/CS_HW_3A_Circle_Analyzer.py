# CS_HW_3A_Circle_Analyzer
# Luke Norvell

def analyze_circle(radius):
    print("Circle Info:")
    print("Radius =",radius)
    print("Diameter =",(radius // 2))
    print("Circumference =",(radius*2*3.14159265358979))
    print("Area =",(radius**2*3.14159265358979))

print("Circle Analyzer")
radius = float(input("Radius? "))
print("")
analyze_circle(radius)