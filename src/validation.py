import json

class Validation:
    """ 
    Validation is a class to validate data before sending to Dukcapil API

    Attributes:
    -----------
    data : dict
        Data to be validated
    
    Methods:
    --------
    validate_nik_spptti() -> str
        Validate NIK from SPPTTI data
    validate_nik_dpo() -> str
        Validate NIK from DPO data
    validate_person() -> str
        Validate NIK from SPPTTI or DPO data to be sent to Dukcapil API

    """
    def __init__(self, data):
        # convert to json
        self.data = json.loads(data)

    def validate_nik_spptti(self):
        # validate nik format
        nik = self.data.get('national_id')

        # Check if the NIK has exactly 16 digits
        if len(nik) == 16:
            return nik
        
    def validate_nik_dpo(self):
        # validate nik format
        jenis_identitas = self.data.get('jenis_identitas')

        if jenis_identitas == 'KTP':
            nik = self.data.get('nomor_identitas')

            # Check if the NIK has exactly 16 digits
            if len(nik) == 16:
                return nik


    def validate_person(self):
        # check if data is not empty
        if self.data:
            if self.data.get('source') == 'spptti':
                self.nik = self.validate_nik_spptti()
                return self.nik
            elif self.data.get('source') == 'dpo':
                self.nik = self.validate_nik_dpo()
                return self.nik