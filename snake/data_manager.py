import json
from multiprocessing import set_forkserver_preload


class data_manager:
    
    def load(self,path):
        file = open(path)
        data = json.load(file)
        return data
    
    def update(self,path,value,index):
        file_content = self.load(path)
        file = open(path,'w')
        file_content[index] = value
        json.dump(file_content,file)

    def update_s(self,path,value,index,index_sec):
        file_content = self.load(path)
        file = open(path,'w')
        file_content[index][index_sec] = value
        json.dump(file_content,file)
    
    def update_ss(self,path,value,index,index_sec,index_th):
        file_content = self.load(path)
        file = open(path,'w')
        file_content[index][index_sec][index_th] = value
        json.dump(file_content,file)

    def append_tuple(self,path,data,index):
        file_content = self.load(path)
        file = open(path,'w')
        file_content[index] += data

        json.dump(file_content,file)
        

    