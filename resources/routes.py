
from resources.authentication import RegisterResource, LoginResource
from resources.videos import VideosResource, ExactVideoResource

routes = (
    (RegisterResource, "/register/"),
    (LoginResource, "/login/"),
    (VideosResource, "/videos/"),
    (ExactVideoResource, "/videos/<int:id>/"),

    #(ModeratorLoginResource, "/login/moderator/"),
    #(AdminLoginResource, "/login/admin/")
)