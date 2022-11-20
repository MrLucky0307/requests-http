import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = file_path.split('/')[-1]
        headers = {"Authorization": f"OAuth {self.token}"}
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                                params={"path": file_name},headers=headers)
        href = response.json()["href"]
        with open(file_path, "r") as f:
            upload_response = requests.put(href, files={"file": f})
            upload_response.raise_for_status()
        return 


if __name__ == '__main__':
    # path_to_file = "Путь до файла на компьютере"
    # token = "Ваш токен Яндекс.Диска"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
