from django.db import models


class Chat(models.Model):
    is_group_chat = models.BooleanField(default=False)
    topic = models.CharField(max_length=128)

    last_message = models.ForeignKey('Message',
                                     null=True,
                                     on_delete=models.SET_NULL,
                                     related_name='chats')

    class Meta:
        verbose_name = 'чат'
        verbose_name_plural = 'чаты'
        ordering = ['topic', 'is_group_chat']


class Member(models.Model):
    chat = models.ForeignKey(Chat,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='members')
    # ?
    new_messages = models.TextField()
    last_read_message = models.ForeignKey('Message',
                                          on_delete=models.SET_NULL,
                                          null=True)

    class Meta:
        verbose_name = 'член'
        verbose_name_plural = 'члены'
        ordering = ['chat']


class Message(models.Model):
    chat = models.ForeignKey(Chat,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='messages')

    user = models.ForeignKey('users.User',
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='messages')

    content = models.CharField(max_length=400)
    added_at = models.DateTimeField()

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ['chat', 'user']


class Attachment(models.Model):
    chat = models.ForeignKey(Chat,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='attachments')

    user = models.ForeignKey('users.User',
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='attachments')

    message = models.ForeignKey(Message,
                                models.SET_NULL,
                                null=True,
                                related_name='attachments')
    kind = models.CharField(max_length=18)
    url = models.URLField()

    class Meta:
        verbose_name = 'приложение'
        verbose_name_plural = 'приложения'
        ordering = ['chat', 'user']
