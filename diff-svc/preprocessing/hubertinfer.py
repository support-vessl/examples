import os.path
from io import BytesIO
from pathlib import Path

import numpy as np
import torch
from network.hubert.hubert_model import get_units, hubert_soft
from network.hubert.vec_model import get_vec_units
from utils.hparams import hparams


class Hubertencoder:
    def __init__(self, pt_path="checkpoints/hubert/hubert_soft.pt"):
        if not "use_vec" in hparams.keys():
            hparams["use_vec"] = False

        pt_path = list(Path(pt_path).parent.rglob("*.pt"))[0]
        if "hubert_gpu" in hparams.keys():
            self.use_gpu = hparams["hubert_gpu"]
        else:
            self.use_gpu = True
        self.dev = torch.device("cuda" if self.use_gpu and torch.cuda.is_available() else "cpu")
        self.hbt_model = hubert_soft(str(pt_path)).to(self.dev)

    def encode(self, wav_path):
        if isinstance(wav_path, BytesIO):
            npy_path = ""
            wav_path.seek(0)
        else:
            npy_path = Path(wav_path).with_suffix(".npy")
        if os.path.exists(npy_path):
            units = np.load(str(npy_path))
        elif hparams["use_vec"]:
            units = get_vec_units(self.hbt_model, wav_path, self.dev).cpu().numpy()[0]
        else:
            units = get_units(self.hbt_model, wav_path, self.dev).cpu().numpy()[0]
        return units  # [T,256]
