from .models import Student
from rest_framework import serializers


def start_with_f(value):
    if value[0].lower() != 'f':
        raise serializers.ValidationError('name should be start with f')

class StudentSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(validators=[start_with_f])
    class Meta:
        model = Student
        fields = ["id","name", "roll", "city"]
        #read_only_fields=['name','roll']
        #extra_kwargs = {'name':{'read_only':True}}

    # id = serializers.IntegerField()
    # name = serializers.CharField(max_length=50,validators=[start_with_f])
    # roll = serializers.IntegerField()
    # city = serializers.CharField(max_length=50)

    def validate_roll(self, value):
        if value >= 200:
            print(value)
            raise serializers.ValidationError('seat full!')
        return value

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        print(nm)
        if nm.lower() == 'foram' and ct.lower() != 'unjha':
            raise serializers.ValidationError('city must be unjha')
        return data

    # def create(self, validated_data):
    #     return Student.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.roll = validated_data.get('roll', instance.roll)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.save()
    #     return instance

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = "__all__"
