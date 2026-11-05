from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField("Title", max_length=200)
    slug = models.SlugField("Slug (URL)", max_length=200, unique=True)
    content = models.TextField("Content", help_text="You can use HTML.")
    show_in_menu = models.BooleanField("Show in menu", default=True)
    order = models.PositiveIntegerField("Menu order", default=0)
    created = models.DateTimeField("Created at", auto_now_add=True)
    updated = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:page', kwargs={'slug': self.slug})


class ContactInfo(models.Model):
    company_name = models.CharField("Company Name", max_length=200, blank=True)
    tagline = models.CharField("Tagline / Slogan", max_length=300, blank=True)
    address = models.CharField("Address", max_length=300, blank=True)
    phone = models.CharField("Phone", max_length=50, blank=True)
    email = models.EmailField("E-mail", blank=True)
    nip = models.CharField("VAT ID / NIP", max_length=20, blank=True)
    opening_hours = models.CharField("Opening Hours", max_length=200, blank=True)
    footer_text = models.CharField("Footer Text", max_length=300, blank=True)

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return self.company_name or "Contact Info"

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Service(models.Model):
    title = models.CharField("Service Name", max_length=200)
    description = models.TextField("Description")
    icon = models.CharField("Bootstrap Icon class", max_length=50,
                            default="bi-translate",
                            help_text="Bootstrap Icons class name, e.g. bi-translate")
    order = models.PositiveIntegerField("Order", default=0)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['order']

    def __str__(self):
        return self.title