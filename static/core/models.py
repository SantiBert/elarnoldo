from django.db import models
from ckeditor.fields import RichTextField


class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    cration_date = models.DateField(
        'Fecha de creación', auto_now=False, auto_now_add=True)
    modification_date = models.DateField(
        'Fecha de modificacion', auto_now=True, auto_now_add=False)
    delete_date = models.DateField(
        'Feacha de eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Season(ModeloBase):
    name = models.CharField('Nombre de temporada',
                            max_length=100, unique=True)
    tag = models.CharField(
        'Etiqueta', max_length=100, null=True, blank=True)
    referential_image = models.ImageField(
        'Imagen referencial', null=True, blank=True, upload_to='temporadas/')
    lenguje = models.BooleanField('ingles', default=False)

    class Meta:
        verbose_name = 'Temporada'
        verbose_name_plural = 'Temporadas'
        ordering = ['cration_date']

    def __str__(self):
        return self.name


class Capitulo(ModeloBase):
    name = models.CharField('Titulo del Capitulo',
                            max_length=150, unique=True)
    slug = models.CharField('Slug', max_length=150, unique=True)
    descripcion = models.TextField('Descripción', null=True, blank=True)
    season = models.ForeignKey(
        Season, related_name="Temporada", on_delete=models.CASCADE)
    number = models.IntegerField(
        'Número de capitulo')
    content = RichTextField('Contenido')
    referential_image = models.ImageField(
        'Imagen Referencial', upload_to='imagenes/', max_length=255, null=True, blank=True)
    published = models.BooleanField('Publicado/No publicado', default=False)
    publication_date = models.DateField('Fecha de publicación')

    class Meta:
        verbose_name = 'Capitulo'
        verbose_name_plural = 'Capitulos'
        ordering = ['number']

    def __str__(self):
        return self.name


class CapituloImage(models.Model):
    product = models.ForeignKey(Capitulo, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return "Capitulo {}".format(self.Capitulo.name)
