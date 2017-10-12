"""Provides SQuAD data for training and dev.
"""

import numpy as np
import os
import pickle
import preprocessing.constants as constants

from datasets.dataset import Dataset
from datasets.file_util import *
from datasets.squad_data_base import SquadDataBase
from preprocessing.vocab_util import get_vocab

class SquadData(SquadDataBase):
    def __init__(self, options):
        data_dir = options.data_dir
        self.data_dir = data_dir
        self.vocab = get_vocab(data_dir)
        self.train_ds = Dataset(
            load_text_file(data_dir, constants.TRAIN_FULL_TEXT_TOKENS_FILE),
            load_file(data_dir, constants.TRAIN_CONTEXT_FILE),
            load_file(data_dir, constants.TRAIN_QUESTION_FILE),
            load_file(data_dir, constants.TRAIN_SPAN_FILE),
            options,
            load_file(data_dir, constants.TRAIN_WORD_IN_QUESTION_FILE),
            load_file(data_dir, constants.TRAIN_WORD_IN_CONTEXT_FILE))
        self.dev_ds = Dataset(
            load_text_file(data_dir, constants.DEV_FULL_TEXT_TOKENS_FILE),
            load_file(data_dir, constants.DEV_CONTEXT_FILE),
            load_file(data_dir, constants.DEV_QUESTION_FILE),
            load_file(data_dir, constants.DEV_SPAN_FILE),
            options,
            load_file(data_dir, constants.DEV_WORD_IN_QUESTION_FILE),
            load_file(data_dir, constants.DEV_WORD_IN_CONTEXT_FILE))
        self.embeddings = np.load(os.path.join(data_dir,
                    constants.EMBEDDING_FILE))
        self.word_vec_size = constants.WORD_VEC_DIM