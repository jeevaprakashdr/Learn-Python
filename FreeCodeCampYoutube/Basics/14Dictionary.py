monthConversions = {
    "jan" : "january",
    "feb" : "february",
    "mar" : "march",
    12 : "number key with value"
}


print(monthConversions)
print(monthConversions["jan"])
print(monthConversions.get("jan"))
print(monthConversions.get("key", "not a valid key"))

print(monthConversions.get(12))

