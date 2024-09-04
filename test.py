#!/usr/bin/env python3

from pathlib import Path
from expert_kb.sqlite_db import SQLiteDB


def main():
    db = SQLiteDB(
        Path("./db.sq3"),
        vector_length=2,
    )
    max_row_id = db.query("""
    select max(rowid) rowid from embedding
    """)[0]["rowid"]
    if not max_row_id:
        max_row_id = 0
        pass

    with db.cursor() as cur:
        cur.execute(f"""
        insert into embedding(rowid, embedding)
        values (:row_id, '[0.5, 0.5]')
        """, {
            "row_id": max_row_id + 1,
        })
        pass
    rows = db.query("""
    select * from embedding;
    """)
    print([dict(row) for row in rows])
    return


if __name__ == '__main__':
    main()
