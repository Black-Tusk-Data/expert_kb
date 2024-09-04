#!/usr/bin/env python3

import os
import time

from expert_kb.sqlite_db import SQLiteDB
from expert_kb import KnowledgeBase, Fragment


EMBEDDING_SIZE = 8092
KB_PATH = "./test.kb"
N_FRAGMENTS = int(1e4)


def main():
    print("starting test...")
    if os.path.exists(KB_PATH):
        os.remove(KB_PATH)
        pass

    kb = KnowledgeBase(
        path=KB_PATH,
        embedding_size=EMBEDDING_SIZE,
    )

    print("constructing mock data...")
    fragments = [
        Fragment(
            fragment_id=f"test-{i}",
            text=f"Big text here: {i}",
        )
            for i in range(N_FRAGMENTS)
    ]
    embeddings = [
        [1 - 1**(-i)] * EMBEDDING_SIZE
            for i in range(N_FRAGMENTS)
    ]

    print(f"inserting {N_FRAGMENTS} fragments...")
    t0 = time.time()
    kb.add_fragments(fragments, embeddings)
    t1 = time.time()
    print(f"inserted {N_FRAGMENTS} in {round(t1 - t0, 2)} seconds")

    print("searching...")
    t0 = time.time()
    res = kb.search(
        [1.0] * EMBEDDING_SIZE,
        k=10,
    )
    t1 = time.time()
    print(f"completed search in {round(t1 - t0, 2)} seconds")

    print("\nResult:")
    print(res)
    return


if __name__ == '__main__':
    main()
