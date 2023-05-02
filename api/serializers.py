from rest_framework import serializers
from quizzes.models import Quiz,Option,DeadLine

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields= ["title","id"]

class QuizSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    class Meta:
        model = Quiz
        fields= "__all__"

class DeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeadLine
        fields= ["deadline",]