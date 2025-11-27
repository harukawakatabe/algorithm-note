# 设计链表



设计并实现自己的链表。

单链表中的节点应该具备两个属性：`val` 和 `next` 。`val` 是当前节点的值，`next` 是指向下一个节点的指针/引用。

实现 `MyLinkedList` 类：

- `MyLinkedList()` 初始化 `MyLinkedList` 对象。
- `int get(int index)` 获取链表中下标为 `index` 的节点的值。如果下标无效，则返回 `-1` 。
- `void addAtHead(int val)` 将一个值为 `val` 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
- `void addAtTail(int val)` 将一个值为 `val` 的节点追加到链表中作为链表的最后一个元素。
- `void addAtIndex(int index, int val)` 将一个值为 `val` 的节点插入到链表中下标为 `index` 的节点之前。如果 `index` 等于链表的长度，那么该节点会被追加到链表的末尾。如果 `index` 比长度更大，该节点将 **不会插入** 到链表中。
- `void deleteAtIndex(int index)` 如果下标有效，则删除链表中下标为 `index` 的节点。



```python
# 包含5个函数

获取第n个元素的值
头节点插入值
尾节点插入值
第n个元素前插入值
删除第n个元素
```



```python
# 通用考虑点
1.index合法判断
	1.1 边界问题，是否包含index=size这个点
 	 1.2 涉及 获取第n个元素的值/第n个元素前插入值/删除第n个元素
2.cur指标初始位置
	2.1 指向dummy_head		
    		删除&插入
	2.2 指向dummy_head.next
    		查找
3.更改指向的顺序
4.遍历结束的条件！！
```



```python
# 首先需要定义链表的节点
# class ListNode:               
#     def __init__(self):   # 这种写法没有留传参的位置，所以会报TypeError的错
#         self.val = None
#         self.next = None
# TypeError: __init__() got an unexpected keyword argument 'val'
#     new_node = ListNode(val = val)

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val 
        self.next = next 

"""
问题：1.head在哪里定义呢？不需要定义head指针吗？
    dummy_head节点已经定义了头节点
"""
class MyLinkedList(object):
    # 定义虚拟头节点 & 链表长度
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0
        
    """
    通用思路：
        1.先判断传入的n是否合法
        2.定义新指针cur来遍历链表
    """
    def get(self, index):
        """
        :type index: int
        :rtype: int
        思路：需要考虑如何赋值：：如何遍历
        Point:边界问题
        """
        if index<0 or index>=self.size:  # Point：边界问题 index>=self.size or index>self.size
            return -1
        # cur = self.dummy_head -> return cur.next.val 取值正确，但是不太符合链表的语义
        cur = self.dummy_head.next # 从index=0开始移动指针
        for i in range(index):
            cur = cur.next
        return cur.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        思路：顺序！！ 必须要考虑赋值后还能不能找到下一个节点
        单行写法：
            1.读取参数val=val，next=self.dummy_head.next
            2.创建ListNode对象
            3.赋值给dummy_head.next
        """
        # new_node = ListNode(val = val)
        # new_node.next = self.dummy_head.next 
        # self.dummy_head.next = new_node     
        # self.size += 1   
        # 优化：使用虚拟头节点，直接在头节点后面插入新节点
        self.dummy_head.next = ListNode(val=val,next=self.dummy_head.next)
        self.size += 1
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        思路：找到next指向null的节点
        point: 代入初始化添加元素验证，cur = self.dummy_head.next 从index=0开始遍历，第一个元素会加不上
        """
        cur = self.dummy_head # 不可以从index=0开始遍历 cur = self.dummy_head.next
        while cur.next != None:
            cur = cur.next
        tail_node = ListNode(val=val)
        cur.next = tail_node
        self.size += 1

        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        point:
            1.插入下标=index之前
            2.注意指标指向顺序！
        """
        if index<0 or index>self.size:
            return
        cur = self.dummy_head # 从index=-1开始，最终cur指向需要插入的元素的前面
        new_node = ListNode(val=val)
        for i in range(index):
            cur = cur.next 
        new_node.next = cur.next
        # cur.next = new_node.next # 顺序没错但赋值错误，cur.next应该是new_node本身
        cur.next = new_node
        self.size += 1


    def deleteAtIndex(self, index):
        """
        删除第n个元素
        思路：
            1.首先需要判断传入index是否合法  
            2.第n个元素必须是cur.next
        point: 代入极端值验证边界情况
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        cur = self.dummy_head
        # 走多少次移动多少次，因为cur初始化时指向
        for i in range(index):
            # 移动指针
            cur = cur.next
        cur.next = cur.next.next 
        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
index = 1
# val = 3
obj = MyLinkedList()
# param_1 = obj.get(index)
# print(param_1)
obj.addAtHead(1)
obj.addAtTail(3)
for i in range(obj.size):
    print(obj.get(i),end=" ")
obj.addAtIndex(index,2)
# obj.get(index)
# obj.deleteAtIndex(index)
print(f"size：{obj.size}")
for i in range(obj.size):
    print(obj.get(i),end=" ")
for i in range(obj.size):
    print(obj.get(i))
# obj.get(index)



"""
这种报错就是链表的结构破坏了
  File "d:\LLM\pythonProject\basic\algorithm\LinkedList\02_0707_MyLinkedList.py", line 134, in <module>
    print(obj.get(i),end=" ")
          ^^^^^^^^^^
  File "d:\LLM\pythonProject\basic\algorithm\LinkedList\02_0707_MyLinkedList.py", line 42, in get
    return cur.val
"""
```

