from ipaddress import ip_address
# from flask import Flask
import subprocess

# app = Flask(__name__)


# @app.route("/ping/<ip>")
def ping(ip):
    try:
        ip = ip_address(ip)
        cmd = f"ping -c 4 {ip}"
        res = subprocess.run(["/bin/bash", "-c", cmd], stdout=subprocess.PIPE)
        return res.stdout.decode(errors="ignore")
    except ValueError:
        return "Invalid IP address"
    except:
        return "An error occurred"


# @app.route("/")
# def index():
#     response = app.response_class()
#     response.status_code = 200
#     response.mimetype = "text/html"
#     response.data = open("index.html").read()
#     return response


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000)
    ip = input("Enter IP address: ")
    print(ping(ip))
