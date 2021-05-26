class BinarySearch:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearch(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearch(data)

    def in_order_traversal(self):
        elements = []
        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        #visit base node
        elements.append(self.data)
        
        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            #might be in left sub tree
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            #might be in right sub tree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        # min = self.data
        # if self.left:
        #     if self.data > self.left.data:
        #         min = self.left.find_min()
        # return min
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        # max = self.data
        # if self.right:
        #     if self.data < self.right.data:
        #         max = self.right.find_max()
        # return max
        if self.data is None:
            return -1
        return(max(self.left.find_max(), self.right.find_max()))
        # if self.right is None:
        #     return self.data
        # return self.right.find_max()
    
    def calculate_sum(self):
        sum = 0
        if self.data:
            sum += self.data
        if self.left:
            sum += self.left.calculate_sum()
        if self.right:
            sum += self.right.calculate_sum()
        return sum

    def post_order_transversal(self):
        elements = []
        #visit left 
        if self.left:
            elements += self.left.post_order_transversal()
        
        #visit right
        if self.right:
            elements += self.right.post_order_transversal()

        # geting data:
        if self.data:
            elements.append(self.data)
        
        return elements
    
    def pre_order_tranversal(self):
        elements = []
        #add node
        elements.append(self.data)
        #visit left
        if self.left:
            elements += self.left.pre_order_tranversal()
        #visit right 
        if self.right:
            elements += self.right.pre_order_tranversal()
        
        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None: 
                return self.right

            #taking min value from right sub tree
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

            #taking max value from left sub tree
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

def build_tree(elements):
    root = BinarySearch(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == "__main__":
    numbers = [15, 12, 7, 14, 27, 20, 23, 88]  #[4, 27 ,80, 92, 9, 10, 456, -199, 600, 2, 289, 7, 2, 0, 10, 67, 99, 78, 289, 2, 10]
    numbers_tree = build_tree(numbers)
    # print(numbers_tree.in_order_traversal())
    # print(numbers_tree.search(-1)) 
    # print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    # print(numbers_tree.calculate_sum())
    # print(numbers_tree.post_order_transversal())
    # print(numbers_tree.pre_order_tranversal())
    # numbers_tree.delete(20)
    # numbers_tree.delete(7)
    # print(numbers_tree.in_order_traversal())

    # map = ["india", "usa", "california", "india", "hogwarts", "ahmedabad", "india"]
    # map_tree = build_tree(map)
    # print(map_tree.search("kazak"))
    # print(map_tree.in_order_traversal())