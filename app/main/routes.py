from app.main import main_bp
from flask import render_template

@main_bp.route('/',methods=['GET'])
@main_bp.route('/index',methods=['GET'])
@main_bp.route('/hello',methods=['GET'])
def hello_world():
    return render_template('hello_world.html')