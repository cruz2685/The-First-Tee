from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Username', max_length=100)
    your_pw = forms.CharField(label='Password', max_length=100,widget=forms.PasswordInput)

class StudentInfoForm(forms.Form):
    student_id = forms.CharField(label='ID', max_length=20)
    student_firstName = forms.CharField(label='First Name', max_length=100)
    student_lastName = forms.CharField(label='Last Name', max_length=100)
    student_phone = forms.CharField(label='Phone Number', max_length=100)
    student_grade = forms.ChoiceField(choices=[(x, x) for x in ("1","2","3","4","5","6","7","8", "9", "10", "11", "12")])
    student_dob = forms.CharField(label='DOB', max_length=100)
    student_sex = forms.ChoiceField(choices=[(x, x) for x in ("Male","Female")])
    student_school = forms.CharField(label='School', max_length=100)
    student_note = forms.CharField(label='Note', max_length=100, required=False)
    
    student_level = forms.ChoiceField(choices=[(x, x) for x in ("Target","Player","A Player","A1 Player","Par","Birdie","Eagle","Ace")])
    student_ethnicities = forms.ChoiceField(choices=[(x, x) for x in ("Black or African-American","Latino/Hispanic","Multi-Racial","White or Caucasian","Native American or Native Alaskan","Asian","Pasific Islander")])

class SearchStudent(forms.Form):
    student_name = forms.CharField(label='Enter the First or Last name of the Student', max_length=100, required = False)  
    #data = Students.objects.all()
    #return TemplateResponse(request, 'Students/main.html',{"data":data})

class SearchSchool(forms.Form):
    student_school = forms.CharField(label='School', max_length=100)

class SearchID(forms.Form):
    ID = forms.IntegerField()
