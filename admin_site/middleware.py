from django.shortcuts import redirect

def login_required(view_func):
    """
        Decorador para verificar si se inicio sesion
        En el caso de no haber iniciado sesion se envia al sistema de logueo
    """
    def wrapper(request, *args, **kwargs):
        # Comprobar si el usuario esta en sesión
        if 'user_id' not in request.session:
            # Si no se encuentra en sesion se redirecciona al sistema de logueo
            return redirect('login')
        # Si se encuentra en sesion se permite el ingreso a la vista
        return view_func(request, *args, **kwargs)
    return wrapper

def rol_required(required_roles):
    """
        Decorador para verificar el rol del usuario
        Se usa para validar entre el usuario normal y el administrador
    """
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            # Se obtiene el rol del usuario
            user_rol = request.session.get('user_rol')
            # Se comprueba si el rol del usuario esta permitido
            if user_rol not in required_roles:
                # Si no lo esta se redirecciona al apartado de un usuario habitual
                return redirect('home')
            # si esta autorizado entonces se envia al home del administrador
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator