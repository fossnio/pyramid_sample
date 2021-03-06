from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    from pyramid.settings import asbool

    # auth settings
    if asbool(settings['auth_mode']):
        from pyramid.security import Allow, Deny, Everyone, Authenticated, DENY_ALL, ALL_PERMISSIONS
        from pyramid.authentication import AuthTktAuthenticationPolicy
        from pyramid.authorization import ACLAuthorizationPolicy

        def get_user(request):
            from pyramid.security import unauthenticated_userid
            return unauthenticated_userid(request)

        def group_finder(userid, request):
            if userid == 'foo':
                return ['group:users']

        class RootFactory:
            __acl__ = [
                (Allow, 'bar', 'WHAT_EVER_YOU_LIKE'),
                (Allow, 'group:users', 'WHAT_EVER_YOU_LIKE'),
                (Allow, 'admin', ALL_PERMISSIONS),
                DENY_ALL
            ]

            def __init__(self, request):
                pass

        authn_policy = AuthTktAuthenticationPolicy(settings['secret_key'],
                                                   timeout=86400, # cookie will expire after 1 day
                                                   callback=group_finder)
        authz_policy = ACLAuthorizationPolicy()

        config = Configurator(settings=settings,
                              root_factory=RootFactory,
                              authentication_policy=authn_policy,
                              authorization_policy=authz_policy)

        config.add_request_method(get_user, 'user', reify=True)
    else:
        config = Configurator(settings=settings)

    # using jinja2 as default template engine
    config.include('pyramid_jinja2')

    # session settings
    if asbool(settings['production_mode']):
        # using pyramid_redis_sessions
        config.include('pyramid_redis_sessions')
    else:
        # using builtin session mechanism
        from pyramid.session import SignedCookieSessionFactory
        config.set_session_factory(SignedCookieSessionFactory(settings['secret_key']))

    # transaction manager settings, used by pyramid_sqlalchemy and
    # pyramid_mailer
    #config.include('pyramid_tm')

    # database settings
    #config.include('pyramid_sqlalchemy')

    # mailer settings
    #config.include('pyramid_mailer')

    # i18n settings
    #config.add_translation_dirs('pyramid_sample:locale')

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    #config.add_route('login', '/login')
    #config.add_route('logout', '/logout')

    config.scan()
    return config.make_wsgi_app()
