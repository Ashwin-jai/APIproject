from rest_framework import serializers
from .models import Employee


class EmployeeSerializers(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    job = serializers.CharField(required=True)


    class Meta:
        model = Employee
        fields = ('name', 'email', 'job')

class updateserialzers(serializers.ModelSerializer):
    name = serializers.CharField(required=False, allow_null=True)
    email = serializers.CharField(required=False, allow_null=True)
    job = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model =Employee
        fields =('name','email','job')


    def validate(self, attrs):
        name = attrs.get('name', None)
        if name is not None and not name.isalpha():
            raise serializers.ValidationError(f'Name should be accept only Alphabets')