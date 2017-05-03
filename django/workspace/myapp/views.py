from django.shortcuts import render
from itertools import chain
 #Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from .forms import NameForm
from .forms import StudentInfoForm
from .forms import SearchStudent
from myapp.models import Admin
from myapp.models import Students
from myapp.models import StudentActivities
import datetime
from .forms import SearchID
from django.db.models import Count
from django.db.models import Sum


def hello(request):
    text = """<h1>welcome to my app !</h1> <br> <h2> Ediberto Cruz is the best </h2>"""
    return HttpResponse(text)
    
def test(request):
    t = get_template('test.html')
    html = t.render()
    getID = StudentActivities.objects.filter(student_id="12")
    print "TEST"
    print getID
    #return render(request,'moreInfo.html',{'ids':getID})
    return HttpResponse(html)
    
def base(request):
    t = get_template('base.html')
    html = t.render()
    return HttpResponse(html)

def login(request):
    t = get_template('login.html')
    html = t.render()
    return HttpResponse(html)
    
def charts(request):
    t = get_template('charts.html')
    html = t.render()
    return HttpResponse(html)
    
    
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #print "Test " + form.cleaned_data['your_name']
            try:
                foo = Admin.objects.get(admin_id=2017)
                print "Success"
            except Admin.DoesNotExist:
                print 'Nope'
            try:
                #names = Admin.objects.filter(username=form.cleaned_data['your_name'])
                names = Admin.objects.get(username=form.cleaned_data['your_name'])
                print names.username
                return HttpResponseRedirect('/myapp/main')
            except Admin.DoesNotExist:
                print "admin does not exist"
            #x = Admin(name=form.cleaned_data['your_name')
            #if form.cleaned_data['your_name'] == 'Jose':
            #   return HttpResponseRedirect('/myapp/main')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        #print "Test " + form.your_name
    return render(request, 'login.html', {'form': form})
    
def SearchStudents(request):
    if request.method == 'POST':
        form = SearchStudent(request.POST)
        print request.POST
        if 'search' in request.POST:
            #print "AHHHHHHHHHHHHHHHHHHHHHH"
            if form.is_valid():
                
                name = form.cleaned_data['student_name']
                try:
                    first_names = Students.objects.filter(name = name)
                    #print "Success, for first names"
                    #print(first_names[1].student_id)
                except Students.DoesNotExist:
                    print 'Nope'
                    
                try:
                    last_names = Students.objects.filter(lastname = name)
                    #print "Success for last names"
                except Students.DoesNotExist:
                    print 'Nope'
                    last_names = []
                result_list = list(chain(last_names, first_names))
                #all_students = first_names
                for student in result_list:
                    print(student.student_id)
                    
                
                return render(request, 'main.html',{'students':result_list, 'form':form})
                
        elif 'submit' in request.POST:
            #print "other button is working"
            if form.is_valid():
                var = request.POST.getlist('Attendance')
                print var
            return render(request, 'main.html',{'form':form})
            
        else:
            print "NOT WORKING"
            return render(request, 'main.html',{'form':form})
    else:
        form = SearchStudent()
        print ('something 1')    
        date = datetime.datetime.now().time()
        return render(request, 'main.html',{'form':form, 'date':date})
    
def add_student(request):
    if request.method == 'POST':
        form = StudentInfoForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data['student_firstName']
            lastName = form.cleaned_data['student_lastName']
            grade = form.cleaned_data['student_grade']
            dob = form.cleaned_data['student_dob']
            school = form.cleaned_data['student_school']
            sex = form.cleaned_data['student_sex']
            note = form.cleaned_data['student_note']
            level = form.cleaned_data['student_level']
            ethnicity = form.cleaned_data['student_ethnicities']
            phone = form.cleaned_data['student_phone']
            id = form.cleaned_data['student_id']
            grade = int(grade)
            student_obj = Students(student_id = id, name = firstName, lastname = lastName, grade = grade, phone_num = phone, dob = dob, gerder = sex, school = school, golf_level = level, note = note, ethnicity = ethnicity, active = "Active")
            student_obj.save()
            
            print(firstName, level, note)
            
            return HttpResponseRedirect('addStudent')
        
    else:
        print ('something')
        form = StudentInfoForm()
    return render(request, 'addStudent.html',{'form':form})
##############################################################################    
#def moreIn(request):
   
    #getID = StudentActivities.objects.filter(student_id="12")
    #print "TEST"
    #print getID
    #return render(request,'moreInfo.html',{'ids':getID})
        
     

def moreIn(request):
    #form = SearchStudent()
    #form1 = Students.objects.values('school').annotate(count=Count('school')).order_by('school')
    form2 = Students.objects.all().annotate(count1=Count('gerder'))
    
    form1 = Students.objects.values('school').annotate(count1=Count('gerder')).filter(gerder__startswith='F')
    return render(request,'moreInfo.html',{'form1':form1})
