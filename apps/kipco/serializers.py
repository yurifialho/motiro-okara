from rest_framework.serializers import ModelSerializer
from apps.kipco.models import IntensiveProcess, ProcessGoal, Activity, ActivityGoal, Intention, Desire, AgentType, AgentSpecialty, Agent


class IntensiveProcessSerializer(ModelSerializer):

    class Meta:
        model = IntensiveProcess
        fields = '__all__'


class ProcessGoalSerializer(ModelSerializer):

    class Meta:
        model = ProcessGoal
        fields = '__all__'


class ActivitySerializer(ModelSerializer):

    class Meta:
        model = Activity
        fields = '__all__'


class ActivityGoalSerializer(ModelSerializer):

    class Meta:
        model = ActivityGoal
        fields = '__all__'


class IntentionSerializer(ModelSerializer):

    class Meta:
        model = Intention
        fields = '__all__'


class DesireSerializer(ModelSerializer):

    class Meta:
        model = Desire
        fields = '__all__'


class AgentTypeSerializer(ModelSerializer):

    class Meta:
        model = AgentType
        fields = '__all__'


class AgentSpecialtySerializer(ModelSerializer):

    class Meta:
        model = AgentSpecialty
        fields = '__all__'


class AgentSerializer(ModelSerializer):

    class Meta:
        model = Agent
        fields = '__all__'
