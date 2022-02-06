import torch
import cv2
import os
import glob
from torch.utils.data import Dataset
import random

class Sentinel_Loader(Dataset):
	
  def __init__(self, data_path):
		"""
		Initialize the data producer
		"""
    self.data_path = data_path
    self.imgs_path = glob.glob(os.path.join(data_path, 'S1Hand/*.tif'))
    self.label_path = glob.glob(os.path.join(data_path, 'HandLabel/*.tif'))

	def __len__(self):
		return self._num_image
		
  def __getitem__(self, index):
    image = cv2.imread(image_path)
    label = cv2.imread(label_path)
    return image, label
	
if __name__ == "__main__":
  sentinel_dataset = Sentinel_Loader("/content/drive/My Drive/c2s_data/v1.1/data/flood_events/HandLabeled/")
  print("Dataset_count", len(sentinel_dataset))
  train_loader = torch.utils.data.DataLoader(dataset=sentinel_dataset,
                                               batch_size=2, 
                                               shuffle=True)
  for image, label in train_loader:
    print(image.shape)
