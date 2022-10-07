
lucky_numbers = [234, 23, 5, 54, 67, 34, 12, 5, 7, 12]
friends = ["c#", "javascript", "python", "rust", "go", "nodejs"]
print(lucky_numbers)
print(friends)

friends.extend(lucky_numbers)
print(friends)

friends.append(23452)
print(friends)

friends.insert(4, "ruby")
print(friends)

friends.remove("ruby")
print(friends)

print(friends.pop())
print(friends)

print(friends.index("go"))

print(friends.insert(4, "ruby"))
print(friends.insert(4, "ruby"))
print(friends.count("ruby"))
print(len(friends))

lucky_numbers.reverse()
print(lucky_numbers)
lucky_numbers.sort(reverse=True)
print(lucky_numbers)

friends_copy = friends.copy()
print(friends_copy)


