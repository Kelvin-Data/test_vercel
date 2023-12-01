from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "HELLO FROM VERCEL"

if __name__ == '__main__':
    app.run(port=5000,debug=True)
 
# cd vercel_deployment   
# ls
# vercel .