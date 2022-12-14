class TreeStore:
    def __init__(self, items=[]):
        self._items = {}
        self._children = {}
        for item in items:
            self._items[item["id"]] = item
            if item["parent"] != "root":
                self._children.setdefault(item["parent"], []).append(item)

    def getAll(self):
        return self._items.values()

    def getItem(self, item_id):
        return self._items[item_id]

    def getChildren(self, parent_id):
        return self._children[parent_id]

    def getAllParents(self, item_id):
        current = self.getItem(item_id)
        result = []

        while current["parent"] != "root":
            current = self.getItem(current["parent"])
            result.append(current)

        return result
