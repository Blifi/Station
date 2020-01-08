from rest_framework import serializers
from employee.models import Employee


class SnippetSerializer(serializers.Serializer):
    #eid = serializers.IntegerField()
    #ename = serializers.CharField()
    #eemail = serializers.CharField()
    #econtact = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.eid = validated_data.get('eid', instance.eid)
        instance.ename = validated_data.get('ename', instance.ename)
        instance.eemail = validated_data.get('eemail', instance.eemail)
        instance.econtact = validated_data.get('econtact', instance.econtact)
        instance.save()
        return instance