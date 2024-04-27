#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <sstream>
#include <cctype>
#include <iomanip> 

using namespace std;

unordered_map<int, unordered_map<string, int>> createDocumentVectors(vector<string>& documents) {
    unordered_map<int, unordered_map<string, int>> documentVectors;
    int documentId = 1;
    
    for (const auto& document : documents) {
        istringstream iss(document);
        string word;
        unordered_map<string, int> vector;
        
        // Tokenize document
        while (iss >> word) {
            // Convert word to lowercase
            for (char& c : word) {
                c = std::tolower(c);
            }
            vector[word]++;
        }
        
        documentVectors[documentId++] = vector;
    }
    
    return documentVectors;
}

pair<int, unordered_set<string>> calculateDotProductWithCommonWords(unordered_map<string, int>& vector1, unordered_map<string, int>& vector2) {
    int dotProduct = 0;
    unordered_set<string> commonWords;
    
    // Calculate dot product and find common words
    for (const auto& entry : vector1) {
        const string& word = entry.first;
        int frequency1 = entry.second;
        int frequency2 = vector2[word];
        
        if (frequency2 > 0) {
            dotProduct += frequency1 * frequency2;
            commonWords.insert(word);
        }
    }
    
    return make_pair(dotProduct, commonWords);
}

void displayDocumentVectors(unordered_map<int, unordered_map<string, int>>& documentVectors) {
    // Get unique words across all documents
    unordered_set<string> uniqueWords;
    for (const auto& vector : documentVectors) {
        for (const auto& wordFreq : vector.second) {
            uniqueWords.insert(wordFreq.first);
        }
    }

    // Calculate maximum width for words and frequencies
    size_t maxWordWidth = 0;
    size_t maxFreqWidth = 0;
    for (const auto& word : uniqueWords) {
        maxWordWidth = max(maxWordWidth, word.size());
    }
    for (const auto& entry : documentVectors) {
        for (const auto& wordFreq : entry.second) {
            maxFreqWidth = max(maxFreqWidth, to_string(wordFreq.second).size());
        }
    }

    // Display header
    cout << left << setw(12) << "Document id";
    for (const auto& word : uniqueWords) {
        cout << setw(maxWordWidth + 2) << word;
    }
    cout << endl;

    // Display vectors
    for (const auto& entry : documentVectors) {
        int documentId = entry.first;
        const auto& vector = entry.second;

        cout << left << setw(12) << documentId;
        for (const auto& word : uniqueWords) {
            int frequency = vector.count(word) ? vector.at(word) : 0;
            cout << setw(maxWordWidth + 2) << frequency;
        }
        cout << endl;
    }

}

int main() {
    // Sample documents
    vector<string> documents = {
       "alice wonderland rabbit tea party",
        "wonderland adventure rabbit hole",
        "alice adventures wonderland",
        "rabbit hole adventure mad hatter tea"
    };
    
    // Create document vectors
    auto documentVectors = createDocumentVectors(documents);
    
    // Display document vectors
    displayDocumentVectors(documentVectors);
    
    // Compare document similarity for all pairs of documents
    for (int i = 1; i <= documents.size(); ++i) {
        for (int j = i + 1; j <= documents.size(); ++j) {
            auto dotProductWithCommonWords = calculateDotProductWithCommonWords(documentVectors[i], documentVectors[j]);
            
            cout << "Dot Product between documents " << i << " and " << j << ": " << dotProductWithCommonWords.first << endl;
            cout << "Common words between documents " << i << " and " << j << ": ";
            for (const auto& word : dotProductWithCommonWords.second) {
                cout << word << " ";
            }
            cout << endl;
        }
    }

    return 0;
}



