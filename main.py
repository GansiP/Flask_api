from flask import Flask, jsonify, abort,request

rest_api = Flask(__name__)

@rest_api.route('/')
def api_root():
    return 'Welcome to CMS Ticket Type'

if __name__ == '__main__':                                                      
    rest_api.run(debug=True)
