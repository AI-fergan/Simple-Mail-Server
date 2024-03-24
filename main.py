from flask import Flask 
app = Flask(__name__) 

users = {}
messagges = {}

def userExists(name):
   return name in users.keys()

def checkPass(name, password):
   return userExists(name) and users[name] == password

@app.route('/')   
def start(): 
   return "Welcome to my simple mail server :)"
 
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
         messagges[dest].append(tuple([name, message]))
         return "message sent successfully"
      else:
         return "Dest not exists :("
   return "User name not exists or invalid passowrd!"

@app.route('/home/<name>/<password>')
def home(name, password):
   home = []
   if checkPass(name, password):
      home.append("<b>" + name + "</b><br>")
      for message in messagges[name]:
         home.append("From: " + message[0] + "<br>" + message[1])
      return '<br><br>'.join(home)
   else:
      return "User name not exists or invalid passowrd!"
   
if __name__ == '__main__': 
   app.run(debug = True) 