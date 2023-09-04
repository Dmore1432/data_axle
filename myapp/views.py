from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from django.views import View
import json

# Create your views here.

def function1(request):
    l="Dnyaneshwar"
    return HttpResponse(l)
def index(request):
    return render(request,'myapp/index.html')

def Insertform(request):
    return render(request,'myapp/insertform.html')

def Insertdata(request):
    #data come from HTML to views
    f_name=request.POST['fname']
    l_name=request.POST['lname']
    e_mail=request.POST['email']
    c_ontact=request.POST['contact']

    #createing object of model class
    #inserting data  into table

    newuser= Student.objects.create(Firstname=f_name,Lastname=l_name,Email=e_mail,Contact=c_ontact)
    newuser.save()
    #after insert data rendar on show.html
    #return render(request,'myapp/show.html')
    return redirect('showpage')

#Read
def Showpage(request):
    #select * from tablename
    #for fetching all the data of the table
    # all_data=Student.objects.all()
    # all_data=Student.objects.filter(Firstname='rohan')
    # all_data = Student.objects.exclude(Firstname='rohan')
    # all_data = Student.objects.order_by('Lastname')
    # all_data = Student.objects.order_by('id').reverse()
    # all_data = Student.objects.order_by("-Firstname").values()
    all_data= Student.objects.all().order_by('Lastname', '-id').values()

    return render(request,'myapp/show.html',{'key1':all_data})

def Editpage(request,pk):
    get_data=Student.objects.get(id=pk)
    return render(request,'myapp/edit.html',{'key2':get_data})

#update
def Updatedata(request,pk):
    udata=Student.objects.get(id=pk)
    udata.Firstname=request.POST['fname']
    udata.Lastname=request.POST['lname']
    udata.Email=request.POST['email']
    udata.Contact=request.POST['contact']
    udata.save()
    return redirect('showpage')

#delete data

def Deletedata(request,pk):
    ddata=Student.objects.get(id=pk)
    ddata.delete()
    return redirect('showpage')



#python object convert to json and show your browser
def json1(request):
    emp={
        'eno':100,
        'ename':'D',
        'esal':10000,
        'eadd':'pune'
    }
    emp1=json.dumps(emp)
    return HttpResponse(emp1,content_type='application/json')

# def just(request):
#     c={'msg':'hey hello'}
#     return render(request,'myapp/just.html',c)

class Just(View):
    def get(self,request):
        c = {'msg': 'hey hello python'}

        return render(request,'myapp/just.html',c)


#class base views

class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This is the get method'})
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This is the post method'})
        return HttpResponse(json_data,content_type='application/json')

    def put(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This is the put method'})
        return HttpResponse(json_data,content_type='application/json')

    def patch(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This is the patch method'})
        return HttpResponse(json_data,content_type='application/json')


#
# class parent(View):
#     name="D "
#     def get(self,request):
#         name='rohan'
#         return HttpResponse(name)
#
# class child(parent):
#     def get(self,request):
#         name='soham'
#         return HttpResponse(self.name)
#
#
#
#
#
#
#
#







#view for register page
# def Registerpage(request):
#     return render(request,'myapp/register.html')
#
#
#
#
#
# # view for user registration
#
# def Userregister(request):
#     if request.method=='POST':
#         f_name=request.POST['fname']
#         l_name=request.Post['lname']
#         e_mail=request.POST['email']
#         c_ontact=request.Post['contact']
#         p_word=request.POST['password']
#         c_pass=request.POST['cpassword']
#         user=User.objects.filter(Email=e_mail)
#         if user:
#             msg='This user alredy exist'
#             return render(request,'myapp/register.html',{'msg':msg})
#         else:
#             if p_word==c_pass:
#                 newuser=User.objects.create(Firstname=f_name,Lastname=l_name,Email=e_mail,Contact=c_ontact,
#                                             Password=p_word)
#                 msg='user register Successfuly'
#                 return render(request,'myapp/login.html',{'msg':msg}
