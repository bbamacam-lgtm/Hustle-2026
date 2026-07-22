# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: Breena
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: Vinyls + MP3s
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.
class Vinyl:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        

    def set_price(self, amount):
        if amount < 0:
             print("A price can't be below zero")
        else:
            self.price = amount

    def play(self):
        print("Playing your vinyl on the record player!")


# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: it will say "A price can't be below zero"
#   Paste the message you see here: NameError: SZA - Ctrl A price can't be below zero


# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.

class MP3(Vinyl):
    pass # copies everything

    def play(self):
        print("Downloading and playing your MP3!")

# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: are in different classes



# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: SZA - Ctrl, 20
#   EXPLAIN : prints out only name SZA - Ctrl

item1 = Vinyl("SZA - Ctrl", 20)
print(item1.name)

item2 = MP3("Bruno Mars - The Romantic", 30)


# Ticket 3 test
item1.set_price(-5)

item1.play()
item2.play()

# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.

class Cart:
    def __init__(self):
        self.items = []

    def add(self,item):
        self.items.append(item)

    def checkout(self):
        total = 0
        
        for item in self.items:
            item.play()
            total += item.price

        print("Total: $" + str(total))


# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.



# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.
store = {"1": item1, "2": item2}

cart = Cart()

# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: SZA - Crtl added!

while True:
    choice = input("Pick 1, 2, or 'done':")

    if choice == "done":
        break

    elif choice in store:
        cart.add(store[choice])
        print(store[choice].name + " added!")

    else:
        print("Invalid choice. Try again")

# Ticket 9
cart.checkout()

# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.
# PREDICT: Pick 1, 2, or 'done': 1
#   SZA - Ctrl added!
#   Pick 1, 2, or 'done': 2
#   Bruno Mars - The Romantic added!
#   Pick 1, 2, or 'done': done
#   Total: $50

# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================
