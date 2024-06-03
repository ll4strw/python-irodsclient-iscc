from irods.data_object import iRODSDataObject
from irods_iscc.iscc_object import IsccObj


class iRODSDataObjectISCC(iRODSDataObject):
    def __init__(self, irods_data_object):
        self.d = irods_data_object
        self.__dict__ = self.d.__dict__.copy()
        self._iscc = None
        
    @property
    def iscc(self):
        if not self._iscc:
            self._iscc = IsccObj(self)
        return self._iscc
    
