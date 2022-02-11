# creating case insensivies
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend #UserModel

class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()   #(this is going to get the usermodels from the settings.py line 138)
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)  #THE USERNAME_FIELD IS THE USERNAME CHANGED TO THE EMAIL IN MODELS.PY LINE 60
        
        try:
            case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
            user = UserModel._default_manager.get(**{case_insensitive_username_field: username})
            
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            
            
# go to the settings and apply it there for it to work (settings.py line 193)