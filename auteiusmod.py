import umap

# Initialize UMAP
umap_model = umap.UMAP(n_neighbors=15, n_components=2, metric='cosine')

# Reduce dimensionality
reduced_embeddings = umap_model.fit_transform(embeddings)
