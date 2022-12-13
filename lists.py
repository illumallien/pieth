

def main():
  ilk = ["alfa", "beta", "delta", "sigma"]
  son = ilk
  ilk[0]= "theon"
  print(son) #ilk ve son hafızadaki aynı listeye işaret ediyor. Biri değişince diğeri de değişiyor.
  roll= ["give you up", "let you down", "run around", ]
  for rick in roll:
    print(f'never gonna {rick}')
  print("and desert you")


  list = ['larry', 'curly', 'moe']
  list.append('shemp')         ## append elem at end
  list.insert(0, 'xxx')        ## insert elem at index 0
  list.extend(['yyy', 'zzz'])  ## add list of elems at end
  print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
  print(list.index('curly'))    ## 2

  list.remove('curly')         ## search and remove that element
  list.pop(1)                  ## removes and returns 'larry'
  print(list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']




  list = [1, 2, 3]
  print(list.append(4))   ## NO, does not work, append() returns None
  ## Correct pattern:
  list.append(4)
  print(list)  ## [1, 2, 3, 4]


  list = ['a', 'b', 'c', 'd']
  print(list[1:-1])   ## ['b', 'c']
  list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
  print(list)         ## ['z', 'c', 'd']


  tuple = (1, 2, 'hi')
  print(len(tuple))  ## 3
  print(tuple[2])    ## hi
  tuple[2] = 'bye'  ## NO, tuples cannot be changed
  tuple = (1, 2, 'bye')  ## this works]]


  tuple = ('hi',)   ## size-1 tuple  To create a size-1 tuple, the lone element must be followed by a comma.

  nums = [1, 2, 3, 4]

  squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]

  strs = ['hello', 'and', 'goodbye']

  shouting = [ s.upper() + '!!!' for s in strs ]
  ## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']

## Select values <= 2
  nums = [2, 8, 1, 6]
  small = [ n for n in nums if n <= 2 ]  ## [2, 1]

  ## Select fruits containing 'a', change to upper case
  fruits = ['apple', 'cherry', 'banana', 'lemon']
  afruits = [ s.upper() for s in fruits if 'a' in s ]
  ## ['APPLE', 'BANANA']




if __name__ == '__main__':
  main()
