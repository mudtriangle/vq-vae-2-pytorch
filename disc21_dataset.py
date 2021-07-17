from torchvision.datasets.folder import *
import os
from typing import Any, Callable, cast, Dict, List, Optional, Tuple


class DISC21(DatasetFolder):
    def __init__(
            self,
            root: str,
            transform: Optional[Callable] = None,
            target_transform: Optional[Callable] = None,
            loader: Callable[[str], Any] = default_loader,
            is_valid_file: Optional[Callable[[str], bool]] = None,
    ):
        super(DISC21, self).__init__(root, loader, IMG_EXTENSIONS if is_valid_file is None else None,
                                     transform=transform,
                                     target_transform=target_transform,
                                     is_valid_file=is_valid_file)
        self.imgs = self.samples

    def find_classes(self, directory: str):
        if not os.path.isdir(directory):
            raise FileNotFoundError(f'{directory} is not a valid directory.')

        return '', {'': 0}
