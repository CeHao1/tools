import os
import torch
import importlib
import datetime
import numpy as np
import random
from shutil import copy

from src.utils.py_utils import AttrDict, ParamDict
from src.utils.mpi_utils import update_with_mpi_config
from src.utils.checkpoint_utils import save_cmd, save_git
from src.utils.wandb import WandBLogger
from src.args.param import parse_args

WANDB_PROJECT_NAME = 'project_name'
WANDB_ENTITY_NAME = 'entity_name'

class Main:
    def __init__(self, args):
        self.args = args # args
        self.setup_device() # set up device

        # set up params
        self.conf = conf = self.get_config() # get config
        update_with_mpi_config(self.conf) # update with mpi config  

        self._hp = self._default_hparams() # default hparams
        self._hp.overwrite(self.conf.general) # overwrite with the config file
        self._hp.exp_path = make_path(self.conf.exp_dir, args.path, args.prefix, args.new_dir)
        self.log_dir = log_dir = os.path.join(self._hp.exp_path, 'events')

        # set seeds, display, worker shutdown
        if args.seed != -1: self._hp.seed = args.seed   # override from command line if set
        set_seeds(self._hp.seed)

        # set up logging
        if self.is_chef:
            print("Running base worker.")
            self.logger = self.setup_logging(self.conf, self.log_dir)
        else:
            print("Running worker {}, disabled logging.".format(self.conf.mpi.rank))
            self.logger = None

        # other setups
        # 1. build environment

        # 2. build agent

        # 3. build sampler

        # resume
        if args.resume or self.conf.ckpt_path is not None:
            start_epoch = self.resume(args.resume, self.conf.ckpt_path)
            self._hp.n_warmup_steps = 0     # no warmup if we reload from checkpoint!

    def _default_hparams(self):
        # default hparams
        default_dict = ParamDict({
            'seed': None, # example
            'agent': None,
        })
        return default_dict

    def get_config(self):
        conf = AttrDict()

        # paths
        conf.exp_dir = self.get_exp_dir()
        conf.conf_path = os.path.join(conf.exp_dir, self.args.path)

        # general and model configs
        print('loading from the config file {}'.format(conf.conf_path))
        conf_module = importlib.import_module(self.args.path)
        conf.general = conf_module.configuration
        
        # read more configs

        return conf

    def setup_logging(self, conf, log_dir):
        if not self.args.dont_save:
            print('Writing to the experiment directory: {}'.format(self._hp.exp_path))
            if not os.path.exists(self._hp.exp_path):
                os.makedirs(self._hp.exp_path)
            save_cmd(self._hp.exp_path)
            save_git(self._hp.exp_path)
            save_config(conf.conf_path, os.path.join(self._hp.exp_path, "conf_" + datetime_str() + ".py"))

            # setup logger
            exp_name = f"{os.path.basename(self.args.path)}_{self.args.prefix}" if self.args.prefix \
                else os.path.basename(self.args.path)
            logger = WandBLogger(exp_name, WANDB_PROJECT_NAME, entity=WANDB_ENTITY_NAME,
                                    path=self._hp.exp_path, conf=conf) 
            return logger

    def setup_device(self):
        # set up device
        self.use_cuda = torch.cuda.is_available() 
        self.device = torch.device('cuda') if self.use_cuda else torch.device('cpu')
        if self.args.gpu != -1:
            os.environ["CUDA_VISIBLE_DEVICES"] = str(self.args.gpu)

    def get_exp_dir(self):
        return os.environ['EXP_DIR']


# ==================== utils ====================
def datetime_str():
    return datetime.datetime.now().strftime("_%Y-%m-%d_%H-%M-%S")

def make_path(exp_dir, conf_path, prefix, make_new_dir):
    # extract the subfolder structure from config path
    path = conf_path.split('configs/', 1)[1]
    if make_new_dir:
        prefix += datetime_str()
    base_path = os.path.join(exp_dir, path)
    return os.path.join(base_path, prefix) if prefix else base_path

def save_config(conf_path, exp_conf_path):
    copy(conf_path, exp_conf_path)

def set_seeds(seed=0, cuda_deterministic=True):
    """Sets all seeds and disables non-determinism in cuDNN backend."""
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)

    if torch.cuda.is_available() and cuda_deterministic:
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True

# ==================== main ====================
if __name__ == "__main__":
    # parse args
    Main(args=parse_args())
    