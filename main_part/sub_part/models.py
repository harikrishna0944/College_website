from django.db import models

# Create your models here.
class register_table(models.Model):

  user_name=models.CharField(max_length=100)   
  Email_id=models.EmailField() 
  password=models.CharField(max_length=20)
  
  
  def __str__(self):
     return self.user_name


class addadtimisionenquire_table(models.Model):

  name=models.CharField(max_length=100)   
  enquirydate=models.CharField(max_length=100)   
  email=models.CharField(max_length=100)   
  DOB=models.CharField(max_length=100)
  Departments=models.CharField(max_length=100)   
  phonenumber=models.CharField(max_length=100)   
  status=models.CharField(max_length=100)
  
def __str__(self):
    return self.name

class add_visiter_table(models.Model):
  date=models.CharField(max_length=100)   
  visitorname=models.CharField(max_length=100)  
  visitedfor=models.CharField(max_length=100)  
  timein=models.CharField(max_length=100)  
  timeout=models.CharField(max_length=100) 
  def __str__(self):
      return self.visitorname  

class add_studentadmission_table(models.Model):
  reference=models.CharField(max_length=100)   
  studentname=models.CharField(max_length=100)  
  department=models.CharField(max_length=100)  
  fathername=models.CharField(max_length=100)  
  dob=models.CharField(max_length=100)
  Gender=models.CharField(max_length=100) 
  mobilenumber=models.CharField(max_length=100)  
  def __str__(self):
      return self.studentname  


    
  

  
    

