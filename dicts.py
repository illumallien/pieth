

def main():
  ## Can build up a dict by starting with the the empty dict {}
  ## and storing key/value pairs into the dict like this:
  ## dict[key] = value-for-that-key
  dict = {}
  dict['a'] = 'alpha'
  dict['g'] = 'gamma'
  dict['o'] = 'omega'

  print(dict) ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

  print(dict['a'])     ## Simple lookup, returns 'alpha'
  dict['a'] = 6       ## Put new key/value into dict
  'a' in dict         ## True
  ## print(dict['z'])                  ## Throws KeyError
  if 'z' in dict: print(dict['z'])     ## Avoid KeyError
  print(dict.get('z'))  ## None (instead of KeyError)

  for key in dict: print(key) #prints a g

  for key in dict.keys(): print(key) #ssssssame

  print(dict.keys()) #ssssssssssame

  for key in dict.values(): print(key)

  print(dict.values())

  ## Common case -- loop over the keys in sorted order,
  ## accessing each key/value
  for key in sorted(dict.keys()):
    print(key, dict[key])


  ## .items() is the dict expressed as (key, value) tuples
  print(dict.items())  ##  dict_items([('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')])

  ## This loop syntax accesses the whole dict by looping
  ## over the .items() tuple list, accessing one (key, value)
  ## pair on each iteration.
  for k, v in dict.items(): print(k, '>', v)
  ## a > alpha    o > omega     g > gamma    #vay anasını bunu aklında tut


  h = {}
  h['word'] = 'garfield'
  h['count'] = 42
  s = 'I want %(count)d copies of %(word)s' % h  # %d for int, %s for string
  # 'I want 42 copies of garfield'

  # You can also use str.format().
  s = 'I want {count:d} copies of {word}'.format(h)

  var = 6
  del var  # var no more!

  list = ['a', 'b', 'c', 'd']
  del list[0]     ## Delete first element
  del list[-2:]   ## Delete last two elements
  print(list)      ## ['b']

  dict = {'a':1, 'b':2, 'c':3}
  del dict['b']   ## Delete 'b' entry
  print(dict)      ## {'a':1, 'c':3}

  # Echo the contents of a text file
  f = open('foo.txt', 'rt', encoding='utf-8')
  for line in f:   ## iterates over the lines of the file
    print(line, end='')    ## end='' so print does not add an end-of-line char
                           ## since 'line' already includes the end-of-line.
  f.close()

  """Reading one line at a time has the nice quality that not all the file needs to fit in memory at one time --
  handy if you want to look at every line in a 10 gigabyte file without using 10 gigabytes of memory. The f.readlines()
   method reads the whole file into memory and returns its contents as a list of its lines. The f.read() method reads the
   whole file into a single string, which can be a handy way to deal with the text all at once, such as with regular
   expressions we'll see later.

   For writing, f.write(string) method is the easiest way to write data to an open output file. Or you can use "print" with
   an open file like "print(string, file=f)"."""

  with open('foo.txt', 'rt', encoding='utf-8') as f:
    for line in f:
    # here line is a *unicode* string

  with open('write_test', encoding='utf-8', mode='wt') as f:
    f.write('\u20ACunicode\u20AC\n') #  €unicode€
    # AKA print('\u20ACunicode\u20AC', file=f)  ## which auto-adds end='\n'






























if __name__ == '__main__':
  main()
