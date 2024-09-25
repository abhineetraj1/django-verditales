from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
import smtplib,os, pymongo, datetime,shutil
from PIL import Image
from django.core.files.storage import FileSystemStorage

def send_mail(subject,content,toemail):
	server = smtplib.SMTP("localhost",587)
	server.starttls()
	server.login("contact@localhost","2205007")
	server.sendmail("contact@localhost",toemail,f"subject:{subject}\nbody:{content}")
	server.quit()

Db=pymongo.MongoClient("mongodb://localhost:27017/")
Verditales = Db["verditales"]
Movies = Verditales["movies"]
Admin = Verditales["admin"]

def rndm():
	return str(datetime.datetime.now()).replace(" ","").replace(":","").replace(".","").replace(".","").replace("-","")

class Verditales:
	def movies(Request,_id):
		if Request.method == "GET":
			for i in Movies.find():
				if str(i["_id"]) == _id:
					return render(Request,"movies.html",{"data":i})
	def index(Request):
		return render(Request,"index.html", {"movies":[{"name":i["name"],"poster":i["poster"],"dimensions":[x for x in i["dimensions"]],"language":[x for x in i["language"]],"category":[x for x in i["category"]],"duration":i["duration"],"rate":i["age"],"releaseDate":i["releaseDate"],"id":i["_id"]} for i in Movies.find() if i["status"] == "running"]})
	def admin_login(Request):
		if Request.method == "GET":
			return render(Request,"admin-login.html")
		else:
			if Admin.find_one({"email":Request.POST.get("email"),"password":Request.POST.get("password")}) != None:
				h=[]
				for i in Movies.find():
					i.update({"id":str(i["_id"])})
					h.append(i)
				return render(Request,"admin-dashboard.html", {"email":Request.POST.get("email"),"password":Request.POST.get("password"),"movies":h})
			else:
				return render(Request,"admin-login.html", {"msg":"Invalid credentials"})
	def admin_dashboard(Request, email, password):
		if Request.method == "GET":
			if Admin.find_one({"email":email,"password":password}) != None:
				h=[]
				for i in Movies.find():
					i.update({"id":str(i["_id"])})
					h.append(i)
				return render(Request,"admin-dashboard.html", {"email":email,"password":password,"movies":h})
			else:
				return render(Request,"admin-login.html", {"msg":"Invalid credentials"})
		else:
			if Admin.find_one({"email":email,"password":password}) != None:
				h=[]
				for i in Movies.find():
					i.update({"id":str(i["_id"])})
					h.append(i)
				return render(Request,"admin-dashboard.html", {"email":email,"password":password,"movies":h})
			else:
				return render(Request,"admin-login.html", {"msg":"Invalid credentials"})
	def add_movie(Request, email, password):
		if Request.method == "GET":
			if Admin.find_one({"email":email,"password":password}) != None:
				return render(Request,"admin_add_movie.html", {"email":email,"password":password})
			else:
				return render(Request,"admin-login.html", {"msg":"Invalid credentials"})
		else:
			file = Request.FILES['file']
			fs=FileSystemStorage()
			lcn=fs.save(file.name,file)
			fname=rndm()+".png"
			Image.open(file.name).save(fname)
			os.remove(file.name)
			shutil.move(fname,"static/media/movies/"+fname)
			Movies.insert_one({"name": Request.POST.get("name"),"poster": "/static/media/movies/"+fname,"trailer": Request.POST.get("trailer"),"dimensions": Request.POST.get("dimensions").split(","),"category": Request.POST.get("category").split(","),"duration": int(Request.POST.get("duration")),"releaseDate": Request.POST.get("releaseDate"),"language": Request.POST.get("language").split(","),"age": Request.POST.get("age"),"status": "running"})
			return render(Request,"admin_add_movie.html", {"email":email,"password":password})
	def edit_movie(Request, email, password, iid):
		if Request.method == "GET":
			if Admin.find_one({"email":email,"password":password}) != None:
				for i in Movies.find():
					if str(i["_id"]) == iid:
						data={"email":email,"password":password}
						data.update(i)
						data.update({"iid":str(i["_id"])})
						return render(Request,"edit_movie.html", data)
				return redirect(f"/admin_dashboard/{email}/{password}/")
			return render(Request,"admin-login.html", {"msg":"Invalid credentials"})
		else:
			for i in Movies.find():
				if str(i["_id"]) == iid:
					poster=i["poster"]
					CurrentImage=i["poster"]
					try:
						file = Request.FILES['file']
						if len(file) > 0:
							fs=FileSystemStorage()
							lcn=fs.save(file.name,file)
							fname=rndm()+".png"
							Image.open(file.name).save(fname)
							os.remove(file.name)
							shutil.move(fname,"static/media/movies/"+fname)
							os.remove(CurrentImage[1:len(CurrentImage)-1])
							CurrentImage="static/media/movies/"+fname
					except:
						pass
					Movies.update_one({"poster":poster},{"$set":{"name": Request.POST.get("name"),"poster": CurrentImage,"trailer": Request.POST.get("trailer"),"dimensions": Request.POST.get("dimensions").split(","),"category": Request.POST.get("category").split(","),"duration": int(Request.POST.get("duration")),"releaseDate": Request.POST.get("releaseDate"),"language": Request.POST.get("language").split(","),"age": Request.POST.get("age"),"status": "running"}})
					return redirect(f"/edit_movie/{email}/{password}/{iid}/")
			return redirect(f"/edit_movie/{email}/{password}/{iid}/")
	def delete_movie(Request, email, password, iid):
		if Request.method == "GET":
			if Admin.find_one({"email":email,"password":password}) != None:
				for i in Movies.find():
					if str(i["_id"]) == iid:
						Movies.delete_one(i)
						break
				h=[]
				for i in Movies.find():
					i.update({"id":str(i["_id"])})
					h.append(i)
				return render(Request,"admin-dashboard.html", {"email":email,"password":password,"movies":h})
			else:
				return render(Request,"admin-login.html", {"msg":"Invalid credentials"})
	def archive_movie(Request, email, password, iid):
		if Request.method == "GET":
			if Admin.find_one({"email":email,"password":password}) != None:
				for i in Movies.find():
					if str(i["_id"]) == iid:
						Movies.update_one(i,{"$set":{"status":"archived"}})
						break
				h=[]
				for i in Movies.find():
					i.update({"id":str(i["_id"])})
					h.append(i)
				return render(Request,"admin-dashboard.html", {"email":email,"password":password,"movies":h})
			else:
				return render(Request,"admin-login.html", {"msg":"Invalid credentials"})
