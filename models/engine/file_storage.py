#!/usr/bin/python3
'''Module contains 'FileStorage' class definition.
'''
import json


class FileStorage:
    '''class FileStorage.
    Handles persitence for the application by saving objects to the file
    'file.json'
    '''
    __file_path = 'file.json'
    __objects = {}

     
    def all(self):
        '''Returns the contents of the '__objects' dictionary
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''Adds the object 'obj' to the collection of objects in the
        '__objects' dictionary.
        '''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        '''Saves the contents of the '__objects' dictionary to the json file
        specified in the '__file_path' class attribute.
        '''
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fp:
            json.dump(FileStorage.__objects, fp)

    def reload(self):
        '''Sets the '__objects' dictionary with the collection of objects
        retrieved for the file.json file.
        '''
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as fp:
                FileStorage.__objects = json.load(fp)
        except NameError:
            pass
        except IOError:
            pass
