import json
import pandas as pd

class Transform:
    """
    Transform is a class to transform data from Dukcapil API to be sent to SPPTTI or DPO API

    Attributes:
    -----------
    dukcapil_data : dict
        Data from Dukcapil API
    
    Methods:
    --------
    transform_data() -> dict
        Transform data from Dukcapil API to be sent to SPPTTI or DPO API
        
    """
    def __init__(self, dukcapil_data):
        self.dukcapil_data = dukcapil_data

    def transform_data(self):
        return {
            'jenis_identitas': 'KTP',
            'nomor_identitas': self.dukcapil_data['nik'],
            'nama_lengkap': self.dukcapil_data['nama'],
            'tanggal_lahir': self.dukcapil_data['tanggal_lahir'],
            'tempat_lahir': self.dukcapil_data['tempat_lahir'],
            'jenis_kelamin': self.dukcapil_data['jenis_kelamin'],
            'alamat': self.dukcapil_data['alamat'],
            'rt': self.dukcapil_data['rt'],
            'rw': self.dukcapil_data['rw'],
            'kelurahan': self.dukcapil_data['kelurahan'],
            'kecamatan': self.dukcapil_data['kecamatan'],
            'kabupaten_kota': self.dukcapil_data['kota'],
            'provinsi': self.dukcapil_data['provinsi'],
            'agama': self.dukcapil_data['agama'],
            'pekerjaan': self.dukcapil_data['pekerjaan'],
            'kewarganegaraan': self.dukcapil_data['kewarganegaraan'],
            'is_validate': True
        }