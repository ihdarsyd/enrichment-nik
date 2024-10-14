import os
import requests


class DukcapilPerson:
    """
    DukcapilPerson is a class to get data from Dukcapil API

    Attributes:
    -----------
    dukcapil_url : str
        Dukcapil API URL
    
    Methods:
    --------
    _request(path : str) -> requests
        Send request to Dukcapil API
    search_nik(nik : str) -> requests
        Get data from Dukcapil API by NIK
    """
    def __init__(self,):
        self.dukcapil_url = os.getenv('DUKCAPIL_URL')

    def _request(
            self,
            path : str
        ) -> requests:
        response = requests.get(path)
        return response.json()
    
    def search_nik(self, nik):
        path = '/api/data?nik=' + nik
        return self._request(path = self.dukcapil_url + path)