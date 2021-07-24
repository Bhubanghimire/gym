from django.test import TestCase
from .models import *
from django.test import TestCase
from django.contrib.auth import get_user_model
import pytest


# Create your tests here.
class GymTestCase(TestCase):
    def test_Enquiry(self):
        new_enq = Enquiry.objects.create(name="bhuban",contact="99999999",emailid="test@gmail.com",age="23",gender='male')
        User = get_user_model()
        user = User.objects.create_user(username="bhuban",is_staff=True,password="pass")
        self.client.login(username='bhuban', password='pass')

        
        data={"name":"bhuban","contact":"987654323","emailid":"test@gmail.com","age":"23","gender":'male'}

        resp = self.client.post('/add_enquiry/',data)
        print(resp)

        self.assertEqual(resp.status_code, 200)


    def test_Equipment(self):
        new_enq = Equipment.objects.create(name="bhuban",price=333,unit=22,date=datetime,description="ssjkjk")
        User = get_user_model()
        user = User.objects.create_user(username="bhuban",is_staff=True,password="pass")
        self.client.login(username='bhuban', password='pass')

        
        data={"name":"bhuban","price":"333","unit":"22","date":"2222-2-2","desc":"ssjkjk"}
        resp = self.client.post('/add_equipment/',data)
        print(resp)

        self.assertEqual(resp.status_code, 200)


    def test_plan(self):
        new_enq = Plan.objects.create(name="bhuban",amount=333,duration="2 month")
        User = get_user_model()
        user = User.objects.create_user(username="bhuban",is_staff=True,password="pass")
        self.client.login(username='bhuban', password='pass')

        
        data={"name":"bhuban","amount":"333","duration":"2 month"}
        resp = self.client.post('/add_plan/',data)
        print(resp)

        self.assertEqual(resp.status_code, 200)

    def test_attendance(self):
        
        user = Member.objects.create(name="bhuban",emailid="abc@gmail.com",joindate="2222-2-2")

        new_enq = Attendance.objects.create(member_id=user,date="3333-3-3",status="True")
        

  