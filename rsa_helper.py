stuff = 'hello'
print("here's the stuff:", stuff)
print("is this alpha?", stuff.isalpha())
print("is this a digit?", stuff.isdigit())



# --- combine this with input ---
ans = ''
while not ans.isalpha():
  ans = input("\ntype letters only:")



# --- what if too short?? ---
ans = ''
while len(ans) < 8 or not ans.isalpha():
  ans = input("\ntype at least 8 letters: ")
  
