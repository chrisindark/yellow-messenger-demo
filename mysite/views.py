from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from tinyurls.constants import TINY_URL_DETAIL_CACHE_KEY
from tinyurls.models import TinyUrl
from tinyurls.serializers import TinyUrlSerializer


def redirect_view(request, tiny_id):
    """
    Redirect to the original url from a tiny id.
    """
    serializer_class = TinyUrlSerializer
    cache_key = TINY_URL_DETAIL_CACHE_KEY  # needs to be unique
    cache_time = 86400  # time in seconds for cache to be valid

    tiny_url = cache.get(cache_key.format(tiny_id))
    if not tiny_url:
        instance = get_object_or_404(TinyUrl, tiny_id=tiny_id)
        if instance:
            instance.last_used_on = timezone.now()
            serializer = serializer_class(instance)
            cache.set(cache_key.format(tiny_id), serializer.data, cache_time)
            return redirect(serializer.data.get('original_url'))
    else:
        return redirect(tiny_url.get('original_url'))
