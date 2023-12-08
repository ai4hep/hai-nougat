python nougat_worker.py \
 --name meta/nougat \
 --host 0.0.0.0 \
 --controller_address http://aiapi.ihep.ac.cn:42901 \
 --limit_model_concurrency 10 \
 --permissions "groups: all; owner: hepai@ihep.ac.cn"  # 自行修改