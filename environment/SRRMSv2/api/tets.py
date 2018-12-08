from flask import Blueprint

testBP = Blueprint('TestAPI', __name__)

@testBP.route('/', methods=['GET', 'POST'])
def get_status():
    return 'xyz'