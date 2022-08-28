from resources.admin_approver import AdminPromotionResource, AdminDemotionResource
from resources.authentication import RegisterResource, LoginResource, ModeratorRegisterResource, ModeratorLoginResource, \
    AdminLoginResource
from resources.videos import VideosResource, ExactVideoResource
from resources.workouts import WorkoutResource, ExactWorkoutResource

routes = (
    (RegisterResource, "/register/"),
    (LoginResource, "/login/"),
    (ModeratorRegisterResource, "/register/moderator/"),
    (ModeratorLoginResource, "/login/moderator/"),
    (AdminLoginResource, "/login/admin/"),
    (AdminPromotionResource, "/admin/promote/"),
    (AdminDemotionResource, "/admin/demote/"),
    (VideosResource, "/videos/"),
    (ExactVideoResource, "/videos/<int:id>/"),
    (WorkoutResource, "/workout/"),
    (ExactWorkoutResource, "/workout/<int:id>/"),


)