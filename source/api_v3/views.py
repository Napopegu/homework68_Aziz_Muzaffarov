import json

from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.renderers import JSONRenderer

from webapp.models import Article
from api_v2.serializers import ArticleSerializer, ArticleModelSerializer

@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


def json_echo_view(request, *args, **kwargs):
    answer = {
        'message': 'Hello World',
        'method': request.method
    }
    if request.body:
        answer['content'] = json.loads(request.body)
    return JsonResponse(answer)


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get("pk", None)
            article = Article.objects.get(pk=pk)
            article_info = ArticleModelSerializer(article).data
            return Response(article_info)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Нет данной статьи'}, status=400)

    def put(self, request, *args, **kwargs):
        try:
            pk = kwargs.get("pk", None)
            article = Article.objects.get(pk=pk)
            serializer = ArticleModelSerializer(article, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Нет данной статьи'}, status=400)





    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get("pk", None)
            article = Article.objects.get(pk=pk)
            article.delete()
            return Response("вы успешно удалили статью")

        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Нет данной статьи'}, status=400)

