import re

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''


pattern = '\W'

results = re.findall(pattern,lorem_ipsum) #search for literal characters that are non alphanumeric

print(len(results))

pattern = 'sit[-:]amet'

occurrance_sit_amet = re.findall(pattern,lorem_ipsum) #search for a pattern in lorem_ipsum that begin with 'sit' and 'amet'

print(len(occurrance_sit_amet))

pattern = '[:-]'

sub = ' '

replace_results = re.sub(pattern,sub,lorem_ipsum) #search for within lorem_ipsum for any ':' or '-' and replace with a ' '

occurrance_sit_amet = re.findall('sit amet',replace_results)

print(len(occurrance_sit_amet))
