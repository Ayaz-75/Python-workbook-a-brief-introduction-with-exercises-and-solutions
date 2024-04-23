
# Exercise 8: Widgets and Gizmos

'''
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos from the user. Then your program should compute
and display the total weight of the parts

'''

def find_wizmos(widg_w8, gizmo_w8): # widg_w8 = widget weighs, gizmo_w8 = gizmo weighs
    total_weight = widg_w8 + gizmo_w8
    return total_weight


weight_of_widgits = float(input("Enter the weight of widgits: "))
weight_of_gizmos = float(input("Enter the weight of gizmos: "))

print("total weight is: ",find_wizmos(weight_of_widgits, weight_of_gizmos))
