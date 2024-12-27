# Semantic-guided Artwork Clustering
My thesis project on **clustering of deep semantic embeddings** of artworks from the *ArtGraph* dataset. The semantic embeddings are obtained from the **CLIP** image and text encoders, i.e. the vision and text Transformers, specifically finetuned for the purpose using data from *ArtGraph*.

The clusters found are then automatically interpreted and described in terms of genre, topic, media and style. These interpretations (associated to each cluster) are eventually used to *generate captions for new paintings* never seen by the model.
