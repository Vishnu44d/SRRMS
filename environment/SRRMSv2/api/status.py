from flask import Blueprint

statusBP = Blueprint('StatusAPI', __name__)

@statusBP.route('/', methods=['GET', 'POST'])
def get_status():
    return 'abc'