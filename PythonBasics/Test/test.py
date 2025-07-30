print(int('0b101', 2)) # 0b101 is binary representation, 2 means base 2. 

isBlabla = True
print(f"Is it blabla? {isBlabla}")
dictionary = {
    'a': 1,
    'b': 2,
    'x': 3
}
print(dictionary)

amazonCart = [
    "notebooks", 
    "sunglasses", 
    "toys",
    "grapes"]

print(f"{amazonCart[-3:]} is the last item in the cart") #-3 means take a slice from the third last item to the end.

print(amazonCart[0])

### LIST SLICING
print(amazonCart)
print(amazonCart[0:2:2])
amazonCart[0] = "laptop" #List is mutable. Meaning, it can change unlike String.
print(amazonCart[1:3])
print(amazonCart)

new_cart = amazonCart; 
new_cart = amazonCart[:] # Create a copy using slicing. And these 2 points to different objects in memory
new_cart[0] = "gum"
print(new_cart) # ["gum", "sunglasses", "toys", "grapes"]
print(amazonCart) # ["latop", "sunglasses", "toys", "grapes"]

basket = [1, 2, 3, 4, 5]
print(len(basket))

new_list = basket.append("Chris Bui")
basket.append("Chris Bui") # If I do print new_list right here, the result is None because the append() doesn't return a new list.
print(basket)

example_list = [1, "a", 3, "b", 5]
print(type(example_list)) # -> list
# List
print(example_list[:])
#[1, "a", 3, "b", 5]
print(example_list[1:4]) # Slicing from index 1 to 4, with step 1. In this case, exclude index 4.
# a, 3, b
print(example_list[1:4:2]) # Slicing from index 1 to 4, with step 2. In this case, exclude index 4.
#a, b
print(example_list[::2]) # Slicing from index 0 to the end, with step 2. In this case, exclude index 4.
#1, 3, 5
print(example_list[::-1]) # Reverse the list
#reverse the list

print(example_list.item())