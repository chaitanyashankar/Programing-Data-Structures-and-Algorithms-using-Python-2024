#week3

#Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the first occurrence of each number

def remdup(seq):
    seen = set()  # Create an empty set to keep track of seen elements
    result = []   # Initialize an empty list to store the unique elements
    for item in seq:  # Iterate through each item in the input sequence
        if item not in seen:  # Check if the current item is not in the set of seen elements
            result.append(item)  # If not seen before, add the item to the result list
            seen.add(item)  # Add the item to the set of seen elements
    return result  # Return the list containing only unique elements


seq = [1, 2, 7, 7, 8, 3, 3]
print(remdup(seq))

#Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers in l and even is the sum of squares of all the even numbers in l.

def sumsquare(l):
    lise = []
    e, o = 0, 0
    for i in range(0, len(l)):
        if l[i]%2 == 0:
            e = e + l[i]**2
        else:
            o = o + l[i]**2
    lise.append(o)
    lise.append(e)
    return lise

#Transpose of a matrix

def transpose(l):
  outl = []
  for row in l[:1]:
    for i in range(len(row)):
      outl.append([])
  for row in l:   
    for i in range(len(row)):
      outl[i].append(row[i])
  return(outl)


                



            


