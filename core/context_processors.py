from .models import ContactInfo, Page


def site_info(request):
    return {
        'contact': ContactInfo.get_solo(),
        'menu_pages': Page.objects.filter(show_in_menu=True),
    }