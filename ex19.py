def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

def chips_and_dip(bags_of_chips, containers_of_dip):
    print "You have %d bags of chips." % bags_of_chips
    print "You have %d containers of dip." % containers_of_dip
    print "Are you having company?"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
chips_and_dip(15, 20)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
amount_of_chips = 20
amount_of_dips = 30
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
chips_and_dip(amount_of_chips, amount_of_dips)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
chips_and_dip(5 + 6, 4 + 8)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
chips_and_dip(amount_of_chips + 20, amount_of_dips - 10)
