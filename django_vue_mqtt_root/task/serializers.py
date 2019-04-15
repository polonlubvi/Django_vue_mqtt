from rest_framework import serializers
from .models import Task


#  class AutomationSerializer(serializers.ModelSerializer):
    #  class Meta:
        #  model = Automation
        #  fields = '__all__'


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'description', 'status')