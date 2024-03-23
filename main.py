from flask import Flask 
app = Flask(__name__) 

users = {}

# routing the decorator function hello_name 
@app.route('/register/<name>/<password>')   
def register(name, password): 
   if name not in users.keys():
      users[name] = password
      return "Registration completed successfully!"
   else:
      return "User name already exists :("
  
if __name__ == '__main__': 
   app.run(debug = True) 