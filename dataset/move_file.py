from shutil import copyfile
from glob import glob
from tqdm import tqdm
import os

def movefiles(filepath, movepath):
    copyfile(filepath, movepath)

train_paths = glob(os.path.join('dataset', 'train','*','images','*.jpg'))

train_rename = ['dataset/train_all/'+train_path.split('\\')[-1] for train_path in train_paths]

for i in tqdm(range(len(train_paths))):
    copyfile(train_paths[i], train_rename[i])



    