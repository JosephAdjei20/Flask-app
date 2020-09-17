from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def index():  
    return "hello, this is Joey's first flask website";  

    
  
if __name__ =='__main__':  
    app.run(debug = True)  
