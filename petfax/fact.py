from flask import ( Blueprint, render_template, redirect, request )

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/', methods=["POST"])
def index():
    if
        print(request.form)
        return redirect('/facts')
    else:
        return 'This is the facts index'
    
@bp.route('/new')
def new():
    return render_template('facts/new.html')