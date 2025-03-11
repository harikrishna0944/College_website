from ensurepip import bootstrap
from math import e
import re
from tabnanny import check
from django.shortcuts import render,redirect
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import auth
from socket import timeout
from urllib import request
from django.shortcuts import render
from . models import register_table,addadtimisionenquire_table,add_visiter_table,add_studentadmission_table
from django.contrib import messages
# Create your views here.
                              #index page
def index(request):
    return render(request,'index.html')
                            #login page
def login(request):
    
    return render(request,'login.html')

def login_form_submission(request):
    if register_table.objects.filter(Email_id=request.POST['Email_id'],password=request.POST['password']):
        print("****sucessfully loggin****")
        user_data=register_table.objects.get(Email_id=request.POST['Email_id'])
        
        return render(request,'dashbord.html',{'user_data':user_data})
    else:
        print("***failed to login***")
        messages.error(request,'invaild username or password',extra_tags='failed_login')
        return render(request,'login.html')
                       
                        #register page

def register(request):
    return render(request,'register.html')

def register_form_submission(request):
    if register_table.objects.filter(Email_id=request.POST['Email_id']):
        messages.error(request,'already registered using this Emailid',extra_tags='already')
        return render(request,'register.html')
    else:
        ex1=register_table(user_name=request.POST.get('user_name'),
                           Email_id=request.POST.get('Email_id'),
                           password=request.POST.get('password'),)
                          
            
        ex1.save()
        print("sucessfully register")
        messages.error(request,"sucessfully registered",extra_tags="registered")
        return render(request,'login.html')  
#about page
def about(request):
    return render(request,'about.html')
#dashbord page   
def dashbord(request):
    return render(request,'dashbord.html')
#coureses pagr
def service(request):
    return render(request,'service.html')
# contact page 
def contact(request):
    return render(request,'contact.html')
# contact page 
def contactreplay(request):
    return render(request,'contactreplay.html')

#college gallery
def gallery(request):
    return render(request,'gallery.html')
                                  #FRONT OFFICE

#Admission Enquiry
def tablesbootstrap(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    view_admission=addadtimisionenquire_table.objects.all()
    return render(request,'tablesbootstrap.html',{'user_data':user_data,'view_admission':view_admission})
#add admission
def aditamissionadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'aditamissionadd.html',{'user_data':user_data})
def aditamissionadd_form_submission(request,Email_id):
    if request.method=='POST':
        ex1=addadtimisionenquire_table(name=request.POST.get('name'),
                                   enquirydate=request.POST.get('enquirydate'),
                                   email=request.POST.get('email'),
                                   DOB=request.POST.get('DOB'),
                                   Departments=request.POST.get('Departments'),
                                   phonenumber=request.POST.get('phonenumber'),
                                   status=request.POST.get('status'))
        ex1.save()
        messages.error(request,'sucessfully added adtimission enquiry',extra_tags='success')
        view_admission=addadtimisionenquire_table.objects.all()
        user_data=register_table.objects.get(Email_id=Email_id)
        return render(request,'tablesbootstrap.html',{'user_data':user_data,'view_admission':view_admission})
    else:                                
        return render(request,'aditamissionadd.html')


  
  
  
    
 #edit admission
def editpage(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'editpage.html',{'user_data':user_data})
   


#Visitor Book
def visitorbook(request,Email_id):
    view_visitor=add_visiter_table.objects.all()
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'visitorbook.html',{'user_data':user_data,'view_visitor':view_visitor})

#add visitor
def addvisitor(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'addvisitor.html',{'user_data':user_data})

def addvisitor_form_submission(request,Email_id):
    if request.method=='POST':
        ex1=add_visiter_table(date=request.POST.get('date'),
                          visitorname=request.POST.get('visitorname'),
                          visitedfor=request.POST.get('visitedfor'),
                          timein=request.POST.get('timein'),
                          timeout=request.POST.get('timeout'))
        ex1.save()
        messages.error(request,'sucessfully added visitors',extra_tags='visitor')
        view_visitor=add_visiter_table.objects.all()
        user_data=register_table.objects.get(Email_id=Email_id)
        return render(request,'visitorbook.html',{'user_data':user_data,'view_visitor':view_visitor})
    else:                                
        return render(request,'addvisitor.html')

    



#edit visitor
def editvisitor(request,Email_id):
    visitor_data=add_visiter_table.objects.get(id=id)
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'editvisitor.html',{'user_data':user_data,'visitor_data':visitor_data})

def visitor_update_form_submission(request,id,Email_id):
    if request.method=='POST':
        ex1=add_visiter_table.objects.filter(id=id).update(datevisited=request.POST['date'],
                                                            visitorname=request.POST['visitorname'],
                                                            visitedfor=request.POST['visitedfor'],
                                                            timein=request.POST['timein'],
                                                            timeout=request.POST['timeout'])

                                                            
        messages.error(request,'Successfully Updated!...',extra_tags='success')
        view_visitor=add_visiter_table.objects.all()
        user_data=register_table.objects.get(Email_id=Email_id)
        return render(request,'visitorbook.html',{'user_data':user_data,'view_visitor':view_visitor})
    else:
        visitor_data=add_visiter_table.objects.get(id=id)
        user_data=register_table.objects.get(Email_id=Email_id)
        return render(request,'editvisitor.html',{'user_data':user_data,'visitor_data':visitor_data})
#delate visitor
def delete_visitor(request,Email_id,id):
    user_data=register_table.objects.get(Email_id=Email_id)
    visitor_data=add_visiter_table.objects.get(id=id)
    visitor_data.delete()
    messages.error(request,'successfully deleted!...',extra_tags='success')
    view_visitor=add_visiter_table.objects.all()
    return render(request,'visitorbook.html',{'user_data':user_data,'view_visitor':view_visitor})




                          #Student Information

#Student Details
def studentview(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentview.html',{'user_data':user_data})
#add student view
def studentviewadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentviewadd.html',{'user_data':user_data})
#edit student view
def studentviewedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentviewedit.html',{'user_data':user_data})


#Student Admission
def studentadmision(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentadmision.html',{'user_data':user_data})
#add sudent admission
def studentadmissionadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentadmissionadd.html',{'user_data':user_data})

def addstudentadmission_form_submission(request,Email_id):
    if request.method=='POST':
        ex1=add_studentadmission_table(reference=request.POST.get('reference'),
                                   studentname=request.POST.get('studentname'),
                                   department=request.POST.get('department'),
                                   fathername=request.POST.get('fathername'),
                                   dob=request.POST.get('dob'),
                                   Gender=request.POST.get('Gender'),
                                   mobilenumber=request.POST.get('mobilenumber'))
        ex1.save()
        messages.error(request,'sucessfully added student admission',extra_tags='admission')
        view_data=add_visiter_table.objects.all()
        user_data=register_table.objects.get(Email_id=Email_id)
        return render(request,'studentadmision.html',{'user_data':user_data,'view_data':view_data})

#edit student admission
def studentadmisionedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentadmisionedit.html',{'user_data':user_data})

#Online Admission
def onlineadmission(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'onlineadmission.html',{'user_data':user_data})
#add online admission
def onlineadmissionadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'onlineadmissionadd.html',{'user_data':user_data})
#edit online admission
def onlineadmissionedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'onlineadmissionedit.html',{'user_data':user_data})

                         #Fees Collection
# Collection fees 
def feesdetails(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'feesdetails.html',{'user_data':user_data})
#add feedeatils
def feesdetailsadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'feesdetailsadd.html',{'user_data':user_data})
#edit feesdeatils
def feesdetailsedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'feesdetailsedit.html',{'user_data':user_data})


#Search Fees Payment
def stufeescollect(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'stufeescollect.html',{'user_data':user_data})
#add search fees
def stufeescollectadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'stufeescollectadd.html',{'user_data':user_data})
#edit search fees
def stufeescollectedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'stufeescollectedit.html',{'user_data':user_data})

 #Fees Discount  
def feesdiscount(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'feesdiscount.html',{'user_data':user_data})
#add feesdiscount
def adddiscount(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'adddiscount.html',{'user_data':user_data})
#edit feesdiscount
def editfeediscount(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'editfeediscount.html',{'user_data':user_data})

                                 #Income  
#Income details

def incomedetails(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'incomedetails.html',{'user_data':user_data})
#income add
def addincome(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'addincome.html',{'user_data':user_data})
#edit income
def editincome(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'editincome.html',{'user_data':user_data})


                                   #Expenses
 #Expenses Details
def expensesdetails(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'expensesdetails.html',{'user_data':user_data})
#add expenses
def addexpenses(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'addexpenses.html',{'user_data':user_data})
#edit expenses
def editexpense(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'editexpense.html',{'user_data':user_data})


                                   #Attendance                                
#Student Attendence
def studentattendence(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentattendence.html',{'user_data':user_data})
#add student attendence
def addleavebutton(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'addleavebutton.html',{'user_data':user_data})
#edit attendence
def editleavebutton(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'editleavebutton.html',{'user_data':user_data})



# Student Absents
def studentapprove(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentapprove.html',{'user_data':user_data})
#add student absent
def studentapproveadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentapproveadd.html',{'user_data':user_data})
#edit 
def studentapproveedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentapproveedit.html',{'user_data':user_data})

                                    #Examinations
 #   Exam Group list 
def Examgroup(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'Examgroup.html',{'user_data':user_data})
#add exam group list
def examaddpage(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'examaddpage.html',{'user_data':user_data})
#edit exam group
def examiconedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'examiconedit.html',{'user_data':user_data})

#  Exam list
def examlistpage(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'examlistpage.html',{'user_data':user_data})
#add exam list
def exlistaddbu(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'exlistaddbu.html',{'user_data':user_data})
#edit exam list
def exlisticonadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'exlisticonadd.html',{'user_data':user_data})

#  Exam Schedule
def exschedulelist(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'exschedulelist.html',{'user_data':user_data})
#add exam schedule
def examschedadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'examschedadd.html',{'user_data':user_data})
#edit exam schedule
def examschededit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'examschededit.html',{'user_data':user_data})

#Semester Exam Result                 
def Examresult(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'Examresult.html',{'user_data':user_data})
#add exam results
def examresultadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'examresultadd.html',{'user_data':user_data})
#edit exam results
def examaresultedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'examresultedit.html',{'user_data':user_data})


                               #Online Examinations
#Online Exam Schedule
def onlineexamsch(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'onlineexamsch.html',{'user_data':user_data})
#add online exam schedule
def onlineexamschadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'onlineexamschadd.html',{'user_data':user_data})
#edit online exam schedule
def onlineexshledit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'onlineexshledit.html',{'user_data':user_data})

#Online Semester Exam
def onlinesemexamfile(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'onlinesemexamfile.html',{'user_data':user_data})
#add online semester exam
def onlinesemfileadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'onlinesemfileadd.html',{'user_data':user_data})
#edit online sem exam
def onlinesemexamedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'onlinesemexamedit.html',{'user_data':user_data})

                                 #Academics
#Class Timetable
def classtimetable(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'classtimetable.html',{'user_data':user_data})
#add class time table 
def classtimetableadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'classtimetableadd.html',{'user_data':user_data})
#edit class time table
def classtimetableedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'classtimetableedit.html',{'user_data':user_data})


#Teachers Timetable
def teachertimetable(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'teachertimetable.html',{'user_data':user_data})
#add teacher timetable
def teachertietableadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'teachertietableadd.html',{'user_data':user_data})
#edit teacher timetable
def teachertimetableedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'teachertimetableedit.html',{'user_data':user_data})


#Subject
def subjectlist(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'subjectlist.html',{'user_data':user_data})
#add subject
def subjectlistadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'subjectlistadd.html',{'user_data':user_data})
#edit subject
def subjectlistedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'subjectlistedit.html',{'user_data':user_data})

                                        #staff                              
#Staff Directory
def satffdirtlist(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'satffdirtlist.html',{'user_data':user_data})
#add staff dir
def satffdirtlistadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'satffdirtlistadd.html',{'user_data':user_data})
#edit staff dir
def satffdirtlistedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'satffdirtlistedit.html',{'user_data':user_data})


#Staff Attendance
def satffattencelist(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'satffattencelist.html',{'user_data':user_data})
#add staff attendance
def satffattenceadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'satffattenceadd.html',{'user_data':user_data})
#edit staff attendance
def satffattenceedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'satffattenceedit.html',{'user_data':user_data})

#Staff Leave Form
def satffleaveform(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'satffleaveform.html',{'user_data':user_data})
#add staff leave form
def satffleaveadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'satffleaveadd.html',{'user_data':user_data})
#edit staff leave form
def satffleaveedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'satffleaveedit.html',{'user_data':user_data})

                                             #Library
#Library Book
def librarybooklist(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'librarybooklist.html',{'user_data':user_data})
#add books
def addbookpage(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'addbookpage.html',{'user_data':user_data})
#edit book 
def editbookpage(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'editbookpage.html',{'user_data':user_data})


                                             #Feedback
#students
def studentfeedback(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentfeedback.html',{'user_data':user_data})
#add student feedback
def studentfeedbackadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentfeedbackadd.html',{'user_data':user_data})
#edit student feed back
def studentfeedbackedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentfeedbackedit.html',{'user_data':user_data})


#Teacher
def teacherfeedback(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'teacherfeedback.html',{'user_data':user_data})
#add teacher feedback
def teacherfeedbackadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'teacherfeedbackadd.html',{'user_data':user_data})
#edit teacher feedback
def teacherfeedbackedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'teacherfeedbackedit.html',{'user_data':user_data})





def alex1page(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'alex1page.html',{'user_data':user_data})
def alexdemo(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'alexdemo.html',{'user_data':user_data})
def downloattencecerif(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'downloattencecerif.html',{'user_data':user_data})
def downloattencecerifadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'downloattencecerifadd.html',{'user_data':user_data})
def downloattencecerifedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'downloattencecerifedit.html',{'user_data':user_data})
def downlobonafidecert(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'downlobonafidecert.html',{'user_data':user_data})
def downlobonafidecertadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'downlobonafidecertadd.html',{'user_data':user_data})
def downlobonafidecertedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'downlobonafidecertedit.html',{'user_data':user_data})
def googlemeettimetable(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'googlemeettimetable.html',{'user_data':user_data})
def googlemeettimetableadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'googlemeettimetableadd.html',{'user_data':user_data})
def googlemeettimetableedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'googlemeettimetableedit.html',{'user_data':user_data})

def onadmisedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'onadmisedit.html',{'user_data':user_data})

def onlineclassdet(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'onlineclassdet.html',{'user_data':user_data})
def onlineclassdetadd(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'onlineclassdetadd.html',{'user_data':user_data})
def onlineclassdetedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'onlineclassdetedit.html',{'user_data':user_data})
def studentedit(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentedit.html',{'user_data':user_data})
def studentinfo(request,Email_id):
    user_data=register_table.objects.get(Email_id=Email_id)
    return render(request,'studentinfo.html',{'user_data':user_data})

































































