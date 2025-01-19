#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

int main() {
    std::string filePath = R"(J:\Drive Saya\analisa sentimen git\percobaan 5\combined_train_data.csv)";
    std::string outputPath = R"(J:\Drive Saya\analisa sentimen git\percobaan 5\tokenized_train_data2.csv)";

    // Membuka file input dan output
    std::ifstream inputFile(filePath);
    std::ofstream outputFile(outputPath);

    // Memeriksa apakah file berhasil dibuka
    if (!inputFile.is_open()) {
        std::cerr << "Gagal membuka file input: " << filePath << std::endl;
        return 1;
    }
    if (!outputFile.is_open()) {
        std::cerr << "Gagal membuka file output: " << outputPath << std::endl;
        return 1;
    }

    std::string line;
    bool isHeader = true;

    // Menulis header baru ke file output
    outputFile << "full_text,Value,full_text_tokenized\n";

    // Membaca file baris demi baris
    while (std::getline(inputFile, line)) {
        // Mengabaikan header pada file input
        if (isHeader) {
            isHeader = false;
            continue;
        }

        std::stringstream ss(line);
        std::string fullText, value;

        // Memisahkan kolom berdasarkan koma
        std::getline(ss, fullText, ',');
        std::getline(ss, value);

        // Tokenisasi kolom full_text
        std::stringstream textStream(fullText);
        std::string word;
        std::vector<std::string> tokens;

        while (textStream >> word) {
            tokens.push_back(word);
        }

        // Membuat string tokenized dalam format Python list
        std::ostringstream tokenizedText;
        tokenizedText << "['";
        for (size_t i = 0; i < tokens.size(); ++i) {
            tokenizedText << tokens[i];
            if (i < tokens.size() - 1) {
                tokenizedText << "', '";
            }
        }
        tokenizedText << "']";

        // Menulis hasil ke file output
        outputFile << fullText << "," << value << "," << tokenizedText.str() << "\n";
    }

    // Menutup file
    inputFile.close();
    outputFile.close();

    std::cout << "Proses tokenisasi selesai. Hasil disimpan di: " << outputPath << std::endl;

    return 0;
}