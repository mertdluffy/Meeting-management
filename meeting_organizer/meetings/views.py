from django.shortcuts import render, get_object_or_404
from .models import Meeting
from django.http import JsonResponse

def meeting_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings/meeting_list.html', {'meetings': meetings})

def meeting_edit(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    # Düzenleme işlemleri burada yapılacak
    return render(request, 'meetings/meeting_edit.html', {'meeting': meeting})

def add_meeting(request):
    # Extract form data from the request
    subject = request.POST.get('subject')
    date = request.POST.get('date')
    start_time = request.POST.get('startTime')
    end_time = request.POST.get('endTime')
    participants = request.POST.get('participants')

    # Create a new meeting object
    meeting = Meeting.objects.create(
        subject=subject,
        date=date,
        start_time=start_time,
        end_time=end_time,
        participants=participants
    )

    # Return a JSON response indicating success
    return JsonResponse({'message': 'Meeting created successfully', 'meeting_id': meeting.id})
