import dataclasses

import torch


@dataclasses.dataclass
class BaseConfig:
    seed: int = 1
    gpu_id: int = 0
    verb: bool = False


def _main(cfg: BaseConfig):
    # actual main function
    pass


def main(cfg: BaseConfig):
    if cfg.verb:
        print(cfg)
    torch.cuda.set_device(cfg.gpu_id)
    with homura.set_seed(cfg.seed):
        _main(cfg)


if __name__ == "__main__":
    main()
