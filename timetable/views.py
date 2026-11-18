from django.shortcuts import render
from datetime import time

def timetable_view(request):

    slots = [
        {
            'day': 'Monday',
            'start_time': time(9, 0),
            'end_time': time(10, 0),
            'subject_name': 'Mathematics',
            'faculty_name': 'Mr. Kumar',
            'classroom': 'Room 101'
        },
        {
            'day': 'Monday',
            'start_time': time(10, 0),
            'end_time': time(11, 0),
            'subject_name': 'Python Programming',
            'faculty_name': 'Ms. Priya',
            'classroom': 'Lab 1'
        },
        {
            'day': 'Tuesday',
            'start_time': time(9, 0),
            'end_time': time(10, 0),
            'subject_name': 'Database Management',
            'faculty_name': 'Mr. Ravi',
            'classroom': 'Room 102'
        },
        {
            'day': 'Wednesday',
            'start_time': time(9, 0),
            'end_time': time(10, 0),
            'subject_name': 'Web Development',
            'faculty_name': 'Ms. Anu',
            'classroom': 'Lab 2'
        },
        {
            'day': 'Thursday',
            'start_time': time(10, 0),
            'end_time': time(11, 0),
            'subject_name': 'Computer Networks',
            'faculty_name': 'Mr. Arun',
            'classroom': 'Room 103'
        },
        {
            'day': 'Friday',
            'start_time': time(9, 0),
            'end_time': time(10, 0),
            'subject_name': 'Operating Systems',
            'faculty_name': 'Ms. Divya',
            'classroom': 'Room 104'
        },
    ]

    return render(
        request,
        'timetable/timetable.html',
        {'slots': slots}
    )