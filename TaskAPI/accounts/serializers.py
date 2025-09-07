from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = ("username", "email", "password", "password2", "date_of_birth", "profile_photo")

  def validate(self, attrs):
    if attrs["password"] != attrs["password2"]:
      raise serializers.ValidationError({"password": "Passwords must match"})
    return attrs
    # where attrs is  adictionary of validated input data i.e usernmae, email, password, password2, date_od_birth, profile_photo

  def create(self, validated_data):
    #  the validated_data here is the returned attrs in dictionary form from def validated(self, attrs) above
    validated_data.pop("password2")
    #  this line prevents password2 from being saved to the database when creating an instance of the customed User
    user = User.objects.create_user(**validated_data)
    return user
    # **validated_data unpacks the dictionary into keyword arguments