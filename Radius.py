import math
radius = float( input(("Enter radius: ")))
Pi=math.pi
volume= (4/3)* Pi * (radius**3)
formatted_volume= round(volume,3)

print(f"Volume of Sphere with {radius} cm is {formatted_volume}cm³")

