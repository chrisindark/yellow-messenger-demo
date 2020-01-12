from django.http import JsonResponse
from django.core.cache import cache
from django.utils import timezone
from rest_framework import generics, status, pagination
from rest_framework.response import Response

from users.permissions import IsNotAuthenticated
from tinyurls.models import TinyUrl
from tinyurls.serializers import TinyUrlSerializer, TinyUrlCreateSerializer
from tinyurls.constants import TINY_URL_DETAIL_CACHE_KEY


# Create your views here.
class TinyUrlPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class TinyUrlListCreateApiView(generics.ListCreateAPIView):
    queryset = TinyUrl.objects.all()
    serializer_class = TinyUrlSerializer
    pagination_class = TinyUrlPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TinyUrlCreateSerializer
            pass
        return self.serializer_class

    def get_permissions(self):
        if self.request.method == 'POST':
            return (IsNotAuthenticated(),)
        return (IsNotAuthenticated(),)

    def perform_create(self, serializer):
        serializer.save()
        return Response({}, status=status.HTTP_200_OK)


class TinyUrlDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TinyUrl.objects.all()
    serializer_class = TinyUrlSerializer
    lookup_field = 'tiny_id'
    cache_key = TINY_URL_DETAIL_CACHE_KEY  # needs to be unique
    cache_time = 86400  # time in seconds for cache to be valid

    def retrieve(self, request, *args, **kwargs):
        tiny_id = kwargs.get('tiny_id')
        tiny_url = cache.get(self.cache_key.format(tiny_id))
        if not tiny_url:
            instance = self.get_object()
            instance.last_used_on = timezone.now()
            instance.save()
            serializer = self.get_serializer(instance)
            cache.set(self.cache_key.format(tiny_id), serializer.data, self.cache_time)
            return Response(serializer.data)
        else:
            return JsonResponse(tiny_url, safe=False)
