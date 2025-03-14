from django import urls
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('service',views.service,name='service'),
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('contactreplay',views.contactreplay,name='contactreplay'),
    path('gallery',views.gallery,name='gallery'),
    path('register',views.register,name='register'),
    path('dashbord/<str:Email_id>',views.dashbord,name='dashbord'),
    path('addbookpage/<str:Email_id>',views.addbookpage,name='addbookpage'),
    path('adddiscount/<str:Email_id>',views.adddiscount,name='adddiscount'),
    path('addexpenses/<str:Email_id>',views.addexpenses,name='addexpenses'),
    path('addincome/<str:Email_id>',views.addincome,name='addincome'),
    path('addleavebutton/<str:Email_id>',views.addleavebutton,name='addleavebutton'),
    path('addvisitor/<str:Email_id>',views.addvisitor,name='addvisitor'),
    path('aditamissionadd/<str:Email_id>',views.aditamissionadd,name='aditamissionadd'),
    path('alex1page/<str:Email_id>',views.alex1page,name='alex1page'),
    path('alexdemo/<str:Email_id>',views.alexdemo,name='alexdemo'),
    path('classtimetable/<str:Email_id>',views.classtimetable,name='classtimetable'),
    path('classtimetableadd/<str:Email_id>',views.classtimetableadd,name='classtimetableadd'),
    path('classtimetableedit/<str:Email_id>',views.classtimetableedit,name='classtimetableedit'),
    path('downloattencecerif/<str:Email_id>',views.downloattencecerif,name='downloattencecerif'),
    path('downloattencecerifadd/<str:Email_id>',views.downloattencecerifadd,name='downloattencecerifadd'),
    path('downloattencecerifedit/<str:Email_id>',views.downloattencecerifedit,name='downloattencecerifedit'),
    path('downlobonafidecert/<str:Email_id>',views.downlobonafidecert,name='downlobonafidecert'),
    path('downlobonafidecertadd/<str:Email_id>',views.downlobonafidecertadd,name='downlobonafidecertadd'),
    path('downlobonafidecertedit/<str:Email_id>',views.downlobonafidecertedit,name='downlobonafidecertedit'),
    path('editbookpage/<str:Email_id>',views.editbookpage,name='editbookpage'),
    path('editexpense/<str:Email_id>',views.editexpense,name='editexpense'),
    path('editfeediscount/<str:Email_id>',views.editfeediscount,name='editfeediscount'),
    path('editincome/<str:Email_id>',views.editincome,name='editincome'),
    path('editleavebutton/<str:Email_id>',views.editleavebutton,name='editleavebutton'),
    path('editpage/<str:Email_id>',views.editpage,name='editpage'),
    path('editvisitor/<str:Email_id>/<int:id>',views.editvisitor,name='editvisitor'),
    path('examaddpage/<str:Email_id>',views.examaddpage,name='examaddpage'),
    path('Examgroup/<str:Email_id>',views.Examgroup,name='Examgroup'),
    path('examiconedit/<str:Email_id>',views.examiconedit,name='examiconedit'),
    path('examlistpage/<str:Email_id>',views.examlistpage,name='examlistpage'),
    path('Examresult/<str:Email_id>',views.Examresult,name='Examresult'),
    path('examresultadd/<str:Email_id>',views.examresultadd,name='examresultadd'),
    path('examresultedit/<str:Email_id>',views.examaresultedit,name='examresultedit'),
    path('examschedadd/<str:Email_id>',views.examschedadd,name='examschedadd'),
    path('examschededit/<str:Email_id>',views.examschededit,name='examschededit'),
    path('exlistaddbu/<str:Email_id>',views.exlistaddbu,name='exlistaddbu'),
    path('exlisticonadd/<str:Email_id>',views.exlisticonadd,name='exlisticonadd'),
    path('expensesdetails/<str:Email_id>',views.expensesdetails,name='expensesdetails'),
    path('exschedulelist/<str:Email_id>',views.exschedulelist,name='exschudlelist'),
    path('feesdetails/<str:Email_id>',views.feesdetails,name='feesdeatils'),
    path('feesdetailsadd/<str:Email_id>',views.feesdetailsadd,name='feesdetailsadd'),
    path('feesdetailsedit/<str:Email_id>',views.feesdetailsedit,name='feesdetailsedit'),
    path('feesdiscount/<str:Email_id>',views.feesdiscount,name='feesdiscount'),
    path('googlemeettimetable/<str:Email_id>',views.googlemeettimetable,name='googlemeettimetable'),
    path('googlemeettimetableadd/<str:Email_id>',views.googlemeettimetableadd,name='googlemeettimetableadd'),
    path('googlemeettimetableedit/<str:Email_id>',views.googlemeettimetableedit,name='googlemeettimetableedit'),
    path('incomedetails/<str:Email_id>',views.incomedetails,name='incomedetails'),
    path('librarybooklist/<str:Email_id>',views.librarybooklist,name='librarybooklist'),
    path('onsdmidedit/<str:Email_id>',views.onadmisedit,name='onadmisedit'),
    path('onlineadmission/<str:Email_id>',views.onlineadmission,name='onlineadmission'),
    path('onlineadmissionadd/<str:Email_id>',views.onlineadmissionadd,name='onlineadmissionadd'),
    path('onlineadmissionedit/<str:Email_id>',views.onlineadmissionedit,name='onlineadmissionedit'),
    path('onlineclassdet/<str:Email_id>',views.onlineclassdet,name='onlineclassdet'),
    path('onlineclassdetadd/<str:Email_id>',views.onlineclassdetadd,name='onlineclassdetadd'),
    path('onlineclassdetedit/<str:Email_id>',views.onlineclassdetedit,name='onlineclassdetedit'),
    path('onlineexamsch/<str:Email_id>',views.onlineexamsch,name='onlineexamsch'),
    path('onlineexamschadd/<str:Email_id>',views.onlineexamschadd,name='onlineexamschadd'),
    path('onlineexshledit/<str:Email_id>',views.onlineexshledit,name='onlineexshledit'),
    path('onlinesemexamfile/<str:Email_id>',views.onlinesemexamfile,name='onlinesemexamfile'),
    path('onlinesemfileadd/<str:Email_id>',views.onlinesemfileadd,name='onlinesemfileadd'),
    path('onlinesemexamedit/<str:Email_id>',views.onlinesemexamedit,name='onlinesemfileedit'),
    path('satffleaveadd/<str:Email_id>',views.satffleaveadd,name='satffleaveadd'),
    path('satffleaveedit/<str:Email_id>',views.satffleaveedit,name='satffleaveedit'),
    path('satffleaveform/<str:Email_id>',views.satffleaveform,name='satffleaveform'),
    path('satffattandenceadd/<str:Email_id>',views.satffattenceadd,name='satffattandenceadd'),
    path('satffattandenceedit/<str:Email_id>',views.satffattenceedit,name='satffattandenceedit'),
    path('satffattandencelist/<str:Email_id>',views.satffattencelist,name='satffattandencelist'),
    path('satffdirlist/<str:Email_id>',views.satffdirtlist,name='satffdirlist'),
    path('satffdirlistadd/<str:Email_id>',views.satffdirtlistadd,name='satffdirlistadd'),
    path('satffdirlistedit/<str:Email_id>',views.satffdirtlistedit,name='satffdirlistedit'),
    path('studentadmision/<str:Email_id>',views.studentadmision,name='studentadmision'),
    path('studentadmisionedit/<str:Email_id>',views.studentadmisionedit,name='studentadmisionedit'),
    path('studentadmissionadd/<str:Email_id>',views.studentadmissionadd,name='studentadmissionadd'),
    path('studentapprove/<str:Email_id>',views.studentapprove,name='studentapprove'),
    path('studentapproveadd/<str:Email_id>',views.studentapproveadd,name='studentapproveadd'),
    path('studentapproveedit/<str:Email_id>',views.studentapproveedit,name='studentapproveedit'),
    path('studentattendence/<str:Email_id>',views.studentattendence,name='studentattendence'),
    path('studentedit/<str:Email_id>',views.studentedit,name='studentedit'),
    path('studentfeedback/<str:Email_id>',views.studentfeedback,name='studentfeedback'),
    path('studentfeedbackadd/<str:Email_id>',views.studentfeedbackadd,name='studentfeedbackadd'),
    path('studentfeedbackedit/<str:Email_id>',views.studentfeedbackedit,name='studentfeedbackedit'),
    path('studentinfo/<str:Email_id>',views.studentinfo,name='studentinfo'),
    path('studentview/<str:Email_id>',views.studentview,name='studentview'),
    path('studentviewadd/<str:Email_id>',views.studentviewadd,name='studentviewadd'),
    path('studentviewedit/<str:Email_id>',views.studentviewedit,name='studentviewedit'),
    path('stufeescollect/<str:Email_id>',views.stufeescollect,name='stufeescollect'),
    path('stufeescollectadd/<str:Email_id>',views.stufeescollectadd,name='stufeescollectadd'),
    path('stufeescollectedit/<str:Email_id>',views.stufeescollectedit,name='stufeescollectedit'),
    path('subjectlist/<str:Email_id>',views.subjectlist,name='subjectlist'),
    path('subjectlistadd/<str:Email_id>',views.subjectlistadd,name='subjectlistadd'),
    path('subjectlistedit/<str:Email_id>',views.subjectlist,name='subjectlistedit'),
    path('tablesbootstrap/<str:Email_id>',views.tablesbootstrap,name='tablesbootstrap'),
    path('teacherfeedback/<str:Email_id>',views.teacherfeedback,name='teachersfeedback'),
    path('teacherfeedbackadd/<str:Email_id>',views.teacherfeedbackadd,name='teachersfeedbackadd'),
    path('teacherfeedbackedit/<str:Email_id>',views.teacherfeedbackedit,name='teachersfeedbackedit'),
    path('teachertimetable/<str:Email_id>',views.teachertimetable,name='teachertimetable'),
    path('teachertietableadd/<str:Email_id>',views.teachertietableadd,name='teachertietableadd'),
    path('teachertimetableedit/<str:Email_id>',views.teachertimetableedit,name='teachertimetableedit'),
    path('visitorbook/<str:Email_id>',views.visitorbook,name='visitorbook'),
    # register  form url
    path('register_form_submission',views.register_form_submission,name='register_form_submission'),
    #login form url
    path('login_form_submission',views.login_form_submission,name='login_form_submission'),
    # aditamissionadd url
    path('aditamissionadd_form_submission/<str:Email_id>',views.aditamissionadd_form_submission,name='aditamissionadd_form_submission'),
     #add studentadmission url
    path('addstudentadmission_form_submission/<str:Email_id>',views.addstudentadmission_form_submission,name='addstudentadmission_form_submission'),
   
    #add visitor url
    path('addvisitor_form_submission/<str:Email_id>',views.addvisitor_form_submission,name='addvisitor_form_submission'),
    #update or edit visitor url
    path('visitor_update_form_submission/<str:Email_id>/<int:id>',views.visitor_update_form_submission,name="visitor_update_form_submission"),
    #delate visitor url
    path('delete_visitor/<str:Email_id>/<int:id>',views.delete_visitor,name='delete_visitor'),
    #visitor_page:
    path('visitorbook/<str:email_id>',views.visitorbook,name='visitorbook'),
    path('addvisitor/<str:email_id>',views.addvisitor,name='addvisitor'),
    path('editvisitor/<str:email_id>/<int:id>',views.editvisitor,name='editvisitor'),
    path('addvisitor_form_submission/<str:email_id>',views.addvisitor_form_submission,name='addvisitor_form_submission'),
    path('visitor_update_form_submission/<str:email_id>/<int:id>',views.visitor_update_form_submission,name='visitor_update_form_submission'),
    path('delete_visitor/<str:email_id>/<int:id>',views.delete_visitor,name='delete_visitor'),

    
    








]



