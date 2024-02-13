from django.shortcuts import render, get_object_or_404
from .models import Meeting
from django.http import JsonResponse
import json

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
def get_meeting_details(request, meeting_id):
   try:
       meeting = Meeting.objects.get(pk=meeting_id)
       meeting_details = {
           'subject': meeting.subject,
           'date': meeting.date,
           'startTime': meeting.start_time,
           'endTime': meeting.end_time,
           'participants': meeting.participants
       }
       return JsonResponse(meeting_details)
   except Meeting.DoesNotExist:
       return JsonResponse({'error': 'Meeting not found'}, status=404)
def delete_meeting(request):
    if request.method == 'POST':
        # Assuming JSON data is sent
        try:
            # Parse the JSON data
            data = json.loads(request.body)
            meeting_id = data.get('meeting_id')
            print("Meeting ID:", meeting_id)
            if meeting_id is not None:
                try:
                    meeting = Meeting.objects.get(pk=meeting_id)
                    meeting.delete()
                    return JsonResponse({'message': 'Meeting deleted successfully'})
                except Meeting.DoesNotExist:
                    return JsonResponse({'error': 'Meeting not found'}, status=404)
            else:
                return JsonResponse({'error': 'Meeting ID not provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
def update_meeting(request):
    if request.method == 'POST':
        # Retrieve updated meeting details from request body
        data = json.loads(request.body)
        meeting_id = data.get('meeting_id')
        updated_subject = data.get('subject')
        updated_date = data.get('date')
        updated_start_time = data.get('startTime')
        updated_end_time = data.get('endTime')
        updated_participants = data.get('participants')
        # Update meeting object in the database
        try:
            meeting = Meeting.objects.get(pk=meeting_id)
            meeting.subject = updated_subject
            meeting.date = updated_date
            meeting.start_time = updated_start_time
            meeting.end_time = updated_end_time
            meeting.participants = updated_participants
            meeting.save()
            return JsonResponse({'message': 'Meeting updated successfully'})
        except Meeting.DoesNotExist:
            return JsonResponse({'error': 'Meeting not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
