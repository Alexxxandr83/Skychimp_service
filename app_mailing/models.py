from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Модель клиента"""
    email = models.EmailField(max_length=50, verbose_name='Почта')
    full_name = models.CharField(max_length=128, verbose_name='Ф.И.О.')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    """Модель сообщения для рассылки"""
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Тело сообщения')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    """Модель рассылки"""
    PERIODICITY = [
        ('day', 'раз в день'),
        ('week', 'раз в неделю'),
        ('month', 'раз в месяц')
    ]
    STATUS = [
        ('stopped', 'завершена'),
        ('created', 'создана'),
        ('launched', 'запущена')
    ]

    name = models.CharField(max_length=50, verbose_name='Название рассылки')
    time = models.TimeField(verbose_name='Время рассылки')
    periodicity = models.CharField(max_length=5,
                                   choices=PERIODICITY,
                                   verbose_name='Периодичность')
    status = models.CharField(max_length=8,
                              choices=STATUS,
                              verbose_name='Статус', default='created')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    clients = models.ManyToManyField(Client, verbose_name='Клиенты')

    def __str__(self):
        return f'{self.name}--{self.time}--{self.periodicity}--{self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class MailingTry(models.Model):
    """Модель попыток рассылки"""
    MAILING_TRY_STATUS = [
        ('OK', 'Выполнено'),
        ('Err', 'Ошибка')
    ]

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    try_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Время попытки')
    try_status = models.CharField(max_length=3,
                                  choices=MAILING_TRY_STATUS,
                                  verbose_name='Статус')
    mail_service_response = models.TextField(verbose_name='Ответ почтового сервиса')

    def __str__(self):
        return f'{self.try_datetime}--{self.try_status}--{self.mailing}: {self.mail_service_response}'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
