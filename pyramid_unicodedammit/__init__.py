import codecs

from bs4 import UnicodeDammit

from pyramid.tweens import INGRESS


def unicodedammit_tween_factory(handler, registry):

    def unicodedammit_tween(request):
        env = request.environ
        qs = env.get('QUERY_STRING', '')

        if qs:
            try:
                codecs.utf_8_decode(qs, 'strict', True)
            except UnicodeDecodeError:
                ud = UnicodeDammit(qs)
                env['QUERY_STRING'] = codecs.encode(ud.unicode_markup, 'utf-8')

        return handler(request)

    return unicodedammit_tween


def includeme(config):
    config.add_tween('pyramid_unicodedammit.unicodedammit_tween_factory',
                     under=INGRESS)
