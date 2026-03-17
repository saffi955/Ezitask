from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from . import models, serializers
from rest_framework.response import Response
from datetime import datetime



class Profile(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request):
        # get the id of the user form session
        user = models.User.objects.get(pk=1) # and use here
        dp = models.UserProfile.objects.get(user=user)
        serializer = serializers.UserSerielizer(user)
        serializer2 = serializers.UserProfileSerielizer(dp)
        return Response({"user": serializer.data, "profile": serializer2.data}, template_name="profile.html")
        # return Response(data= [serializer.data, serializer2.data])
    
    def post(self, request):
        profile = models.UserProfile.objects.get(id=request.data['pk'])
        serializer = serializers.UserProfileSerielizer(instance=profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if 'profile_picture' in serializer.validated_data:
            profile.profile_picture = serializer.validated_data['profile_picture']
            profile.save()
            return Response('Your Profile Picture is Updated..', status=status.HTTP_200_OK)
        

class UserView(APIView):
    def get(self, request):
        user = models.Attendence.objects.filter(user=1)
        serializer = serializers.AttendenceSerielizer(user, many=True)
        return Response(serializer.data)
    

current_date = datetime.now().date()
def attendence_validator(usr):
    a = models.Attendence.objects.filter(user=usr).filter(date=current_date)
    print(a)
    return a


class MarkPresent(APIView):
    def get(self, request):
        user = models.Attendence.objects.filter(user=1)
        serializer = serializers.AttendenceSerielizer(user, many=True)
        return Response(serializer.data)


    def post(self, request):
        userr = models.User.objects.get(id=request.user.id)
        if not attendence_validator(usr=userr):
            serializer = serializers.AttendenceSerielizer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # models.Attendence.objects.create(date=current_date, user=userr, status='Present')
            return Response("Marked as Present", status=status.HTTP_201_CREATED)
        else:
            return Response("You've already marked your Attendence for torday, try it again tomorrow!", status=status.HTTP_405_METHOD_NOT_ALLOWED)


class MarkLeave(APIView):
    def get(self, request):
        user = models.Attendence.objects.filter(user=1)
        serializer = serializers.AttendenceSerielizer(user, many=True)
        return Response(serializer.data)


    def post(self, request):
        reason = 'nothing'
        userr = models.User.objects.get(id=request.user.id)
        if not attendence_validator(usr=userr):
            serializer = serializers.AttendenceSerielizer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # models.Attendence.objects.create(date=current_date, user=userr, status='Leave Applied', leave_reason=reason)
            return Response("Leave Sent", status=status.HTTP_201_CREATED)
        else:
            return Response("You've already marked your Attendence for torday, try it again tomorrow!", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        

def attendence_counter(atts, date_from, date_to):
    absents = 0
    leaves = 0
    presents = 0
    days = abs((datetime.strptime(date_from, "%Y-%m-%d")-datetime.strptime(date_to, "%Y-%m-%d")).days)
    for r in atts:
        if r.status == 'Present':
            presents += 1
        elif r.status == 'Leave Accepted' or r.status == 'Leave Applied':
            leaves += 1
    absents += days - (leaves + presents)
    count_list = {"From": date_from, "Till": date_to,"User": 'all', "Total days": days, "Presents": presents, "Leaves": leaves, "Absents": absents}
    return count_list


class ModifyAttendence(APIView):
    def get(self, request, pk):
        item = models.Attendence.objects.get(id=pk)
        serializer = serializers.AttendenceSerielizer(item)
        return Response(serializer.data, status=status.HTTP_302_FOUND)


    def patch(self, request, pk):
        data = request.data
        serializer = serializers.AttendenceSerielizer(instance=models.Attendence.objects.get(id=pk), data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Attendence Updated/Modified..!', status=status.HTTP_200_OK)


    def delete(self, request, pk):
        item = models.Attendence.objects.get(id=pk)
        item.delete()
        return Response('Attendence Deleted..!', status=status.HTTP_200_OK)


class ClientView(APIView):
    def get(self, request):
        atts = models.Attendence.objects.all()
        serializer = serializers.AttendenceSerielizer(atts, many=True)
        # return render(request, 'index.html', context={'data': serializer.data})
        counts = attendence_counter(atts=atts, date_from="2023-01-01", date_to=str(current_date))
        return Response(data = [serializer.data, counts])


    def post(self, request):
        data = request.data
        serializer = serializers.AttendenceSerielizer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Attendence Marked..!', status=status.HTTP_201_CREATED)


class AttendenceFilterView(APIView):
    def get(self, request):
        user_id = request.GET['user_id']
        dfrom = request.GET['from']
        dto = request.GET['to']
        atts = models.Attendence.objects.filter(date__gte=dfrom).filter(date__lte=dto)
        counts = attendence_counter(atts=atts, date_from=dfrom, date_to=dto)
        if user_id != 'all':
            user = models.User.objects.get(pk=user_id)
            atts = atts.filter(user=user)
            counts["User"]= str(user)
        serializer = serializers.AttendenceSerielizer(atts, many=True)
        # return render(request, 'index.html', context={'data': serializer.data})
        return Response(data = [serializer.data, counts])


class LeaveView(APIView):
    def get(self, request):
        atts = models.Attendence.objects.filter(status="Leave Applied")
        serializer = serializers.AttendenceSerielizer(atts, many=True)
        return Response(data = [serializer.data, {"Total Leaves": atts.count()}])
    

    def patch(self, request):
        isinstance = models.Attendence.objects.get(pk=request.data['id'])
        serializer = serializers.AttendenceSerielizer(instance=isinstance, data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Leave Accepted', status=status.HTTP_202_ACCEPTED)
        


class Signin(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response(template_name="signin.html")

    def post(self, request):
        username = request.data['username']
        password = request.data['password']


class Signup(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response(template_name="signup.html")

    def post(self, request):
        pass





















'''
Client Panel
    Showing all the Attendences of all the user (with a proper count of leaves presents and absents) ...done
    able to add, modify and delete attendences ... done
    show Attendence from and to (also able to make a report) ...done
    Check the leave and able to Accept them. ...done


User Panel
	Showing all Attendences of the user ..done
	showing full profile ..done
	able to change the profile picture ......
	mark Present (with the restriction to mark once a day) ....done
	mark Leave with comment and reason ....done
	

'''