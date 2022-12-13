import re



def main():
  str = 'an example word:cat!!'
  match = re.search(r'word:\w\w\w', str)
  # If-statement after search() tests if it succeeded
  if match:
    print('found', match.group()) ## 'found word:cat'
  else:
    print('did not find')


"""

    a, X, 9, < -- ordinary characters just match themselves exactly. The meta-characters which do not match
    themselves because they have special meanings are:
    . ^ $ * + ? { [ ] \ | ( ) (details below)
    . (a period) -- matches any single character except newline '\n'
    \w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. Note that although
    "word" is the mnemonic for this, it only matches
     a single word char, not a whole word. \W (upper case W) matches any non-word character.
    \b -- boundary between word and non-word
    \s -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form [ \n\r\t\f]. \S
    (upper case S) matches any non-whitespace character.
    \t, \n, \r -- tab, newline, return
    \d -- decimal digit [0-9] (some older regex utilities do not support \d, but they all support \w and \s)
    ^ = start, $ = end -- match the start or end of the string
    \ -- inhibit the "specialness" of a character. So, for example, use \. to match a period or \\ to match a slash.
     If you are unsure if a character has special meaning,
    such as '@', you can try putting a slash in front of it, \@. If its not a valid escape sequence, like \c, your
    python program will halt with an error.


"""

  ## Search for pattern 'iii' in string 'piiig'.
  ## All of the pattern must match, but it may appear anywhere.
  ## On success, match.group() is matched text.
  match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
  match = re.search(r'igs', 'piiig') # not found, match == None

  ## . = any char but \n
  match = re.search(r'..g', 'piiig') # found, match.group() == "iig"

  ## \d = digit char, \w = word char
  match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
  match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"



  ## i+ = one or more i's, as many as possible.
  match = re.search(r'pi+', 'piiig') # found, match.group() == "piii"

  ## Finds the first/leftmost solution, and within it drives the +
  ## as far as possible (aka 'leftmost and largest').
  ## In this example, note that it does not get to the second set of i's.
  match = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"

  ## \s* = zero or more whitespace chars
  ## Here look for 3 digits, possibly separated by whitespace.
  match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # found, match.group() == "1 2   3"
  match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found, match.group() == "12  3"
  match = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, match.group() == "123"

  ## ^ = matches the start of string, so this fails:
  match = re.search(r'^b\w+', 'foobar') # not found, match == None
  ## but without the ^ it succeeds:
  match = re.search(r'b\w+', 'foobar') # found, match.group() == "bar"


  str = 'purple alice-b@google.com monkey dishwasher'   #suppose you want to find the e mail address
  match = re.search(r'[\w.-]+@[\w.-]+', str)
  if match:
    print(match.group())  ## 'alice-b@google.com'



"""
(More square-bracket features) You can also use a dash to indicate a range,
so [a-z] matches all lowercase letters. To use a dash without indicating a
range, put the dash last, e.g. [abc-]. An up-hat (^) at the start of a square-bracket
 set inverts it, so [^ab] means any char except 'a' or 'b'.
"""



  str = 'purple alice-b@google.com monkey dishwasher'
  match = re.search(r'([\w.-]+)@([\w.-]+)', str)
  if match:
    print(match.group())   ## 'alice-b@google.com' (the whole match)
    print(match.group(1))  ## 'alice-b' (the username, group 1)
    print(match.group(2))  ## 'google.com' (the host, group 2)

"""
The "group" feature of a regular expression allows you to pick out parts of
the matching text. Suppose for the emails problem that we want to extract the
username and host separately. To do this, add parenthesis ( ) around the username
and host in the pattern, like this: r'([\w.-]+)@([\w.-]+)'. In this case, the
 parenthesis do not change what the pattern will match, instead they establish logical
  "groups" inside of the match text. On a successful search, match.group(1) is the match
  text corresponding to the 1st left parenthesis, and match.group(2) is the text
  corresponding to the 2nd left parenthesis. The plain match.group() is still the
  whole match text as usual.


"""

#FINDALL

"""
findall() is probably the single most powerful function in the re module.
 Above we used re.search() to find the first match for a pattern. findall()
 finds *all* the matches and returns them as a list of strings, with each
 string representing one match.

"""


  ## Suppose we have a text with many email addresses
  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

  ## Here re.findall() returns a list of all the found email strings
  emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
  for email in emails:
    # do something with each found email string
    print(email)


  # Open file
  f = open('test.txt', 'r')
  # Feed the file text into findall(); it returns a list of all the found strings
  strings = re.findall(r'some pattern', f.read())

"""
The re functions take options to modify the behavior of the pattern match.
The option flag is added as an extra argument to the search() or findall()
etc., e.g. re.search(pat, str, re.IGNORECASE).

    IGNORECASE -- ignore upper/lowercase differences for matching, so 'a'
     matches both 'a' and 'A'.
    DOTALL -- allow dot (.) to match newline -- normally it matches anything
    but newline. This can trip you up -- you think .* matches everything, but
     by default it does not go past the end of a line. Note that \s (whitespace)
      includes newlines, so if you want to match a run of whitespace that may
      include a newline, you can just use \s*
    MULTILINE -- Within a string made of many lines, allow ^ and $ to match the
     start and end of each line. Normally ^/$ would just match the start and end
     of the whole string.
"""


"""
This is optional section which shows a more advanced regular expression
technique not needed for the exercises.

Suppose you have text with tags in it: <b>foo</b> and <i>so on</i>

Suppose you are trying to match each tag with the pattern '(<.*>)'
-- what does it match first?

The result is a little surprising, but the greedy aspect of the .*
causes it to match the whole '<b>foo</b> and <i>so on</i>' as one big
 match. The problem is that the .* goes as far as is it can, instead of
  stopping at the first > (aka it is "greedy").

There is an extension to regular expression where you add a ? at the
end, such as .*? or .+?, changing them to be non-greedy. Now they stop
as soon as they can. So the pattern '(<.*?>)' will get just '<b>' as the
first match, and '</b>' as the second match, and so on getting each <..>
pair in turn. The style is typically that you use a .*?, and then immediately
its right look for some concrete marker (> in this case) that forces the end
of the .*? run.

The *? extension originated in Perl, and regular expressions that include Perl's
extensions are known as Perl Compatible Regular Expressions -- pcre. Python includes
pcre support. Many command line utils etc. have a flag where they accept pcre patterns.

An older but widely used technique to code this idea of "all of these chars except
stopping at X" uses the square-bracket style. For the above you could write the pattern,
but instead of .* to get all the chars, use [^>]* which skips over all characters which
are not > (the leading ^ "inverts" the square bracket set, so it matches any char not
in the brackets).
"""

  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
  ## re.sub(pat, replacement, str) -- returns new string with all replacements,
  ## \1 is group(1), \2 group(2) in the replacement
  print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
  ## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher








if __name__ == '__main__':
  main()
