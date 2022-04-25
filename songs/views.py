from django.shortcuts import get_object_or_404
from .models import Song
from .serializers import SongSerializer
from rest_framework import generics, mixins
from rest_framework.response import Response

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.GenericAPIView,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

    def patch(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        action = self.request.query_params.get('action')

        if action == "like":
            serializer = SongSerializer(song, data={'num_likes': song.num_likes + 1}, partial=True)
        elif action == "dislike":
            serializer = SongSerializer(song, data={'num_likes': song.num_likes - 1}, partial=True)
        else:
            serializer = SongSerializer(song, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
            

