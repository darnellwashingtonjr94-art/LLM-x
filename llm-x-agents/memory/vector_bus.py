class VectorMemoryBus:
    def __init__(self):
        self.store = []

    def query_embeddings(self, semantic_query: str) -> list:
        print(f"[Vector Bus] Pruning context window for query: {semantic_query}")
        return self.store[:5]
