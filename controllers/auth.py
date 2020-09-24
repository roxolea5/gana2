from passlib.hash import pbkdf2_sha256

from models.usuarios import Usuario as User


class AuthController:

    @staticmethod
    def verify_user_for_jwt(username, password):
        user = User.query.filter_by(username=username).first()
        pw = User.query.filter_by(password=password).first()
        if user and pw:  # and pbkdf2_sha256.verify(password, user.password):
            return user
        return None
