from rest_framework import serializers

from films.models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('title', 'rating_kp', 'release_year')