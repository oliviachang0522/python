scores=[99,100,38,94,90]
friends=["olivia","kiki","nana","yoyo","cathy"]
thing=[99,"olivia",True]
print(scores[1:3]) 
scores[2]=50
scores.extend(friends)
scores.append(77)
scores.remove(90)
scores.insert(3,67)
scores.pop()

scores.sort()
scores.reverse()
print(scores.count(100))





print(scores)
scores.clear()

