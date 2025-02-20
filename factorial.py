from flask import Flask, request

app = Flask(__name__)

@app.route("/factorial",methods=["POST"])
def endpoint():
  js = request.get_json()
  argument = js.get("argument")
  if argument != None:
    result = calculate(argument)
    return {"result":result},200 # OK
  else:
    return "",400 # Bad Request

def calculate(n):
    if n <= 0:
        return 1
    result = 1
    while n > 0:
        result *= n
        n -= 1
    
    return result

if __name__ == "__main__":
  app.run(host="localhost",port=3000)
