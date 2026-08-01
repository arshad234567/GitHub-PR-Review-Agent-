from typing import List

class RAGService:

    def __init__(self, retriever):
        self.retriever = retriever

    def retrieve_context(
        self,
        pull_request,
        top_k: int = 5,
    ) -> List[dict]:

        contexts = []

        for file in pull_request.changed_files:
            file_context = self.retriever.retrieve(
                file_path=file.filename,
                query=file.patch,
                top_k=top_k,
            )

            contexts.extend(file_context)

        return contexts