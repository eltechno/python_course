

world = { "afganistan": 30.55,
          "albania": 2.77,
          "algera" : 39.21
          }

for key, value in world.items():
    print(key + " --- ", str(value))



# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for x, y in europe.items():
    print("The capital of " + x + " is " + y)