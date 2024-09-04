#!/usr/bin/env python3

from pathlib import Path
from expert_kb.sqlite_db import SQLiteDB
from expert_kb import KnowledgeBase


def main():
    kb = KnowledgeBase(
        path="./db.sq3",
        embedding_size=100,
    )

    kb.add_fragment(
        fragment_id="test-1",
        text="Big text here",
        embedding=[0.1] * 100,
    )
    # db = SQLiteDB(
    #     Path("./db.sq3"),
    #     vector_length=2,
    # )
    # max_row_id = db.query("""
    # select max(rowid) rowid from embedding
    # """)[0]["rowid"]
    # if not max_row_id:
    #     max_row_id = 0
    #     pass

    # with db.cursor() as cur:
    #     cur.execute(f"""
    #     insert into embedding(rowid, embedding)
    #     values (:row_id, '[0.5, 0.5]')
    #     """, {
    #         "row_id": max_row_id + 1,
    #     })
    #     pass
    # rows = db.query("""
    # select * from embedding;
    # """)
    # print([dict(row) for row in rows])
    return


if __name__ == '__main__':
    main()
