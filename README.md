# dyfinalcode
Unsupervised Contrastive Learning of Sentence Embeddings through Optimized Sample Construction and Knowledge Distillation

Unsupervised contrastive learning of sentence embedding has been a recent focus of researchers. However, issues such as unreasonable
division of positive and negative samples and poor data enhancementleading to text semantic changes still exist. We propose an optimized
data augmentation method that combines contrastive learning’s data augmentation with unsupervised sentence pair modelling’s distillation.
Our data augmentation uses in-sentence tokens for positive examples and text similarity for negative examples, while the distillation is conducted
without supervised pairs. Experimental results on the STS task show that our method achieves a Spearman correlation of 81.03%, outperforming
existing STS benchmarks.
