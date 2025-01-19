#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <regex>

// Fungsi untuk melakukan tokenisasi
std::string tokenizeContent(const std::string& content) {
    std::vector<std::string> tokens;
    std::regex wordRegex("\\w+");
    auto wordsBegin = std::sregex_iterator(content.begin(), content.end(), wordRegex);
    auto wordsEnd = std::sregex_iterator();

    for (std::sregex_iterator i = wordsBegin; i != wordsEnd; ++i) {
        tokens.push_back(i->str());
    }

    std::ostringstream tokenized;
    tokenized << "['";
    for (size_t i = 0; i < tokens.size(); ++i) {
        tokenized << tokens[i];
        if (i != tokens.size() - 1) {
            tokenized << "', '";
        }
    }
    tokenized << "']";
    return "\"" + tokenized.str() + "\""; // Tambahkan tanda kutip ganda
}

// Fungsi untuk membaca file CSV dan memproses data
void processCSV(const std::string& inputPath, const std::string& outputPath) {
    std::ifstream inputFile(inputPath);
    std::ofstream outputFile(outputPath);

    if (!inputFile.is_open() || !outputFile.is_open()) {
        std::cerr << "Error: Unable to open file.\n";
        return;
    }

    std::string line;
    std::getline(inputFile, line); // Membaca header
    outputFile << line << ",tokenisasi\n"; // Menambahkan header baru

    while (std::getline(inputFile, line)) {
        std::stringstream ss(line);
        std::string userName, content, score, at, appVersion;

        std::getline(ss, userName, ',');
        std::getline(ss, content, ',');
        std::getline(ss, score, ',');
        std::getline(ss, at, ',');
        std::getline(ss, appVersion, ',');

        // Tokenisasi konten
        std::string tokenizedContent = tokenizeContent(content);

        // Tulis ke file output
        outputFile << userName << "," << content << "," << score << ","
                   << at << "," << appVersion << "," << tokenizedContent << "\n";
    }

    inputFile.close();
    outputFile.close();
    std::cout << "Tokenisasi selesai. File disimpan di: " << outputPath << "\n";
}

int main() {
    std::string inputPath = "C:\\Users\\ghiff\\Documents\\kuliah\\Analisa_Sentimen_Gojek\\percobaan 14\\cleaned_data.csv";
    std::string outputPath = "C:\\Users\\ghiff\\Documents\\kuliah\\Analisa_Sentimen_Gojek\\percobaan 14\\data_tokenisasi.csv";

    processCSV(inputPath, outputPath);
    return 0;
}
