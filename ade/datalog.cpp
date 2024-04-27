#include <iostream>
#include <vector>

using namespace std;

// Define a class to represent assembly in the deductive database
class Assembly {
public:
    string predicate;
    string subject;
    string object;
    int quantity;

    Assembly(string predicate, string subject, string object, int quantity) {
        this->predicate = predicate;
        this->subject = subject;
        this->object = object;
        this->quantity = quantity;
    }
};

// Define a method to execute Datalog queries
vector<Assembly> query(const string& predicate, const vector<Assembly>& database) {
    vector<Assembly> results;
    for (const auto& fact : database) {
        if (fact.predicate == predicate) {
            results.push_back(fact);
        }
    }
    return results;
}

// Define a method to apply the second rule of the deductive database and return newly added tuples
vector<Assembly> applySecondRule(vector<Assembly>& assembly) {
    vector<Assembly> newFacts;
    for (const auto& fact1 : assembly) {
        for (const auto& fact2 : assembly) {
            if (fact1.predicate == "component" && fact2.predicate == "component"
                    && fact1.object == fact2.subject) {
                Assembly newTuple("component", fact1.subject, fact2.object, fact1.quantity);
                // Check if the new tuple already exists in the assembly
                bool exists = false;
                for (const auto& existingTuple : assembly) {
                    if (existingTuple.predicate == newTuple.predicate &&
                        existingTuple.subject == newTuple.subject &&
                        existingTuple.object == newTuple.object &&
                        existingTuple.quantity == newTuple.quantity) {
                        exists = true;
                        break;
                    }
                }
                // If the new tuple does not exist, add it to the list of new facts
                if (!exists) {
                    bool duplicate = false;
                    for (const auto& n : newFacts) {
                        if (n.predicate == newTuple.predicate &&
                            n.subject == newTuple.subject &&
                            n.object == newTuple.object &&
                            n.quantity == newTuple.quantity) {
                            duplicate = true;
                            break;
                        }
                    }
                    if (!duplicate) {
                        newFacts.push_back(newTuple);
                    }
                }
            }
        }
    }
    // Add the new facts to the assembly
    assembly.insert(assembly.end(), newFacts.begin(), newFacts.end());
    return newFacts;
}

int main() {
 vector<Assembly> assembly = {
        Assembly("component", "Wheel", "Trike", 3),
        Assembly("component", "Frame", "Trike", 1),
        Assembly("component", "Spoke", "Wheel", 2),
        Assembly("component", "Tyre", "Wheel", 1),
        Assembly("component", "Seat", "Frame", 1),
        Assembly("component", "Pedal", "Frame", 1),
        Assembly("component", "Tube", "Tyre", 1),
        Assembly("component", "Rim", "Tyre", 1)
    };   


    // Applying the first rule
    cout << "---Applying first rule---\n";
    cout << "Part\tSubpart\tQuantity\n";
    for (const auto& tuple : assembly) {
        cout << tuple.object << "\t" << tuple.subject << "\t" << tuple.quantity << endl;
    }

    // Applying the second rule the first time
    vector<Assembly> newTuples = applySecondRule(assembly);

    // Output the new tuples added after applying the second rule the first time
    cout << "\nNew Tuples Added After First Application of Second Rule:" << endl;
    cout << "Part\tSubpart\tQuantity\n";
    for (const auto& tuple : newTuples) {
        cout << tuple.object << "\t" << tuple.subject << "\t" << tuple.quantity << endl;
    }

    // Applying the second rule the second time
    newTuples = applySecondRule(assembly);

    // Output the new tuples added after applying the second rule the second time
    cout << "\nNew Tuples Added After Second Application of Second Rule:" << endl;
    cout << "Part\tSubpart\tQuantity\n";
    for (const auto& tuple : newTuples) {
        cout << tuple.object << "\t" << tuple.subject << "\t" << tuple.quantity << endl;
    }

    return 0;
}
