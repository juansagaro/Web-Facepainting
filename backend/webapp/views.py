"""
Vistas de webapp — conectadas a la base de datos.

Flujo de cada vista:
1. Consultar la BD para obtener datos dinámicos (FAQ, galería, servicios, SEO...)
2. Pasar los datos al template como contexto
3. El template decide cómo renderizarlos

El patrón .first() en PageSEO permite que la vista funcione incluso
si no hay datos SEO cargados — el template usa valores por defecto.

IMPORTANTE sobre el formulario de contacto:
- GET  → muestra el formulario vacío
- POST → valida y guarda en BD, luego redirige (patrón POST-Redirect-GET)
  PRG evita que el usuario reenvíe el formulario al refrescar la página.
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage, GalleryImage, Service, FAQ, PageSEO


def _get_seo(page_id):
    """
    Helper que busca los metadatos SEO para una página.
    Devuelve el objeto PageSEO o None (el template usa defaults).
    """
    return PageSEO.objects.filter(page_id=page_id).first()


def home(request):
    """Página principal — funnel de conversión."""
    context = {
        'active_page': 'home',
        'seo': _get_seo('home'),
        'services': Service.objects.filter(is_visible=True),
        'faqs': FAQ.objects.filter(is_visible=True),
    }
    return render(request, 'home.html', context)


def nosotros(request):
    """Sobre nosotros — historia, valores."""
    context = {
        'active_page': 'nosotros',
        'seo': _get_seo('nosotros'),
    }
    return render(request, 'nosotros.html', context)


def galeria(request):
    """Galería de trabajos con filtros por categoría."""
    context = {
        'active_page': 'galeria',
        'seo': _get_seo('galeria'),
        'images': GalleryImage.objects.filter(is_visible=True),
    }
    return render(request, 'galeria.html', context)


def contacto(request):
    """
    Formulario de contacto.
    GET  → muestra formulario vacío
    POST → valida, guarda en BD, muestra mensaje de éxito
    """
    if request.method == 'POST':
        # Extraer datos del formulario
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        event_type = request.POST.get('event-type', '').strip()
        event_date = request.POST.get('event-date', '').strip() or None
        message_text = request.POST.get('message', '').strip()

        # Validación básica (el frontend también valida, esto es el safety net)
        errors = []
        if not name:
            errors.append('El nombre es obligatorio.')
        if not email:
            errors.append('El email es obligatorio.')
        if not message_text:
            errors.append('El mensaje es obligatorio.')

        if errors:
            # Devolver al formulario con los errores y los datos que ya escribió
            # Usamos un dict con claves sin guiones para que el template pueda acceder
            context = {
                'active_page': 'contacto',
                'seo': _get_seo('contacto'),
                'errors': errors,
                'form_data': {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'event_type': event_type,
                    'event_date': event_date or '',
                    'message': message_text,
                },
            }
            return render(request, 'contacto.html', context)

        # Guardar en la base de datos
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            event_type=event_type,
            event_date=event_date,
            message=message_text,
        )

        # Patrón PRG: redirigir para evitar reenvío del formulario al refrescar
        messages.success(request, '¡Mensaje enviado correctamente! Te responderemos lo antes posible.')
        return redirect('contacto')

    # GET — formulario vacío
    context = {
        'active_page': 'contacto',
        'seo': _get_seo('contacto'),
    }
    return render(request, 'contacto.html', context)


def facepainting(request):
    """Servicio: Facepainting."""
    context = {
        'active_page': 'facepainting',
        'seo': _get_seo('facepainting'),
    }
    return render(request, 'facepainting.html', context)


def bodypaint(request):
    """Servicio: Body Painting."""
    context = {
        'active_page': 'bodypaint',
        'seo': _get_seo('bodypaint'),
    }
    return render(request, 'bodypaint.html', context)


def glitterbar(request):
    """Servicio: Glitter Bar."""
    context = {
        'active_page': 'glitterbar',
        'seo': _get_seo('glitterbar'),
    }
    return render(request, 'glitterbar.html', context)


def talleres(request):
    """Servicio: Talleres y Cursos."""
    context = {
        'active_page': 'talleres',
        'seo': _get_seo('talleres'),
    }
    return render(request, 'talleres.html', context)
