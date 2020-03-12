// unordered_map + list solution
// get: O(capacity), put: O(capacity)
// Runtime: 460 ms, faster than 5.03% of C++ online submissions for LRU Cache.
// Memory Usage: 40.2 MB, less than 34.55% of C++ online submissions for LRU Cache.

class LRUCache {
private:
     int capacity_;
     unordered_map<int, int> map;
     list<int> que;

public:
    LRUCache(int capacity) {
        capacity_ = capacity;
    }

    int get(int key) {
        if (map.find(key) != map.end()) {
            que.remove(key);
            que.push_back(key);
            return map.at(key);
        }
        return -1;
    }

    void put(int key, int value) {
        if (map.find(key) != map.end()) {
            map[key] = value;
            get(key);
            return;
        }
        if (map.size() >= capacity_) {
            map.erase(que.front());
            que.pop_front();
        }
        map.insert(pair<int, int>(key, value));
        get(key);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */