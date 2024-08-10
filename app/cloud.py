import aiohttp
from app.config import CLOUD_API_URL, CLOUD_API_KEY

# Определяем функцию для загрузки файла в облако
async def upload_to_cloud(file_path: str):
    """
        Загружаем файл в облако.

        Аргументы:
            file_path (str): Путь к файлу.
        """
    # Создаём клиентскую сессию HTTP
    async with aiohttp.ClientSession() as session:
        with open(file_path, 'rb') as file:
            files = {'file': file}
            headers = {'Authorization': f'Bearer {CLOUD_API_KEY}'}
            async with session.post(CLOUD_API_URL, data=files, headers=headers) as response:
                if response.status != 200:
                    raise Exception("Failed to upload to cloud")
