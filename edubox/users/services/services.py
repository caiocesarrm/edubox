from django.contrib.auth import get_user_model
from edubox.users.serializers import CreateAuthUserSerializer

User = get_user_model()

class UserRegister():
    @classmethod
    def execute(cls, email, password, confirm_password):
        try:
           
            if password != confirm_password:
                return {"success": False, 'message':'Different passwords.'}

            if(User.objects.filter(email=email).exists()):
                return({"success": False, "message": f"Email {email} already registered."})
    
            auth_user = User(email=email, username=email, is_active=True)
            auth_user.set_password(password)
            auth_user.save()

            return {"success": True, 'message':'Registered sucessfully.'}
        except Exception as e:
            print(str(e))
            raise Exception
            
