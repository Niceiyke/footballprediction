import os
import dill

def save_obj(file_path,obj):

    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb')as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        print(e)


def load_obj(file_path):

    try:
        with open(file_path,'rb')as file_obj:
            print('loaded')
            return dill.load(file_obj)

    except Exception as e:
        print(e)