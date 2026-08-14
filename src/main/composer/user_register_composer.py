from src.models.repositories.users_repository import UsersRepository
from src.controllers.user_register import UserRegister
from src.views.user_register_view import UserRegisterView

def user_register_composer():
    model = UsersRepository()
    controller = UserRegister(model)
    view = UserRegisterView(controller)
    return view