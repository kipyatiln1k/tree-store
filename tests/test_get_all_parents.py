from tree_store import TreeStore


def test_get_all_parents():
    items = [
        {"id": 7, "parent": 4, "type": None},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 1, "parent": "root"},
    ]
    item_id = items[0]["id"]
    parents = items[1:]

    assert TreeStore(items).getAllParents(item_id) == parents
