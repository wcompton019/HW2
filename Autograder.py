# Autograder

# This will attempt to perform intended tasks for Stack. It will only use naturals, for simplicity.
# It is not required that your stack work with values other than naturals or only with naturals.
# For each task, the autograder will:
#  - Define some expected behavior for some use case
#  - Perform the use case
#  - Award "points" if the result is as expected
#  - Either not award points (not too bad) or cause an error (pretty bad) if the result is not as expected
#    NOTE: Exception handling here could manage these errors, but it can be helpful to see them as well!

# This is a script to do the tests and print out what's happening
def singleTest(desc, target, val, pts):
	print("AUTOGRADER: " + desc)
	print(" - Expected Value: " + str(target))
	print(" - Observed Value: " + str(val))
	score = 0
	if (val == target):
		score = 5
		pts = pts + 5
	print("POINTS: This section: " + str(score).zfill(2) + "/05 Total: " + str(pts).zfill(3) + "/100\n")	
	return pts

points = 0

print("\n --- AUTOGRADER: STACK ---\n")
from stack import Stack
s = Stack()

print("\nAUTOGRADER: Empty Stack Testing: 25 pts\n")
points = singleTest("Checking Stack().empty() is True", True, s.empty(), points)
print(type(s))
print(s.size())
points = singleTest("Checking Stack().size()  is zero", 0, s.size(), points)
points = singleTest("Checking Stack().peek()  is None", None, s.peek(), points)
points = singleTest("Checking Stack().pop()   is None", None, s.pop(), points)
s.push(5)
points = singleTest("Checking Stack() is still a stack after a push.", type(Stack()), type(s), points)

print("\nAUTOGRADER: Singleton Stack Testing: 40 pts\n")
points = singleTest("Checking after push that .empty() is False", False, s.empty(), points)
points = singleTest("Checking after push that .size()  is equal to one", 1, s.size(), points)
points = singleTest("Checking after pushing 5 that .peek() is 5", 5, s.peek(), points)
points = singleTest("Checking that stack is unaltered by peek by checking .size()", 1, s.size(), points)
points = singleTest("Checking that .pop() 5", 5, s.pop(), points)
points = singleTest("Checking that stack is altered by pop by checking .size()", 0, s.size(), points)
points = singleTest("Checking that stack is altered by pop by checking .peek()", None, s.peek(), points)
points = singleTest("Checking that stack is altered by pop by checking .pop()", None, s.pop(), points)


print("\nAUTOGRADER: Order Preservation Testing: 35 pts\n")
s= Stack()
for i in [1,2,3,4,5]:
	s.push(i)
points = singleTest("Checking peek is 5 after adding 1 through 5", 5, s.peek(), points)
points = singleTest("Checking pop is 5", 5, s.pop(), points)
points = singleTest("Checking pop is 4", 4, s.pop(), points)
points = singleTest("Checking pop is 3", 3, s.pop(), points)
s.push(6)
points = singleTest("Checking that after pushing 6, .pop() is 6", 6, s.pop(), points)
points = singleTest("Checking pop is 2", 2, s.pop(), points)
points = singleTest("Checking pop is 1", 1, s.pop(), points)
points = singleTest("Checking pop is None", None, s.pop(), points)


	
