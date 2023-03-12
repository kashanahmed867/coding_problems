class CategoryTree:
    def __init__(self):
        self.categories = {}
        
    def add_category(self, category, parent):
        # Check if the category has already been added
        if category in self.categories:
            raise KeyError('Category already exists')
        
        # Check if the parent category exists
        if parent is not None and parent not in self.categories:
            raise KeyError('Parent category does not exist')
        
        # Add the category to the tree
        self.categories[category] = parent

    def get_children(self, parent):
        children = [category for category, parent_category in self.categories.items() if parent_category == parent]
        return children

if __name__ == "__main__":
    c = CategoryTree()
    c.add_category('A', None)
    c.add_category('B', 'A')
    c.add_category('C', 'A')
    print(','.join(c.get_children('A') or []))
