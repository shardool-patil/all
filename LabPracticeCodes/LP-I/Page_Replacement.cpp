#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>
using namespace std;

class PageReplacement {
    int frames; // Number of frames
    vector<int> pages; // Page reference string

public:
    PageReplacement(int frames, vector<int> pages){
        this->frames=frames;
        this->pages=pages;
    }

    void FIFO() {
        queue<int> memory;
        unordered_map<int, bool> isInMemory;
        int pageFaults = 0;

        cout << "FIFO Page Replacement:\n";
        for (int page : pages) {
            if (isInMemory[page] == false) { // Page fault
                pageFaults++;
                if (memory.size() == frames) { // Remove the oldest page
                    int oldestPage = memory.front();
                    memory.pop();
                    isInMemory[oldestPage] = false;
                }
                memory.push(page);
                isInMemory[page] = true;
                cout << "Page " << page << " loaded (Page Fault)\n";
            } else {
                cout << "Page " << page << " accessed (Hit)\n";
            }
        }
        cout << "Total Page Faults: " << pageFaults << "\n\n";
    }

    void LRU() {
        vector<int> memory;
        int pageFaults = 0;

        cout << "LRU Page Replacement:\n";
        for (int page : pages) {
            auto it = find(memory.begin(), memory.end(), page);
            if (it == memory.end()) { // Page fault
                pageFaults++;
                if (memory.size() == frames) {
                    memory.erase(memory.begin()); // Remove least recently used page
                }
                memory.push_back(page);
                cout << "Page " << page << " loaded (Page Fault)\n";
            } else { // Page hit
                memory.erase(it); // Remove and re-insert to update usage order
                memory.push_back(page);
                cout << "Page " << page << " accessed (Hit)\n";
            }
        }
        cout << "Total Page Faults: " << pageFaults << "\n\n";
    }

    void Optimal() {
        vector<int> memory;
        int pageFaults = 0;

        cout << "Optimal Page Replacement:\n";
        for (int i = 0; i < pages.size(); i++) {
            int page = pages[i];
            auto it = find(memory.begin(), memory.end(), page);

            if (it == memory.end()) { // Page fault
                pageFaults++;
                if (memory.size() == frames) {
                    int farthestIndex = -1, pageToReplace = -1;
                    for (int memPage : memory) {
                        auto nextUsage = find(pages.begin() + i + 1, pages.end(), memPage);
                        int dist;
                        if (nextUsage == pages.end()) {
                            dist = pages.size();  // If the page is not found again, set dist to the size of the pages
                        } else {
                            dist = distance(pages.begin(), nextUsage);  // Otherwise, calculate the distance to the next usage of the page
                        }

                        if (dist > farthestIndex) {
                            farthestIndex = dist;
                            pageToReplace = memPage;
                        }
                    }
                    memory.erase(find(memory.begin(), memory.end(), pageToReplace));
                }
                memory.push_back(page);
                cout << "Page " << page << " loaded (Page Fault)\n";
            } else {
                cout << "Page " << page << " accessed (Hit)\n";
            }
        }
        cout << "Total Page Faults: " << pageFaults << "\n\n";
    }
};

int main() {
    int frames;
    int numPages;
    vector<int> pages;

    cout << "Enter the number of frames: ";
    cin >> frames;

    cout << "Enter the number of pages: ";
    cin >> numPages;

    cout << "Enter the page reference string:\n";
    for (int i = 0; i < numPages; i++) {
        int page;
        cin >> page;
        pages.push_back(page);
    }

    PageReplacement pr(frames, pages);
    pr.FIFO();
    pr.LRU();
    pr.Optimal();

    return 0;
}
