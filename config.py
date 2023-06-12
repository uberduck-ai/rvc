import json

def get_hparams_from_file(config_path):
    with open(config_path, "r") as f:
        data = f.read()
    config = json.loads(data)

    hparams = HParams(**config)
    return hparams


class HParams:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if type(v) == dict:
                v = HParams(**v)
            self[k] = v

    def keys(self):
        return self.__dict__.keys()

    def items(self):
        return self.__dict__.items()

    def values(self):
        return self.__dict__.values()

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __contains__(self, key):
        return key in self.__dict__

    def __repr__(self):
        return self.__dict__.__repr__()

RVC_DEFAULTS = {
    "max_wav_value": 32768.0,
    "sampling_rate": 40000,
    "filter_length": 2048,
    "hop_length": 400,
    "win_length": 2048,
    "n_mel_channels": 125,
    "mel_fmin": 0.0,
    "mel_fmax": None,
}

RVC_TRAIN_DEFAULTS = {
    "log_interval": 200,
    "seed": 1234,
    "epochs": 20000,
    "learning_rate": 1e-4,
    "betas": [0.8, 0.99],
    "eps": 1e-9,
    "batch_size": 4,
    "fp16_run": False,
    "lr_decay": 0.999875,
    "segment_size": 12800,
    "init_lr_ratio": 1,
    "warmup_epochs": 0,
    "c_mel": 45,
    "c_kl": 1.0,
    "steps_per_sample": 100,
    "iters_per_checkpoint": 100,
    "output_directory": "/tmp",
}
