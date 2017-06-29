from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like dogs %s?" % user_name
likes = raw_input(prompt)

print "Do you like cats %s?" % user_name
cats = raw_input(prompt)

print "Which do you like better?"
better = raw_input(prompt)

print """
Alright, so you said %r about liking dogs.You said
 %r about liking cats. You like  %r better.  Nice so do I.
""" % (likes, cats, better)
