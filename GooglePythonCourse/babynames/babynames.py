#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -1 Extract the year and print it
 -2 Extract the names and rank numbers and just print them
 -3 Get the names data into a dict and print it
 -4 Build the [year, 'name rank', ... ] list and print it
 -5 Fix main() to use the extract_names list
"""

#Step 1

f = open(name = 'baby1990.html', mode = 'rU') #use 'rU' to read it as the actual string from an html, not some file reference
f_string = f.read()

match_year = re.search('Popularity\sin\s(\d\d\d\d)', f_string)
if match_year:
  print match_year.group(1)
else:
  print 'not found'

#Step 2

match_name = re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)', f_string)
if match_name:
  for triple in match_name:
    print triple[0] + triple[1] + triple[2]

# if match_name:
#   print match_name.group(1)
# else:
#   print 'not found'

#Step 3

dict_1990 = {}
if match_name:
  for triple in match_name:
    dict_1990[triple[1]] = triple[0]
    dict_1990[triple[2]] = triple[0]

dict_1990['Cierra']

#Step 4

list_1990 = []
list_1990.append(match_year.group(1))
for item in dict_1990.items():
  list_1990.append(item[0] + ' ' + item[1])

print list_1990

#ordering

def only_the_name(word_plus_number):
  match = re.search('\S', word_plus_number)
  return match.group()

list_1990_ordered_without_first_number = sorted(list_1990[1:], key = only_the_name)

list_1990_ordered = []
list_1990_ordered.append(list_1990[0])
list_1990_ordered = list_1990_ordered + list_1990_ordered_without_first_number

print list_1990_ordered

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(name=filename, mode='rU')  # use 'rU' to read it as the actual string from an html, not some file reference
  f_string = f.read()

  match_year = re.search('Popularity\sin\s(\d\d\d\d)', f_string)
  if match_year:
    print match_year.group(1)
  else:
    print 'not found'

  # Step 2

  match_name = re.findall('<td>(\d+)</td><td>(\w+)</td><td>(\w+)', f_string)
  if match_name:
    for triple in match_name:
      print triple[0] + triple[1] + triple[2]

  # if match_name:
  #   print match_name.group(1)
  # else:
  #   print 'not found'

  # Step 3

  dict_1990 = {} #naming was not changed, should just be without the year number
  if match_name:
    for triple in match_name:
      dict_1990[triple[1]] = triple[0]
      dict_1990[triple[2]] = triple[0]

  dict_1990['Cierra']

  # Step 4

  list_1990 = []
  list_1990.append(match_year.group(1))
  for item in dict_1990.items():
    list_1990.append(item[0] + ' ' + item[1])

  print list_1990

  # ordering

  def only_the_name(word_plus_number):
    match = re.search('\S', word_plus_number)
    return match.group()

  list_1990_ordered_without_first_number = sorted(list_1990[1:], key=only_the_name)

  list_1990_ordered = []
  list_1990_ordered.append(list_1990[0])
  list_1990_ordered = list_1990_ordered + list_1990_ordered_without_first_number

  print list_1990_ordered

  return

extract_names('baby1990.html')

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    names = extract_names(filename)

    # Make text out of the whole list
    text = '\n'.join(names)

    if summary:
      outf = open(filename + '.summary', 'w')
      outf.write(text + '\n')
      outf.close()
    else:
      print text
  
if __name__ == '__main__':
  main()





