from rest_framework import serializers

from .import models



class HelloSerializer(serializers.Serializer):
    """Serializes a new field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSeriliazer(serializers.ModelSerializer):
    """Serializes for our user profile objects"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email','name', 'password')
        # Add extra keywords argument for the model to make password write only
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

#create a ProfileFeedItemSerializer
class ProfileFeedItemSerializer(serializers.HyperlinkedModelSerializer):
    """A serializer for profile feed item."""
    # define class Meta
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        #set user_profile to read only.
        extra_kwargs = {'user_profile': {'read_only': True}}
