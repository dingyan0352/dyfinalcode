CUDA_VISIBLE_DEVICES=$1 python src/self_distill.py \
#	--model_name_or_path "princeton-nlp/unsup-simcse-roberta-base" \
	--model_name_or_path "home/qii/dy/RankEncoder-main/code/SimCSE_RankEncoder/SentEval/outputs/simcse/checkpoints/simcse_unsup_rank_encoder_seed_61507" \
 	--batch_size_bi_encoder 128 \
	--batch_size_cross_encoder 32 \
	--num_epochs_bi_encoder 10 \
	--num_epochs_cross_encoder 1 \
	--cycle 3 \
	--bi_encoder_pooling_mode cls \
	--init_with_new_models \
	--task sts_sickr \
	--random_seed 2021