from flask import Flask,render_template,request
from flask import session
import json  #v2 reg 
import numpy as np  #v3
# import cv2 #v3
import os #v3
app=Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index():
	if request.method =='POST':
		if request.values['send']=='送出':
			return render_template('index.html',inputName=request.values['user'])
	return render_template('index.html',inputName="")

@app.route('/album')
def test():
	basepath = os.path.join(os.path.dirname(__file__), 'static','uploads') #v3
	# os.mkdir(os.path.join(basepath,request.values['userid']))
	#upload_path = os.path.join(basepath) #v3
	#image=cv2.imread(upload_path) #v3
	dirs=os.listdir(os.path.join(basepath)) #v3
	#files=dict2
	return render_template('album.html',dirs=dirs) #v3

# @app.route('/register')
# def to_register():
# 	return render_template('register.html')

@app.route('/register',methods=['POST','GET']) #v2 reg 
def register():
	with open('./member.json','r') as file_object:
		member = json.load(file_object)
	if request.method=='POST':
		if request.values['send']=='送出':
			if request.values['userid'] in member:
				for find in member:
					if member[find]['nick']==request.values['username']:
						return render_template('register.html',alert='this account and nickname are used.')
				return render_template('register.html',alert='this account is used.',nick=request.values['username'])
			else:
				for find in member:
					if member[find]['nick']==request.values['username']:
						return render_template('register.html',alert='this nickname are used.',id=request.values['userid'],pw=request.values['userpw'])
				member[request.values['userid']]={'password':request.values['userpw'],'nick':request.values['username']}
				with open('./member.json','w') as f:
					json.dump(member, f)
				return render_template('index.html')
	return render_template('register.html')

if __name__ == '__main__':
	app.run(port='5000',debug=True)