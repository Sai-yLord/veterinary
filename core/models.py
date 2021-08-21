from django.db import models


from django.utils.translation import gettext_lazy as _


class News(models.Model):
    title = models.CharField(_('Название'), max_length=50)
    description = models.TextField(_('Описание'))
    picture = models.ImageField(_('Изображение'), blank=True)
    created = models.DateField(auto_now_add=True, null=True)
    views = models.PositiveIntegerField(default=0)


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

class Doctors(models.Model):
    fullname = models.CharField(_("Ф.И.О"), max_length=250)
    experience = models.CharField(_('Стаж'), max_length=10)
    description = models.TextField(_('О себе'))
    picture = models.ImageField(_('Изображение'), blank=True)


    class Meta:
        verbose_name = 'Ветеринара'
        verbose_name_plural = 'Ветеринары'

    def __str__(self):
        return self.fullname

class Services(models.Model):
    title = models.CharField(_('Название'), max_length=50)
    description = models.TextField(_('Подробности'))
    picture = models.ImageField(_('Изображение'), blank=True)


    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    description = models.TextField(_('О нас'))

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.description

class Advices(models.Model):
    title = models.CharField(_('Название'), max_length=50)
    description = models.TextField(_('Текст'))
    picture = models.ImageField(_('Изображение'), blank=True)

    class Meta:
        verbose_name = 'Полезный совет'
        verbose_name_plural = 'Полезные советы'

    def __str__(self):
        return self.title

class Address(models.Model):
    address = models.CharField(_('Адрес'), max_length=255)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адресы'

    def __str__(self):
        return self.address

class Contacts(models.Model):
    phone_number = models.CharField(_('Контакт'), max_length=15)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.phone_number

class Contact(models.Model):
    phone_number = models.CharField(_('Контакт'), max_length=15)
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, related_name='contact')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.phone_number

class Feedback(models.Model):
    fullname = models.CharField(_("Ф.И.О"), max_length=250)
    area = models.CharField(_('Ваша область'), max_length=150)
    email = models.EmailField(_('Почта'), max_length=155, blank=True)
    phone_number = models.CharField(_('Ваш номер телефона'), max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.phone_number

class Products(models.Model):
    title = models.CharField(_('Название'), max_length=50)
    price = models.CharField(_('Цена'), max_length=255)
    picture = models.ImageField(_('Изображение'), blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title