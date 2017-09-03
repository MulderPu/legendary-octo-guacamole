'''
Write a Python program to accept 2 inputs:  Applicant’s name and Interviewer name and to display a
new interview date (1 month later from the current date) for an interview.   
'''
import datetime
from dateutil.relativedelta import relativedelta

applicant_name = input('Enter the applicant\'s name:')
interviewer_name = input('Enter the interviewer\'s name:')

current = datetime.datetime.today()
one_month_from_now = current + relativedelta(months=1)
time = one_month_from_now.strftime('%H:%M')
date = one_month_from_now.strftime('%Y-%m-%d')
print('%s will interview %s at %s on %s' %(applicant_name, interviewer_name, time,date))

