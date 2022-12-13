
def main():

    raw=r'bok,sssss'
    looow= raw.lower()
    uup=raw.upper()
    somebodycomegether=raw.strip()
    yep=raw.startswith('b0')
    nope=raw.endswith('k')
    where= raw.find("ok")
    tochange= "selam ben rabia. Benim adımı nicin rabia koymuslar? bilmiyorum ama rabia koymuslar."
    ayir=raw.split(',')
    bol=raw[1:4]
    basisil= raw[1:] #birden basla devamini al

    yappistir='hehe'.join(['yook', 'artiiik', 'ceeem']) #also nice
    alprn=tochange.replace("rabia","alperen") #vayt baya begendim
    print(where)

    if yep:
        print('yup starts with bo')
    if nope:
        print("noope doesn't end with ko")  #stup

#f strings

    address_book = [{'name':'N.X.', 'addr':'15 Jones St', 'bonus': 70},
        {'name':'J.P.', 'addr':'1005 5th St', 'bonus': 400},
        {'name':'A.A.', 'addr':'200001 Bdwy', 'bonus': 5},]

    for person in address_book:
      print(f'{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}')

    # N.X.     || 15 Jones St          ||    70
    # J.P.     || 1005 5th St          ||   400
    # A.A.     || 200001 Bdwy          ||     5


      # % operator
      # %d = int   %s = string   %f, %g = float
    text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')

    # Add parentheses to make the long line work:
    #use () [] or {}
    text = (
      "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down."
      % (3, 'huff', 'puff', 'house'))

      # Split the line into chunks, which are concatenated automatically by Python
    text = (
      "%d little pigs come out, "
      "or I'll %s, and I'll %s, "
      "and I'll blow your %s down."
      % (3, 'huff', 'puff', 'house'))



    #bytes and unicode
    bite = b'bite me' #byte
    nevermind = bite.decode('utf-8') #utf-8
    okokbite = nevermind.encode('utf-8') #byte


    #if else boolean etc.
    if time_hour >= 0 and time_hour <= 24:
        print('Suggesting a drink option...')
    if mood == 'sleepy' and time_hour < 10:
        print('coffee')
    elif mood == 'thirsty' or time_hour < 2:
        print('lemonade')
    else:
        print('water')









if __name__ == '__main__':
    main()
