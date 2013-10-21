from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('dashboard')

def my_view(request):
    return {'project':'dashboard'}
