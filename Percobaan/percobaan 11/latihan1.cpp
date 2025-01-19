#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>

std::vector<std::string> tokenize(const std::string& text) {
    std::vector<std::string> tokens;
    std::istringstream stream(text);
    std::string word;
    while (stream >> word) {
        tokens.push_back(word);
    }
    return tokens;
}

std::string formatTokenizedOutput(const std::vector<std::string>& tokens) {
    std::string formatted = "['";
    for (size_t i = 0; i < tokens.size(); ++i) {
        formatted += tokens[i];
        if (i < tokens.size() - 1) {
            formatted += "', '";
        }
    }
    formatted += "']";
    return formatted;
}

int main() {
    std::string inputFilePath = "J:\\Drive Saya\\analisa sentimen git\\percobaan 5\\combined_train_data.csv";
    std::string outputFilePath = "J:\\Drive Saya\\analisa sentimen git\\percobaan 11\\train_data.csv";

    std::ifstream inputFile(inputFilePath);
    std::ofstream outputFile(outputFilePath);

    if (!inputFile.is_open() || !outputFile.is_open()) {
        std::cerr << "Failed to open input or output file!" << std::endl;
        return 1;
    }

    std::string line, header;
    // Read header
    std::getline(inputFile, header);
    outputFile << "full_text,Value,full_text_tokenized\n"; // Add header for output

    while (std::getline(inputFile, line)) {
        std::istringstream lineStream(line);
        std::string full_text, value;

        // Parse CSV fields
        std::getline(lineStream, full_text, ',');
        std::getline(lineStream, value, ',');

        // Tokenize the full_text
        std::vector<std::string> tokens = tokenize(full_text);

        // Format tokenized output as a list
        std::string tokenizedText = formatTokenizedOutput(tokens);

        // Write to output file
        outputFile << full_text << "," << value << ",\"" << tokenizedText << "\"\n";
    }

    inputFile.close();
    outputFile.close();

    std::cout << "Tokenization complete! File saved to: " << outputFilePath << std::endl;
    return 0;
}
