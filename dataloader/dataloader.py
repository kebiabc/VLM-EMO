from torchvision import datasets, transforms
import torch
from torch.utils.data import DataLoader, Dataset
from PIL import Image, ImageDraw
import os
import utils.util as ut 
import numpy as np
from torch.utils.data import DataLoader
from torch.utils.data.dataloader import default_collate
from torch.utils.data.sampler import SubsetRandomSampler


# def collate_fn(batch):
#     batch = list(filter(lambda x: x is not None, batch))
#     return torch.utils.data.dataloader.default_collate(batch)

# class BaseDataLoader(DataLoader):
#     """
#     Base class for all data loaders
#     """
#     def __init__(self, dataset, batch_size, shuffle, validation_split, num_workers, collate_fn=default_collate):
#         self.validation_split = validation_split
#         self.shuffle = shuffle

#         self.batch_idx = 0
#         self.n_samples = len(dataset)

#         self.sampler, self.valid_sampler = self._split_sampler(self.validation_split)

#         self.init_kwargs = {
#             'dataset': dataset,
#             'batch_size': batch_size,
#             'shuffle': self.shuffle,
#             'collate_fn': collate_fn,
#             'num_workers': num_workers
#         }
#         super().__init__(sampler=self.sampler, **self.init_kwargs)

#     def _split_sampler(self, split):
#         if split == 0.0:
#             return None, None

#         idx_full = np.arange(self.n_samples)

#         np.random.seed(0)
#         np.random.shuffle(idx_full)

#         if isinstance(split, int):
#             assert split > 0
#             assert split < self.n_samples, "validation set size is configured to be larger than entire dataset."
#             len_valid = split
#         else:
#             len_valid = int(self.n_samples * split)

#         valid_idx = idx_full[0:len_valid]
#         train_idx = np.delete(idx_full, np.arange(0, len_valid))

#         train_sampler = SubsetRandomSampler(train_idx)
#         valid_sampler = SubsetRandomSampler(valid_idx)

#         # turn off shuffle option which is mutually exclusive with sampler
#         self.shuffle = False
#         self.n_samples = len(train_idx)

#         return train_sampler, valid_sampler

#     def split_validation(self):
#         if self.valid_sampler is None:
#             return None
#         else:
#             return DataLoader(sampler=self.valid_sampler, **self.init_kwargs)


class MyDataset(Dataset):
    def __init__(self, root, input_file, transform=None):
        self.root = root 
        self.transform = transform
        self.data = self.read_input_file(input_file)

    def read_input_file(self, file):
        return [line.rstrip('\n') for line in open(file)]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        if idx >= len(self.data):
            raise IndexError('Index out of bound')
        sample = self.data[idx].split(',')
        path, label, x1, y1, x2, y2 = os.path.join(self.root, sample[0]), int(sample[1]), int(sample[2]), int(sample[3]), int(sample[4]), int(sample[5])
        im = Image.open(path)

        # extract facial and context regions
        face = im.crop((x1, y1, x2, y2))
        # draw = ImageDraw.Draw(im)
        # draw.rectangle((x1, y1, x2, y2), fill=(0, 0, 0))
        data = {
            'face': face,
            'context': im
        }
        
        # transform data 
        try:
            if self.transform is not None:
                face = self.transform(face)
        except:
            return None
        im = self.transform(im)
        # return face, label
        return im, label

# class CAERSDataLoader(BaseDataLoader):
#     def __init__(self, root, detect_file, train=True, batch_size=32, shuffle=True, num_workers=2):
#         """
#         Create dataloader from directory
#         Args:
#             - root (str): root directory
#             - detect_file (str): file containing results from detector 
#         """
        
#         data_transforms = ut.get_transform(train)
#         self.dataset = MyDataset(root, detect_file, data_transforms)
#         super().__init__(self.dataset, batch_size, shuffle, validation_split=0.0, num_workers=num_workers, collate_fn=collate_fn)
