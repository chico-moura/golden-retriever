from domain.value_objects import UserAccount


class InstagramAPIURL:
    __BASE_URL: str = f'https://graph.instagram.com/v12.0/me'

    @classmethod
    def medias(cls, user_account: UserAccount) -> str:
        access_token = cls.__format_access_token(user_account.token)
        return f'{cls.__BASE_URL}/media?fields=timestamp,media_type{access_token}'

    @staticmethod
    def __format_access_token(token: str) -> str:
        return f'&access_token={token}'
