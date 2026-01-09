

cd deploy

python3 nougat_worker.py \
    --name "hepai/hainougat" \
    --host 0.0.0.0 \
    --controller_address https://aiapi.ihep.ac.cn  \
    --limit_model_concurrency 10 \
    --permissions "groups: payg;users: luojianwen21@mails.ucas.ac.cn;owner: tangzh@ihep.ac.cn"