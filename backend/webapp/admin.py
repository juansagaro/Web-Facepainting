"""
Configuración del panel de administración para Body Art Madrid.

Conceptos Django Admin importantes:
- @admin.register(Model) vincula un modelo a su clase de admin.
- list_display: qué columnas aparecen en el listado.
- list_filter: filtros laterales (como categorías).
- search_fields: campos donde busca la barra de búsqueda.
- list_editable: campos editables directamente en el listado (sin abrir).
- readonly_fields: campos que el admin muestra pero no permite editar.
- fieldsets: organiza los campos del formulario en secciones.
- actions: acciones masivas (seleccionar varios → ejecutar acción).
"""
from django.contrib import admin
from django.utils.html import format_html
from .models import ContactMessage, GalleryImage, Service, FAQ, PageSEO


# ============================================
# CONTACTO
# ============================================
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Los mensajes de contacto son de solo lectura en el admin
    (los crea el formulario de la web, no la dueña manualmente).
    Solo puede marcarlos como leídos/no leídos.
    """

    list_display = ['name', 'email', 'event_type', 'created_at', 'is_read']
    list_filter = ['is_read', 'event_type', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = [
        'name', 'email', 'phone', 'event_type',
        'event_date', 'message', 'created_at',
    ]
    list_per_page = 25

    # Ordenar: no leídos primero, luego por fecha
    ordering = ['is_read', '-created_at']

    fieldsets = [
        ('Datos del cliente', {
            'fields': ('name', 'email', 'phone'),
        }),
        ('Detalles del evento', {
            'fields': ('event_type', 'event_date', 'message'),
        }),
        ('Estado', {
            'fields': ('is_read', 'created_at'),
        }),
    ]

    # No permitir crear mensajes desde el admin
    def has_add_permission(self, request):
        return False

    # Acción masiva: marcar como leídos
    @admin.action(description='Marcar como leídos')
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    # Acción masiva: marcar como no leídos
    @admin.action(description='Marcar como no leídos')
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)

    actions = ['mark_as_read', 'mark_as_unread']


# ============================================
# GALERÍA
# ============================================
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    """
    Gestión de imágenes de galería con vista previa en miniatura.
    """

    list_display = ['image_preview', 'alt_text', 'category', 'order', 'is_visible']
    list_filter = ['category', 'is_visible']
    search_fields = ['alt_text', 'caption']
    list_editable = ['order', 'is_visible']
    list_per_page = 20

    fieldsets = [
        (None, {
            'fields': ('image', 'image_preview_large', 'alt_text', 'caption'),
        }),
        ('Clasificación', {
            'fields': ('category', 'order', 'is_visible'),
        }),
    ]

    readonly_fields = ['image_preview_large']

    @admin.display(description='Vista previa')
    def image_preview(self, obj):
        """Miniatura de 60px en el listado."""
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px; border-radius:4px; object-fit:cover;" />',
                obj.image.url,
            )
        return '—'

    @admin.display(description='Vista previa')
    def image_preview_large(self, obj):
        """Vista previa de 200px en el formulario de edición."""
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:200px; border-radius:6px;" />',
                obj.image.url,
            )
        return 'Sin imagen'


# ============================================
# SERVICIOS
# ============================================
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Gestión de servicios. El slug no se debe cambiar una vez creado
    porque está vinculado a las URLs y las vistas.
    """

    list_display = ['title', 'slug', 'is_external', 'order', 'is_visible']
    list_filter = ['is_external', 'is_visible']
    list_editable = ['order', 'is_visible']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = [
        (None, {
            'fields': ('title', 'slug', 'tagline', 'description'),
        }),
        ('Imágenes', {
            'fields': ('card_image', 'hero_image'),
        }),
        ('Enlace externo', {
            'fields': ('is_external', 'external_url'),
            'classes': ('collapse',),
            'description': 'Solo para servicios que enlazan a otra web (Tatuajes, Belly).',
        }),
        ('Configuración', {
            'fields': ('order', 'is_visible'),
        }),
    ]


# ============================================
# FAQ
# ============================================
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """
    Preguntas frecuentes editables. El campo 'order' permite
    ordenarlas directamente desde el listado.
    """

    list_display = ['question_short', 'order', 'is_visible']
    list_editable = ['order', 'is_visible']
    search_fields = ['question', 'answer']
    list_per_page = 20

    @admin.display(description='Pregunta')
    def question_short(self, obj):
        """Trunca la pregunta a 80 caracteres en el listado."""
        q = obj.question
        return q if len(q) <= 80 else q[:77] + '...'


# ============================================
# SEO
# ============================================
@admin.register(PageSEO)
class PageSEOAdmin(admin.ModelAdmin):
    """
    Metadatos SEO por página. page_id identifica qué página
    corresponde (home, nosotros, galeria, etc.).
    """

    list_display = ['page_id', 'title', 'meta_description_short']
    search_fields = ['page_id', 'title']

    @admin.display(description='Meta description')
    def meta_description_short(self, obj):
        d = obj.meta_description
        return d if len(d) <= 60 else d[:57] + '...'


# ============================================
# PERSONALIZAR EL ADMIN
# ============================================
admin.site.site_header = 'Body Art Madrid — Administración'
admin.site.site_title = 'Body Art Madrid Admin'
admin.site.index_title = 'Panel de gestión'
