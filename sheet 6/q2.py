import json
users = [
    {"username": "mostafa", "pass": "245vf"},
    {"username": "Ahmed", "pass": "dv5d5v"},
    {"username": "Mohamed", "pass": "vs534"},
    {"username": "Khaled", "pass": "vdkc58"}
        ]
file = open('users.json', 'w')
json.dump(users, file)
file.close()
file = open('users.json', 'r')
users = json.load(file)
file.close()
print(f"First user: {users[0]['username']} , pass: {users[0]['pass']}")
users.append({"username": "Mahmoud", "pass": "m6969"})
file = open('users.json', 'w')
json.dump(users, file)
file.close()
print("User added")
u = input("Username: ")
p = input("Password: ")
file = open('users.json', 'r')
users = json.load(file)
file.close()
x = False
for user in users:
    if user['username'] == u and user['pass'] == p:
        x = True
        break
print("Login Success!" if x else "Login Failed")