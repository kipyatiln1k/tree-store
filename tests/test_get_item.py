from tree_store import TreeStore


def test_get_item(items):
    item = items[0]
    item_id = item["id"]

    assert TreeStore(items).getItem(item_id) == item
