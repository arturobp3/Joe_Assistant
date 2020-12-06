

def login_required(func):
    def wrapper(self, *args):
        if self.spotify_controller.login("arturobp"):
            return func(self, *args)
        else:
            return False, "Ejecuta Spotify en tu ordenador o inicia sesión primero"
    return wrapper