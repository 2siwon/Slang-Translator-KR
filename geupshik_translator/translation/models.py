from django.db import models


class Visitor(models.Model):
    ip = models.IntegerField(default='127.0.0.1')
    logged_at = models.DateTimeField(auto_now_add=True)


class Translation(models.Model):
    author = models.ForeignKey(Visitor,
                               blank=True,
                               null=True,
                               on_delete=models.SET_NULL)
    pre_translated_text = models.TextField(max_length=1000)
    post_translated_text = models.TextField()
    edited_translated_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"visitor:{self.author}:translation"
