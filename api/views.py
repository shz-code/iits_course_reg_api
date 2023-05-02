from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from quizzes.models import Quiz,DeadLine
from students.models import Student
from .serializers import QuizSerializer,DeadlineSerializer
import random
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def getQuizzes(request):
    try:
        quizzes = Quiz.objects.all()
        serialize = QuizSerializer(quizzes, many=True)
        # Choose random quizzes with every request
        randomQuizzes = random.sample(serialize.data,3)
        return Response(randomQuizzes)
    except:
        return Response("Not Found",status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getDeadline(request):
    try:
        deadline = DeadLine.objects.last()
        serialize = DeadlineSerializer(deadline)
        return Response(serialize.data)
    except:
        return Response("Not Found",status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def submitQuiz(request):
    if request.method == "POST":
        # Get the request from request
        res = request.data
        quizIds = []
        # Sort the response in ascending order to match server data order 
        res = sorted(res, key = lambda item: item['id'])
        count = 0
        clientQuizAns = []
        '''
         Loop through response and response.options to generate a list of dictionaries 
         containing quizId, selected quiz and option id to match server and client response
        '''
        for quiz in res:
            clientQuizCheck = []
            quizIds.append(quiz["id"])
            for option in quiz['options']:
                obj = {}
                obj["quizId"] = quiz["id"]
                obj["flag"] = option["isSelected"]
                obj["optionId"] = option["id"]
                clientQuizCheck.append(obj)
            clientQuizAns.append({})
            clientQuizAns[count] = clientQuizCheck
            count += 1
        try:
            quizzes = Quiz.objects.filter(id__in=quizIds)
        except:
            return Response("Not Found",status=status.HTTP_404_NOT_FOUND)
        serverQuizAns = []
        count = 0
        '''
         Loop through serverData and serverData.options to generate a list of dictionaries 
         containing quizId, selected quiz and option id to match server and client response
        '''
        for quiz in quizzes:
            serverQuizCheck = []
            for option in quiz.options.all():
                obj = {}
                obj["quizId"] = quiz.id
                obj["flag"] = option.isCorrect
                obj["optionId"] = option.id
                serverQuizCheck.append(obj)
            serverQuizAns.append({})
            serverQuizAns[count] = serverQuizCheck
            count += 1

        # Count the number of dictionaries matching both client and server quiz
        rightAns = 0;
        for i in range(0,len(serverQuizAns)):
            if(serverQuizAns[i] == clientQuizAns[i]):
                rightAns += 1

        # print(rightAns)
        return Response({"totalQuiz": len(serverQuizAns),"rightAns":rightAns,"status":200})

@api_view(['POST'])
def submitForm(request):
    if request.method == "POST":
        res = request.data
        name = res['name']
        email = res['email']
        studentId = res['studentId']
        phone = res['phone']
        phone = phone[-11:]
        reason = res['reason']
        rightAns = res['rightAns']
        totalQuiz = res['totalQuiz']
        try:
            Student.objects.get(studentId = studentId)
            return Response({"msg":"studentId_copy","status":403})
        except:
            pass
        try:
            Student.objects.get(phone = phone)
            return Response({"msg":"phone_copy","status":403})
        except:
            pass
        try:
            Student.objects.get(email = email)
            return Response({"msg":"email_copy","status":403})
        except:
            pass
        Student.objects.create(
            name = name,
            email = email,
            studentId = studentId,
            phone = phone,
            reason = reason,
            rightAns = rightAns,
            totalQuiz = totalQuiz
        )
    return Response({"status":200})