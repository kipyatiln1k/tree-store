from tree_store import TreeStore


def test_tree_store_get_all_is_items(items):
    tree_store_items = TreeStore(items).getAll()
    assert all(item in tree_store_items for item in items)
    assert all(item in items for item in tree_store_items)
