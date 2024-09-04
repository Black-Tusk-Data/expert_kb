import json
from pathlib import Path
import struct

from expert_kb.sqlite_db import SQLiteDB


def serialize(vector: list[float]) -> bytes:
    """serializes a list of floats into a compact "raw bytes" format"""
    return struct.pack("%sf" % len(vector), *vector)


class KnowledgeBase:
    def __init__(
            self,
            *,
            path: str,
            embedding_size: int,
    ):
        self.embedding_size = embedding_size
        self.db = SQLiteDB(
            Path(path),
            vector_length=self.embedding_size,
        )
        self.max_embedding_id = self._get_max_embedding_id()
        return

    def _get_max_embedding_id(self) -> int:
        max_row_id = self.db.query("""
        select max(rowid) rowid from embedding
        """)[0]["rowid"]
        if not max_row_id:
            return 0
        return max_row_id

    def add_fragment(
            self,
            *,
            fragment_id: str,
            text: str,
            embedding: list[float],
            metadata: dict | None = None,
    ) -> int:
        metadata = metadata or {}
        next_embedding_id = self.max_embedding_id + 1
        with self.db.cursor() as cur:
            cur.execute("""
            INSERT INTO embedding(
              rowid, embedding
            )
            VALUES (
              :embedding_id, :embedding
            )
            """, {
                "embedding_id": next_embedding_id,
                "embedding": serialize(embedding),
            })
            cur.execute(f"""
            INSERT INTO embedded_fragment(
              fragment_id,
              embedding_id,
              text,
              metadata_json
            ) VALUES (
              :fragment_id,
              :embedding_id,
              :text,
              :metadata_json
            )
            """, {
                "fragment_id": fragment_id,
                "text": text,
                "embedding_id": next_embedding_id,
                "metadata_json": json.dumps(metadata),
            })
            self.max_embedding_id = next_embedding_id
            return next_embedding_id

    pass
