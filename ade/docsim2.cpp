#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <sstream>

using namespace std;

// Function to preprocess text
string preprocessText(string text) {
    // Convert text to lowercase
    transform(text.begin(), text.end(), text.begin(), ::tolower);
    
    // Remove punctuation
    string punctuation = ".,;:?!";
    for (char c : punctuation) {
        text.erase(remove(text.begin(), text.end(), c), text.end());
    }
    
    return text;
}

// Function to calculate term frequency (TF)
unordered_map<string, double> calculateTF(string text) {
    unordered_map<string, double> tfMap;
    istringstream iss(text);
    string word;
    int totalWords = 0;
    while (iss >> word) {
        tfMap[word]++;
        totalWords++;
    }
    for (auto& pair : tfMap) {
        pair.second /= totalWords; // Normalize term frequency
    }
    return tfMap;
}

// Function to calculate cosine similarity
double calculateCosineSimilarity(const unordered_map<string, double>& tf1, const unordered_map<string, double>& tf2) {
    double dotProduct = 0.0, mag1 = 0.0, mag2 = 0.0;
    
    // Calculate dot product
    for (auto& pair : tf1) {
        auto it = tf2.find(pair.first);
        if (it != tf2.end()) {
            dotProduct += pair.second * it->second;
        }
    }
    
    // Calculate magnitude of vectors
    for (auto& pair : tf1) {
        mag1 += pow(pair.second, 2);
    }
    for (auto& pair : tf2) {
        mag2 += pow(pair.second, 2);
    }
    
    // Calculate cosine similarity
    double similarity = dotProduct / (sqrt(mag1) * sqrt(mag2));
    return similarity;
}

int main() {
    // Example documents
    string document1 = "Machine learning is the study of computer algorithms that improve automatically through experience.";
    string document2 = "Artificial intelligence is the simulation of human intelligence by machines.";
    
    // Preprocess documents
    document1 = preprocessText(document1);
    document2 = preprocessText(document2);
    
    // Calculate TF (term frequency)
    unordered_map<string, double> tf1 = calculateTF(document1);
    unordered_map<string, double> tf2 = calculateTF(document2);
    
    // Calculate cosine similarity
    double similarity = calculateCosineSimilarity(tf1, tf2);
    
    cout << "Similarity Score: " << similarity << endl;
    
    return 0;
}
