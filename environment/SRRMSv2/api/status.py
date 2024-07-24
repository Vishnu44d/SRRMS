from flask import Blueprint

statusBP = Blueprint('StatusAPI', __name__)
#Added a comment -Ayush
@statusBP.route('/', methods=['GET', 'POST'])
def get_status():
    return 'abc'