# writing a script to communicate with a js file

# import socket

# self_addr = ("localhost", 5000)
# soc = socket.socket()
# soc.bind(self_addr)

# soc.listen()

# while True:
# 	con, addr = soc.accept()

# 	print(f"Connected to {addr}")
# 	req = con.recv(1024)
	
# 	print(req.title())

# 	print("Sending data....")


from flask import Flask, jsonify, request
import sqlite3 as s

app = Flask(__name__)
con = s.connect("dummy1.db")
cur = con.cursor()

try:
	cur.execute(f"SELECT * from EMPLOYEES")
except Exception as e:
	cur.execute(f"CREATE TABLE EMPLOYEES(name, age, address, email)")
finally:
	con.commit()
	con.close()

@app.route("/", methods=["GET"])
def home():
	return jsonify("Hello there !")


@app.route("/", methods=["POST"])
def print_data():
	data = request.get_json()
	con = s.connect("dummy.db")
	cur = con.cursor()
	cur.execute(f"INSERT INTO EMPLOYEES (name, age, address, email) VALUES (?, ?, ?, ?)", tuple(data.values()))
	con.commit()	
	con.close()
	return jsonify("done")


if __name__ == "__main__":
	app.run(host = "localhost", port = 5000)