from django.db import models


class Visitor(models.Model):
    ip = models.GenericIPAddressField(blank=True, null=True)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'visitor:{self.pk}'


class Translation(models.Model):
    author = models.ForeignKey(Visitor,
                               blank=True,
                               null=True,
                               on_delete=models.SET_NULL)
    pre_translated_text = models.TextField(max_length=1000)  # 필수 필드
    post_translated_text = models.TextField()  # 필수 필드
    edited_translated_text = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # 필수 필드

    def __str__(self):
        return f"visitor:{self.author}:translation"

    def save(self, *args, **kwargs):
        # 번역 알고리즘 관련 부분 - utils.py
        # 번역할 일반어를 form으로 제출 시, 번역된 급식체를 필드에 저장하면서
        # 모델 인스턴스를 저장함
        self.post_translated_text = self.pre_translated_text + '번역됨'
        super().save(*args, **kwargs)
