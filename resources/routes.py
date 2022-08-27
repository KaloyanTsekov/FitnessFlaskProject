from resources.authentication import RegisterResource, LoginResource
from resources.videos import VideosResource

routes = (
    (RegisterResource, "/register/"),
    (VideosResource, "/videos/"),
    (LoginResource, "/login/")
)