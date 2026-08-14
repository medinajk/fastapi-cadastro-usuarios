from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler
from src.controllers.interfaces.user_finder import UserFinderInterface

class UserFinderView:
    def __init__(self, controller: UserFinderInterface) -> None:
        self.__controller = controller

    async def handle_find_user_by_name(self, http_request: HttpRequest) -> HttpResponse:
        try:
            user_name = http_request.path_params["user_name"]
            response = await self.__controller.find_user_by_name(user_name)
            return HttpResponse(body = response, status_code = 200)
        except Exception as exception:
            error_handler(exception)