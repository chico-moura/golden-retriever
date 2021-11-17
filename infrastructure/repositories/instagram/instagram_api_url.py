from tokens import INSTAGRAM_ACCESS_TOKEN


class InstagramAPIURL:
    __BASE_URL: str = f'https://graph.instagram.com/v12.0/me'
    __ACCESS_TOKEN: str = f'&access_token={INSTAGRAM_ACCESS_TOKEN}'

    @classmethod
    def medias(cls):
        return f'{cls.__BASE_URL}/media?fields=timestamp,media_type{cls.__ACCESS_TOKEN}'
