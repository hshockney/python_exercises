my_name = 'Heather C. Shockney'
my_age = 39 # not a lie
my_height = 64 # inches
my_weight = 0 # lbs
my_eyes = 'Blue'
my_color = 'Purple'
my_hair = 'Blonde'

print "Let's talk about %s." % my_name
print "She's %d inches tall." % my_height
print "She's %d pounds heavy." % my_weight
print "Actually that's impossible."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her favorite color is %s." % my_color

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
