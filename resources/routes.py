from resources.authentication import RegisterResource, LoginResource
from resources.videos import VideosResource

routes = (
    (RegisterResource, "/register/"),
    #(VideosResource, "/videos/"),
    (VideosResource, "/videos/<int:id>/"),
    (LoginResource, "/login/"),
    #(ModeratorLoginResource, "/login/moderator/"),
    #(AdminLoginResource, "/login/admin/")
)