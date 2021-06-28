from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Company(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name='Наименование компании',
    )

    inn = models.CharField(
        max_length=10,
        verbose_name='ИНН',
    )

    kpp = models.CharField(
        max_length=9,
        verbose_name='КПП',
    )

    legal_address = models.CharField(
        max_length=300,
        verbose_name='Юридический адрес',
    )

    actual_address = models.CharField(
        max_length=300,
        verbose_name='Фактический адрес',
        blank=True,
        default='',
    )

    users = models.ManyToManyField(
        User,
    )

    name = models.CharField(
        max_length=100,
        verbose_name='Контактное лицо (ФИО)',
    )

    email_corp = models.EmailField(
    )

    phone_corp = models.CharField(
        max_length=12,
        verbose_name='Контактный номер телефона',
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Customer(Company):

    def __str__(self):
        return self.title


class Producer(Company):

    def __str__(self):
        return self.title


class Order(models.Model):
    """Заказ конкретного Заказчика"""

    CATEGORY_TYPES = [
        ('1', 'Шкафы управления и автоматики'),
        ('2', 'Шкафы силовые и освещения до 250 А'),
        ('3', 'Шкафы силовые и освещения свыше 250 А'),
        ('4', 'Главные распред. щиты (ГРЩ)'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name='Заказчик',
    )

    title = models.CharField(
        max_length=300,
        verbose_name='Наименование заказа',
    )

    category = models.CharField(
        choices=CATEGORY_TYPES,
        max_length=10,
        verbose_name='Наименование категории',
    )

    city_order = models.CharField(
        max_length=50,
        verbose_name='Город',
        blank=True,
        default='',
    )

    budget_order = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Бюджет, руб.',
        blank=True,
        default=None,
    )

    expiration_date = models.DateField(
        default=date.today,
        verbose_name='Дата окончания подачи предложений',
    )

    placement_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    last_modified_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Последние изменения',
    )

    requirement = models.CharField(
        max_length=300,
        verbose_name='Особые требования к исполнителю',
        blank=True,
        default='',
    )

    description = models.TextField(
        max_length=50000,
        verbose_name='Описание',
    )

    file_order = models.FileField(
        upload_to='',
        verbose_name='Прикрепить файлы',
        blank=True,
        default='',
    )

    def __str__(self):
        return '{}. Категория: {}. Заказчик: {}. До: {}. Бюджет: {}'.format(self.title, self.get_category_display(), self.customer, self.expiration_date, self.budget_order)
        #self.get_title_display() позволяет вывсти не короткое значение, а именно наименование категории


class Offer(models.Model):
    """Предложение для конкретного Тендера от конкретного Исполнителя"""

    title = models.CharField(
        max_length=300,
        verbose_name='Наименование заказа',
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Наименование заказа',
    )

    producer = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
        verbose_name='Исполнитель',
    )

    price_offer = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Бюджет, руб.',
        blank=True,
        default=None,
    )

    placement_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    last_modified_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Последние изменения',
    )

    description = models.TextField(
        max_length=5000,
        verbose_name='Условия',
    )

    file_offer = models.FileField(
        upload_to='',
        verbose_name='Прикрепить файлы',
        blank=True,
        default=None,
    )

    # Принятие предложения, кнопка в интерфейсе. Если True, то создается объект класса Contract
    # adoption = False

    def __str__(self):
        return f'Исполнитель: {self.producer} / Заказ: {self.title} / Предложение: {self.price_offer}'


class Contract(models.Model):
    """Предложение для конкретного Тендера от конкретного Исполнителя"""

    title = models.CharField(
        max_length=300,
        verbose_name='Наименование контракта',
    )

    offer = models.ForeignKey(
        Offer,
        on_delete=models.CASCADE,
        verbose_name='Предложения',
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ',
    )

    price_contract = models.FloatField(
        verbose_name='Цена контракта, руб.',
    )

    start_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания контракта',
    )

    finish_date = models.DateField(
        auto_now=True,
        verbose_name='Дата окончания контракта',
    )

    description_contract = models.TextField(
        max_length=5000,
        verbose_name='Описание контракта',
    )

    file_contract = models.FileField(
        upload_to='',
        verbose_name='Прикрепить файлы контракта',
        blank=True,
        default=None,
    )

    is_finished = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f'Наименование контракта: {self.title} / Заказ: {self.title} / Стоимость контракта: {self.price_contract}, / {self.start_date} - {self.finish_date}'


class Message(models.Model):

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    producer = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE
    )

    message_date = models.DateTimeField(
        auto_now_add=True,
    )

    is_edited = models.BooleanField(
        default=False,
    )

    was_sent = models.BooleanField(
        default=False,
    )

    was_read = models.BooleanField(
        default=False,
    )

    description = models.CharField(
        max_length=1000,
    )


class Review(models.Model):
    RATING_FILLED = [
            ('1', 1),
            ('2', 2),
            ('3', 3),
            ('4', 4),
            ('5', 5),
    ]

    rating = models.CharField(
        choices=RATING_FILLED,
        default='3',
        max_length=1,
    )

    description = models.CharField(
        max_length=1000
    )

    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        #related_name='+',
    )

    producer = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        #related_name='+',
    )

    review_date = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return '{}, {}'.format(self.author, self.review_date)


class Tag(models.Model):

    name = models.CharField(
        max_length=300,
        verbose_name='Тэг',
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        blank=True,
    )

