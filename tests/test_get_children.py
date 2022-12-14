from tree_store import TreeStore


def test_get_children(items):
    parent_id = 4
    item = [item for item in items if item["id"] == parent_id].pop()
    children = [item for item in items if item["parent"] == parent_id]
    method_result = TreeStore(items).getChildren(parent_id)
    assert all(item in method_result for item in children)
    assert all(item in children for item in method_result)
