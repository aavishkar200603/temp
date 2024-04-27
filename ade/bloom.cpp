#include <iostream>
#include <vector>
#include <bitset>
#include <string>
#include <algorithm>

using namespace std;

class BloomFilter {
private:
    bitset<10> bitSet;
    int filterSize;
    int numHashFunctions;

public:
    BloomFilter(int size, int numFunctions) : filterSize(size), numHashFunctions(numFunctions) {}

    void add(string key) {
        for (int i = 0; i < numHashFunctions; ++i) {
            int hash = hashFunction(key, i);
            bitSet.set(hash);
        }
    }

    bool contains(string key) {
        for (int i = 0; i < numHashFunctions; ++i) {
            int hash = hashFunction(key, i);
            if (!bitSet.test(hash))
                return false;
        }
        return true;
    }

private:
    int hashFunction(string key, int index) {
        int x = stoi(key);
        return (3 * x + 1 + index) % filterSize;
    }
};

vector<string> bloomJoin(vector<string>& relation1, vector<string>& relation2) {
    // Create Bloom filter for relation 2
    BloomFilter bloomFilter(10, 3);
    for (const auto& row : relation2) {
        auto commaPos = row.find(",");
        string key = row.substr(0, commaPos);
        bloomFilter.add(key);
    }

    // Perform join
    vector<string> result;
    for (const auto& row : relation1) {
        auto commaPos = row.find(",");
        string key = row.substr(0, commaPos);
        if (bloomFilter.contains(key)) {
            auto rowData = find_if(relation2.begin(), relation2.end(), [key](const string& s) {
                return s.find(key) == 0;
            });
            if (rowData != relation2.end()) {
                result.push_back(*rowData);
            }
        }
    }

    return result;
}

int main() {
    // Sample relations (tables)
    vector<string> relation1 = {
        "201, John",
        "202, Jane",
        "203, Alice",
        "204, Bob",
        "205, David"
    };

    vector<string> relation2 = {
        "201, Engineer, New York",
        "202, Manager, London",
        "204, Developer, San Francisco",
        "206, Analyst, Sydney"
    };

    // Perform Bloom join
    auto result = bloomJoin(relation1, relation2);

    // Print result
    for (const auto& row : result) {
        cout << row << endl;
    }

    return 0;
}
