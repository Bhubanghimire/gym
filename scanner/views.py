from __future__ import division
from django.http.response import HttpResponse
from django.shortcuts import render
import pyzbar.pyzbar as pyzbar
import cv2
from django.contrib import messages
from gym.models import Member, AttendanceReport,Attendance
import datetime
from django.shortcuts import redirect
from datetime import date
# Create your views here.


def scanner_view(request):
    i=0
    cap = cv2.VideoCapture(0)
    
    while i<1:
        _, frame = cap.read()

        decoded = pyzbar.decode(frame)
        print(decoded)
        for obj in decoded:
            num = obj.data.decode('utf-8')
            i += 1
            cv2.destroyAllWindows()
            cap.release()
            

        cv2.startWindowThread()
        cv2.imshow("bhuban", frame) 
    
        k = cv2.waitKey(30) & 0xff
        if k==27:
            i=0
            return redirect("home")
           

        
    i=0
    user = Member.objects.filter(contact=num)
    if( not user):
         messages.error(request, 'You had not permission')
         return redirect("scanner_view")

    user = Member.objects.get(contact=num)
    n = user.name
    year = user.get_year()
    month = user.get_month()
    day = user.get_day()

    today = date.today()

    status =  Attendance.objects.filter(member_id=user, date=today)

    if status:
        messages.warning(request, 'You had already attened')
        
    else:
        attendance = Attendance.objects.create(member_id=user,status=True)
        attendance.save()
        AttendanceReport.objects.create(year=year, month=month, day=day, name=n, status=attendance)
        messages.success(request, 'QR Successfully Scanned')
    
    # return HttpResponse("done")
    return redirect('scanner_view') #render(request, 'scanner/scanner.html', context)


    