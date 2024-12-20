# CS_HW_2E_Cubes
# Luke Norvell
# Get all of the cubes from 1 to 50
print("Perfect cubes")

cubed = 0
cubed_result = 0
cubed_list = []
display = 0

for cubed in range(1,51):
    cubed_result = cubed**3
    cubed_list.append(cubed_result)
    cubed = cubed + 1

for display in range(0,50):
    print(display+1, "cubed =", cubed_list[display])
    display = display + 1