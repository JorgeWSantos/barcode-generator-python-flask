from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreateController


class TagCreatorView:
    '''
        responsability for interactive with http
    '''
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        print('body', body)
        product_code = body["product_code"]

        controller = TagCreateController()
        response = controller.create(product_code)

        return HttpResponse(status_code= 200, body=response)
