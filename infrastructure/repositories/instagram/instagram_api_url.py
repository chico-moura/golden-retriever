from domain.value_objects import UserAccount


# FIXME: InstagramAPIClient (put requests inside here and make a method .get)
# FIXME: maybe user account is a dependency?
class InstagramAPIURL:
    __BASE_URL: str = f'https://graph.instagram.com/v12.0/me'

    @classmethod
    def medias(cls, user_account: UserAccount) -> str:
        access_token = cls.__format_access_token(user_account.token)
        return f'{cls.__BASE_URL}/media?fields=timestamp,media_type{access_token}'

    @staticmethod
    def __format_access_token(token: str) -> str:
        return f'&access_token={token}'

    def __init__(self, url):
        self.__BASE_URL = url
