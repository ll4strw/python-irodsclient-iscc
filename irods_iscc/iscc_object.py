import irods.client_configuration as config
config.data_objects.auto_close = True

import iscc_core as ic
import iscc_schema as iss
import magic

class IsccObj:
    def __init__(self, DataObject):
        self._data_obj = DataObject 
        self.core = None
        self._mime = None
        self.meta = None
        
    def __repr__(self):
        return "<{} {} {} {}>".format(
            self.__class__.__name__,
            self.__make_iscc(),
            self._data_obj.__class__.__name__,
            self._data_obj.id
        )

    def __make_iscc(self,data_obj=None,other=None):

        # if no other DataObject is passed,
        # use own DataObject
        if not data_obj:
            data_obj = self._data_obj
        
        with data_obj.open('r') as fp:
            header=fp.read(4096)
            self._mime=magic.from_buffer(header, mime=True)
            fp.seek(0)
            data_code = ic.gen_data_code(fp)
            fp.seek(0)
            instance_code = ic.gen_instance_code(fp)

        meta={avu.name: avu.value for avu in data_obj.metadata.items()}
        meta_code = ic.gen_meta_code(name=data_obj.name,
                                     description="ID: {}, OWNER: {}".format(data_obj.id,data_obj.owner_name),
                                     meta=meta)

        # combine ISCC units
        iscc_code = ic.gen_iscc_code(
            (meta_code["iscc"],
             data_code["iscc"],
             instance_code["iscc"])
        )
        
        iscc = ic.Code(iscc_code["iscc"])

        # iscc meta from schema
        isccmeta = {
            "filename": data_obj.name,
            "mediatype": self._mime,
        }
        
        isccmeta.update(data_code)
        isccmeta.update(instance_code)
        isccmeta.update(meta_code)
        isccmeta.update(iscc_code)

        self.meta=iss.IsccMeta.construct(**isccmeta)

        
        # set property only for own DataObject
        if not other:
            self.core = iscc
        
        return iscc

    
    def compare(self,other_data_obj):
        if not self.core:
            self.core = self.__make_iscc()
        iscc_other=self.__make_iscc(data_obj=other_data_obj,other="yes")
        sim=ic.iscc_compare(self.core.code, iscc_other.code)
        return sim 
    
    def decompose(self):
        if not self.core:
            self.core = self.__make_iscc()
        comp=[ic.Code(unit) for unit in ic.iscc_decompose(self.core.code)]
        return comp
