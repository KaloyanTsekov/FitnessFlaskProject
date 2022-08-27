from resources.authentication import RegisterResource
from resources.videos import VideosResource

routes = (
    (RegisterResource, "/register/"),
    (VideosResource, "/videos/")
)