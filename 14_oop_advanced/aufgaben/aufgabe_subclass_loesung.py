
class BaseService:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        method = getattr(cls, 'handle', None)
        if not callable(method):
            raise TypeError(
                f"{cls.__name__} muss 'handle(self, request)' definieren."
            )


class AuthService(BaseService):
    def handle(self, request):
        print("Authentifiziere Nutzer...")


class BrokenService(BaseService):
    """Produziert Fehler, da handle() fehlt..."""
    pass  # Kein 'handle' → TypeError beim Import


# Anwendung
service = AuthService()
service.handle("dummy-request")  # → OK
