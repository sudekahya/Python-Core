print("welcome to the treasure island!")
print("your mission is to find the treasure.")
step_1 = input("you're at a cross road.where do you want to go? type left or right ")

if step_1 == "left":
  print("you come to a lake there is an island in the middle of the lake.")
  step_2 = input("type wait to wait for a boat.type swim to swim across.")
  if step_2 == "wait":
    print("you arrive at the island unharmed. there is a house with 3 doors.")
    step_3 = input("one red, one yellow and one blue which colour do you choose?")
    if step_3 == "red":
      print("it's a room full of fire game over")
    elif step_3 == "yellow": 
      print("you found the treasure!you win!")
    elif step_3 == "blue":
      print("you enter a room of beasts game over")
  else:
    print("you got attacked by an angry trout game over")
else:
  print("you fell into a hole game over")