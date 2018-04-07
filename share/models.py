from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

# def get_profilepic_path(instance,filename):
# 	return 'users/{0}/profilepic/{1}'.format(instance.user.first_name+"_"+instance.regNum,filename)

class Userprofile(models.Model) : 
	branch_choices = (
		('CSE','Computer Science & Engineering'),
		('ECE','Electronics and Communication Engineering'),
		('MECH','Mechanical Engineering'),
		('MME','Metallurgy Engineering'),
		('CHE','Chemical Engineering'),
		('CIVIL','Civil Engineering'),
		('EEE','Electrical and Electronics Engineering'),
		('BIO','Biotechnology'),
	)

	course_choices = (
		('BTech','B.Tech'),
		('MTech','M.Tech'),
		('MCA','MCA'),
		('MBA','MBA'),
		('PHD','Phd'),
	)

	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='profile')
	regNum = models.CharField(max_length=10)
	course = models.CharField(max_length=10,choices = course_choices,default='BTech')
	branch = models.CharField(max_length=10,choices = branch_choices)
	contact = models.CharField(max_length=20)
	# profile_pic = models.ImageField(upload_to=get_profilepic_path,null=True,blank=True)
	year = models.CharField(max_length = 10)

	def __str__(self):
		return (self.user.first_name + "_" + self.regNum)

class Item(models.Model):
	status_choices = (
		(1,'Available'),
		(2,'Requested'),
		(3,'Borrowed'),
	)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Item_owner')
	itemType = models.CharField(max_length=20)
	status = models.IntegerField(choices=status_choices,default=1)
	title = models.CharField(max_length=255)
	desc = models.CharField(max_length= 1000)

	def __str__(self) :
		return self.title

class BorrowRequest(models.Model):
	status_choices = (
		(1,'Requested'),
		(2,'Accepted'),
		(3,'Rejected'),
		(4,'Completed'),
	)

	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='I_owner')
	borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Item_borrower')
	status = models.IntegerField(choices=status_choices,default=1)
	description = models.CharField(max_length=512, null = True)
	requestDate = models.DateField(default=datetime.date.today)
	approvalDate = models.DateField(auto_now=False, auto_now_add=False)



