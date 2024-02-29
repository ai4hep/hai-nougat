python nougat_worker.py \
 --name meta/nougat \  # Set the name of the worker to meta/nougat
 --host 0.0.0.0 \  # Set the host address of the worker to 0.0.0.0
 --controller_address http://aiapi.ihep.ac.cn:42901 \  # Set the controller address to http://aiapi.ihep.ac.cn:42901
 --limit_model_concurrency 5 \  # Set the model concurrency limit to 5
 --permissions "groups: all"  # Set permissions to "groups: all"