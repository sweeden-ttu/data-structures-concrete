# data-structures-swift

Swift data structure implementations for Apple platforms and Linux.

## Overview

This project provides Swift data structure implementations with support for macOS, iOS, and Linux.

## Features

- **Generic implementations** - Type-safe data structures
- **Value types** - Swift-native value semantics
- **Thread-safe variants** - Concurrent data structures
- **Cross-platform** - macOS, iOS, Linux

## Data Structures

### Linear Structures
- Stack, Queue, Deque, List, Array

### Tree Structures
- Tree, BinaryTree, BST, Trie

### Graph Structures
- Graph, DirectedGraph, UndirectedGraph

### Hash Structures
- HashTable, BloomFilter

### Heap Structures
- MinHeap, MaxHeap, PriorityQueue

## Quick Start

```swift
import DataStructures

let stack = Stack<Int>()
stack.push(1)
stack.push(2)
print(stack.pop()) // 2

let queue = Queue<String>()
queue.enqueue("first")
queue.enqueue("second")
print(queue.dequeue()) // "first"
```

## License

MIT License
