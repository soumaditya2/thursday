from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def soumya():  
    return "<h1>We are from FIEM </h1>";  
  
if __name__ =='__main__':  
    app.run()  



