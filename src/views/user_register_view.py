from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler
from src.controllers.interfaces.user_register import UserRegisterInterface

class UserRegisterView:
    def __init__(self, controller: UserRegisterInterface) -> None:
        self.__controller = controller

    async def handle_register_user(self, http_request: HttpRequest) -> HttpResponse:
        try:
            user_data = http_request.body
            response = await self.__controller.register_user(user_data)
            return HttpResponse(body = response, status_code = 201)
        except Exception as exception:
            error_handler(exception)