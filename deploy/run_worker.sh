nohup python nougat_worker.py \
 --name meta/nougat \
 --host 0.0.0.0 \
 --controller_address http://aiapi.ihep.ac.cn:42901 \
 --limit_model_concurrency 5 \
 --permissions "groups: all; users: luojianwen21@mails.ucas.ac.cn; owner: hepai@ihep.ac.cn" > worker.log & # 自行修改