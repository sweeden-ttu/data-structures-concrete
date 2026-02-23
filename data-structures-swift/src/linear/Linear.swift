import Foundation

public struct Stack<T> {
    private var items: [T] = []
    
    public init() {}
    
    public mutating func push(_ item: T) {
        items.append(item)
    }
    
    public mutating func pop() -> T? {
        items.popLast()
    }
    
    public func peek() -> T? {
        items.last
    }
    
    public var isEmpty: Bool {
        items.isEmpty
    }
    
    public var count: Int {
        items.count
    }
}

public struct Queue<T> {
    private var items: [T] = []
    
    public init() {}
    
    public mutating func enqueue(_ item: T) {
        items.append(item)
    }
    
    public mutating func dequeue() -> T? {
        guard !items.isEmpty else { return nil }
        return items.removeFirst()
    }
    
    public func peek() -> T? {
        items.first
    }
    
    public var isEmpty: Bool {
        items.isEmpty
    }
    
    public var count: Int {
        items.count
    }
}

public struct Deque<T> {
    private var items: [T] = []
    
    public init() {}
    
    public mutating func pushFront(_ item: T) {
        items.insert(item, at: 0)
    }
    
    public mutating func pushBack(_ item: T) {
        items.append(item)
    }
    
    public mutating func popFront() -> T? {
        guard !items.isEmpty else { return nil }
        return items.removeFirst()
    }
    
    public mutating func popBack() -> T? {
        items.popLast()
    }
    
    public func front() -> T? {
        items.first
    }
    
    public func back() -> T? {
        items.last
    }
    
    public var isEmpty: Bool {
        items.isEmpty
    }
    
    public var count: Int {
        items.count
    }
}
