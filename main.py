from flask import Flask 
app = Flask(__name__) 

users = {}
messagges = {}

def userExists(name):
   return name in users.keys()

def checkPass(name, password):
   return userExists(name) and users[name] == password

# routing the decorator function hello_name 
@app.route('/register/<name>/<password>')   
def register(name, password): 
   if name not in users.keys():
      users[name] = password
      messagges[name] = []
      return "Registration completed successfully!"
   else:
      return "User name already exists :("
   
@app.route('/delete/<name>/<password>')  
def delete(name, password):
   if checkPass(name, password):
      del users[name]
      return "User deleted successfully!"
   else:
      return "User name not exists or invalid passowrd!"

@app.route('/message/<name>/<password>/<dest>/<message>')
def message(name, password, dest, message):
   if checkPass(name, password):
      if userExists(dest):
         messagges[dest].append(tuple(name, message))
         return "message sent successfully"
      else:
         return "Dest not exists :("
   return "User name not exists or invalid passowrd!"

if __name__ == '__main__': 
   app.run(debug = True) 