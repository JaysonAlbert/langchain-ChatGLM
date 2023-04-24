import torch.cuda
import torch.backends


embedding_model_dict = {
    "ernie-tiny": "nghuyong/ernie-3.0-nano-zh",
    "ernie-base": "nghuyong/ernie-3.0-base-zh",
    "text2vec": "GanymedeNil/text2vec-large-chinese",
}

# Embedding model name
EMBEDDING_MODEL = "text2vec"

# Embedding running device
EMBEDDING_DEVICE = "cpu"

# supported LLM models
llm_model_dict = {
    "chatglm-6b-int4-qe": "THUDM/chatglm-6b-int4-qe",
    "chatglm-6b-int4": "THUDM/chatglm-6b-int4",
    "chatglm-6b": "/data/disk1/.cache/huggingface/hub/models--THUDM--chatglm-6b/snapshots/f83182484538e663a03d3f73647f10f89878f438",
}

# LLM model name
LLM_MODEL = "chatglm-6b"

# Use p-tuning-v2 PrefixEncoder
USE_PTUNING_V2 = False

# LLM running device
LLM_DEVICE = "cuda"

VS_ROOT_PATH = "./vector_store/"

UPLOAD_ROOT_PATH = "./content/"
