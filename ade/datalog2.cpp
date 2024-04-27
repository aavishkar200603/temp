#include <iostream>
#include <vector>
#include <string>
#include <tuple>

using namespace std;

// Define the deductive database facts
vector<tuple<string, string, string, int>> facts = {
    make_tuple("component", "wheel", "tricycle", 3),
    make_tuple("component", "frame", "tricycle", 1),
    make_tuple("component", "spoke", "wheel", 2),
    make_tuple("component", "tyre", "wheel", 1),
    make_tuple("component", "seat", "frame", 1),
    make_tuple("component", "pedal", "frame", 1),
    make_tuple("component", "tube", "tyre", 1),
    make_tuple("component", "rim", "tyre", 1)
};

// Define a function to execute Datalog queries
vector<tuple<string, string, int>> query(const string& predicate, const vector<tuple<string, string, string, int>>& database) {
    vector<tuple<string, string, int>> results;
    for (const auto& fact : database) {
        if (get<0>(fact) == predicate) {
            results.push_back(make_tuple(get<1>(fact), get<2>(fact), get<3>(fact)));
        }
    }
    return results;
}

int main() {
    // Execute a Datalog query to get all components of the tricycle
    auto results = query("component", facts);

    // Output the results with quantities
    cout << "All components of the tricycle:" << endl;
    for (const auto& result : results) {
        cout << "- " << get<0>(result) << " with quantity " << get<2>(result) << endl;
    }

    // Additional queries
    // Query to find all components of the wheel
    cout << "\nAll components of the wheel:" << endl;
    for (const auto& component : facts) {
        if (get<1>(component) == "wheel") {
            cout << "- " << get<0>(component) << " with quantity " << get<3>(component) << endl;
        }
    }

    // Query to find all components of the frame
    cout << "\nAll components of the frame:" << endl;
    for (const auto& component : facts) {
        if (get<1>(component) == "frame") {
            cout << "- " << get<0>(component) << " with quantity " << get<3>(component) << endl;
        }
    }

    // Query to find all components of the tyre
    cout << "\nAll components of the tyre:" << endl;
    for (const auto& component : facts) {
        if (get<1>(component) == "tyre") {
            cout << "- " << get<0>(component) << " with quantity " << get<3>(component) << endl;
        }
    }

    // Load facts into the database
    vector<tuple<string, string, string, int>> database = facts;

    // Define a function to find components recursively
    vector<tuple<string, string>> find_components(const string& part, const vector<tuple<string, string, string, int>>& database) {
        vector<tuple<string, string>> components;
        for (const auto& fact : database) {
            if (get<0>(fact) == "Assembly" && get<1>(fact) == part) {
                string subpart = get<2>(fact);
                components.push_back(make_tuple(part, subpart));
                auto sub_components = find_components(subpart, database);
                components.insert(components.end(), sub_components.begin(), sub_components.end());
            }
        }
        return components;
    }

    // Execute the Datalog query to find components
    vector<tuple<string, string>> all_components;
    for (const auto& fact : database) {
        if (get<0>(fact) == "Assembly") {
            string part = get<1>(fact);
            auto components = find_components(part, database);
            all_components.insert(all_components.end(), components.begin(), components.end());
        }
    }

    // Print the result
    cout << "Components:" << endl;
    for (const auto& [part, subpart] : all_components) {
        cout << "- " << subpart << " is a component of " << part << endl;
    }

    return 0;
}
