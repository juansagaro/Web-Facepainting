"""
Modelos de datos para Body Art Madrid.

Cada modelo representa algo que la dueña del negocio puede gestionar
desde el panel de administración sin necesidad de tocar código.

Conceptos Django importantes:
- Cada clase que hereda de models.Model se convierte en una tabla SQL.
- Cada atributo de la clase (models.CharField, etc.) se convierte en una columna.
- Django genera automáticamente un campo `id` (primary key autoincremental).
- `__str__` define cómo aparece el objeto en el admin.
- `class Meta` configura opciones de la tabla (nombre, orden, etc.).
- `ordering` define el orden por defecto en las queries.
"""
from django.db import models
from django.utils import timezone


# ============================================
# CONTACTO — Mensajes del formulario web
# ============================================
class ContactMessage(models.Model):
    """
    Cada envío del formulario de contacto crea un registro aquí.
    La dueña puede verlos desde el admin en vez de depender solo del email.
    """

    # Opciones para el tipo de evento (mismas que el <select> del formulario)
    EVENT_CHOICES = [
        ('boda', 'Boda'),
        ('cumpleanos', 'Cumpleaños infantil'),
        ('comunion', 'Comunión'),
        ('corporativo', 'Evento corporativo'),
        ('festival', 'Festival / Fiesta'),
        ('sesion', 'Sesión de fotos'),
        ('otro', 'Otro'),
    ]

    name = models.CharField('Nombre', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Teléfono', max_length=20, blank=True)
    event_type = models.CharField(
        'Tipo de evento',
        max_length=20,
        choices=EVENT_CHOICES,
        blank=True,
    )
    event_date = models.DateField('Fecha del evento', null=True, blank=True)
    message = models.TextField('Mensaje')

    # Campos automáticos para gestión interna
    created_at = models.DateTimeField('Recibido', default=timezone.now)
    is_read = models.BooleanField('Leído', default=False)

    class Meta:
        verbose_name = 'Mensaje de contacto'
        verbose_name_plural = 'Mensajes de contacto'
        ordering = ['-created_at']  # Más recientes primero

    def __str__(self):
        return f'{self.name} — {self.event_type or "sin tipo"} ({self.created_at:%d/%m/%Y})'


# ============================================
# GALERÍA — Imágenes que se muestran en /galeria/
# ============================================
class GalleryImage(models.Model):
    """
    Imágenes de la galería. La dueña sube fotos desde el admin
    y aparecen automáticamente en la web.

    upload_to='gallery/' → las fotos se guardan en MEDIA_ROOT/gallery/
    """

    CATEGORY_CHOICES = [
        ('facepainting', 'Facepainting'),
        ('halloween', 'Halloween'),
        ('bodypaint', 'Body Paint'),
        ('bellypaint', 'Belly Paint'),
        ('glitterbar', 'Glitter Bar'),
    ]

    image = models.ImageField('Imagen', upload_to='gallery/')
    alt_text = models.CharField(
        'Texto alternativo',
        max_length=200,
        help_text='Describe la imagen para SEO y accesibilidad.',
    )
    category = models.CharField(
        'Categoría',
        max_length=20,
        choices=CATEGORY_CHOICES,
    )
    caption = models.CharField('Pie de foto', max_length=200, blank=True)
    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text='Menor número = aparece primero.',
    )
    is_visible = models.BooleanField('Visible', default=True)
    created_at = models.DateTimeField('Fecha de subida', auto_now_add=True)

    class Meta:
        verbose_name = 'Imagen de galería'
        verbose_name_plural = 'Imágenes de galería'
        ordering = ['order', '-created_at']

    def __str__(self):
        return f'{self.alt_text[:50]} [{self.get_category_display()}]'


# ============================================
# SERVICIOS — Los 4 servicios internos
# ============================================
class Service(models.Model):
    """
    Define los servicios que aparecen en la home y en sus páginas individuales.

    slug = identificador URL-friendly. Ej: 'facepainting', 'bodypaint'.
    Se usa para generar la URL del servicio y para identificarlo en el código.
    """

    slug = models.SlugField(
        'Slug',
        max_length=50,
        unique=True,
        help_text='Identificador URL (ej: facepainting, bodypaint). No cambiar.',
    )
    title = models.CharField('Título', max_length=100)
    tagline = models.CharField(
        'Eslogan',
        max_length=200,
        help_text='Frase corta que aparece bajo el título en la home.',
    )
    description = models.TextField(
        'Descripción',
        help_text='Texto largo para la página individual del servicio.',
    )
    card_image = models.ImageField(
        'Imagen de tarjeta',
        upload_to='services/',
        blank=True,
        help_text='Imagen que aparece en la tarjeta de servicios de la home.',
    )
    hero_image = models.ImageField(
        'Imagen hero',
        upload_to='services/',
        blank=True,
        help_text='Imagen grande de la cabecera de la página del servicio.',
    )
    is_external = models.BooleanField(
        'Servicio externo',
        default=False,
        help_text='Si es externo (Tatuajes, Belly), se enlaza a otra web.',
    )
    external_url = models.URLField(
        'URL externa',
        blank=True,
        help_text='Solo si es servicio externo.',
    )
    order = models.PositiveIntegerField('Orden', default=0)
    is_visible = models.BooleanField('Visible', default=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['order']

    def __str__(self):
        return self.title


# ============================================
# FAQ — Preguntas frecuentes
# ============================================
class FAQ(models.Model):
    """
    Preguntas frecuentes que aparecen en la home (y opcionalmente en
    otras páginas). La dueña puede añadir/editar/reordenar desde el admin.
    """

    question = models.CharField('Pregunta', max_length=200)
    answer = models.TextField('Respuesta')
    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text='Menor número = aparece primero.',
    )
    is_visible = models.BooleanField('Visible', default=True)

    class Meta:
        verbose_name = 'Pregunta frecuente'
        verbose_name_plural = 'Preguntas frecuentes'
        ordering = ['order']

    def __str__(self):
        return self.question[:80]


# ============================================
# SEO — Metadatos por página
# ============================================
class PageSEO(models.Model):
    """
    Permite editar el <title> y la meta description de cada página
    desde el admin, sin tocar código.

    page_id = identificador interno que coincide con el nombre de la vista.
    Ej: 'home', 'nosotros', 'galeria', 'contacto', etc.
    """

    page_id = models.CharField(
        'Identificador de página',
        max_length=50,
        unique=True,
        help_text='Nombre interno (home, nosotros, galeria, etc.). No cambiar.',
    )
    title = models.CharField(
        'Title (SEO)',
        max_length=70,
        help_text='Aparece en la pestaña del navegador y en Google. Máximo ~60 caracteres.',
    )
    meta_description = models.CharField(
        'Meta description',
        max_length=160,
        help_text='Resumen que aparece en Google bajo el título. Máximo ~155 caracteres.',
    )
    og_title = models.CharField('OG Title', max_length=100, blank=True)
    og_description = models.CharField('OG Description', max_length=200, blank=True)

    class Meta:
        verbose_name = 'SEO de página'
        verbose_name_plural = 'SEO de páginas'

    def __str__(self):
        return f'SEO: {self.page_id}'
