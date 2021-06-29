from rest_framework import serializers

from applications.twits.models import *


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        exclude = ()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ()


