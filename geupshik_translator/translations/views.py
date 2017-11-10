from rest_framework import generics, mixins

from .models import Visitor, Translation
from .serializers import TranslationSerializer


class TranslatorList(mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # 방문자 정해주기
        print(self.request.data)
        visitor = Visitor.objects.create()
        serializer.save(author=visitor)
        # 이후 model의 override된 save() method로 이어짐
        # 그 부분에서 post_translated_text field populate함
