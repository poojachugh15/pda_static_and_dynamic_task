### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
  

# missing The == operator compares the value or equality of two objects.
  def check_for_ace(self, card):
    if card.value = 1: # it should be if card.value == 1:
      return True
    else      #Here, it should be colon after else:
      return False
   
#  Spelling mistake dif, it should be def and there shoud be comma after card1,
  dif highest_card(self, card1 card2): 
  if card1.value > card2.value: # here, it is an indent error.
    return card1 
  else:
    return card2  
  

# first line of method,here it is an indent error.
def cards_total(self, cards):
  total   #this should be total = 0 because total is not associated with anything.
  for card in cards:
    total += card.value
    return "You have a total of" + total #here again, an indent error. and total should be convert into str(total).
   
  
```
