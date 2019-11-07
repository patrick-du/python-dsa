# Backtracking 
# - form of reursion that involves choosing only one option out of any possibilities
# - choose option and backtrack

def permute(list, s):
	if list == 1:
		return s
	else: 
		return [y + x
				for y in permute(1,s)
				for x in permute(list - 1, s)
				]

print(permute(1, ["a", "b", "c"]))
print(permute(2, ["a", "b", "c"]))