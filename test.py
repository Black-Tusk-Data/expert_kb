#!/usr/bin/env python3

from pathlib import Path
from expert_kb.sqlite_db import SQLiteDB
from expert_kb import KnowledgeBase, Fragment


def main():
    kb = KnowledgeBase(
        path="./db.sq3",
        embedding_size=100,
    )

    # kb.add_fragments(
    #     [
    #         Fragment(
    #             fragment_id=f"test-{i}",
    #             text=f"Big text here: {i}",
    #         )
    #         for i in range(100)
    #     ],
    #     [
    #         [1 - 1**(-i)] * 100
    #         for i in range(100)
    #     ]
    # )

    res = kb.search(
        [1.0] * 100,
    )
    print(res)

    
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
