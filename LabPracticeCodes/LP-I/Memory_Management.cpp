#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
# define MAX 20

class MemoryStrategy{
    int memorySize[MAX];
    int **processInfo;
    int n, m;
    public:
    
    MemoryStrategy(){

        for(int i = 0; i < MAX; i++){
            memorySize[i] = -1;
        }
        memorySize[2] = 100; // adding used up spaces
        memorySize[5] = 100;
        memorySize[6] = 100;
        memorySize[13] = 100;

        cout<<"Enter the number of processes: ";cin>>n;
        processInfo = new int*[n];
        for(int i = 0; i < n; i++){
            processInfo[i] = new int[2];
        }

        for(int i = 0; i<n; i++){
            cout<<"Enter the memory request by process P"<<i<<" ";
            processInfo[i][0] = i;
            cin>>processInfo[i][1];
        }
    }
    
    void displayProcess(){
        for(int i = 0; i < n; i++){
            cout<<"Process ID: "<<processInfo[i][0]<<"\t\t";
            cout<<"Requested memory: "<<processInfo[i][1];
            cout<<endl;
        }
    }

    void displayMemory(){
        for(int i = 0; i < MAX; i++){
            cout<<memorySize[i]<<"|";
        }
    }

    void FirstFit(){
        for(int i = 0; i < n; i++){
            int processSize = processInfo[i][1];
            int j = 0;
            int size = 0;
            while(j < MAX){
                if(memorySize[j] == -1 and size != processSize){
                    j++;
                    size++;
                    if(size == processSize){break;}
                }else{
                    j++;
                    size = 0;
                }
            }
            while(size != 0){
                memorySize[j-1] = processInfo[i][0];
                j--; size--;
            }
        }
    }

    void NextFit(){
        int j=0;

        for(int i=0; i < n; i++){
            int processSize=processInfo[i][1];
            int size=0;

            while(j<MAX){
                if(memorySize[j]==-1 && size!=processSize){
                    j++;
                    size++;
                    if(size==processSize)
                        break;
                }else{
                    j++;
                    size=0;
                }
            }

            if(j==MAX){
                j=0;
                size=0;

                while(j<MAX){
                    if(memorySize[j]==-1 && size!=processSize){
                        j++;
                        size++;
                        if(size==processSize)
                            break;
                    }else{
                        j++;
                        size=0;
                    }
                }
            }

            if(size==processSize){
                int temp=j;
                while(size!=0){
                    memorySize[temp-1]=processInfo[i][0];
                    temp--;
                    size--;
                }
            }else
                cout<<"Process"<<processInfo[i][0]<<" process could not be allocated"<<endl;
        }
    }

    void BestFit(){
        vector <int> hole;
        vector <vector<int>> holes;
        int size = 0;
        for(int i = 0; i < MAX; i++){
            hole.clear();
            if(memorySize[i] == -1){
                size ++;
                if (i == MAX-1){
                    hole.push_back(size);
                    hole.push_back(i-size);
                    holes.push_back(hole);
                    break;
                }
            }else{
                hole.push_back(size);
                hole.push_back(i-size);
                holes.push_back(hole);
                size = 0;
            }
        }

        // Available hole sizes
        for (const auto& h : holes) {
        cout << "Size: " << h[0] << ", Starting Index: " << h[1] << endl;
        }   
        // Allocating best hole
        for (int i = 0; i < n; i++) {
            int Psize = processInfo[i][1];
            bool allocated = false;

            for (auto& h : holes) {
                if (Psize <= h[0]) { 
                    
                    for (int k = h[1]; k < h[1] + Psize; k++) {
                        memorySize[k] = processInfo[i][0]; 
                    }
                    
                    h[0] -= Psize; 
                    h[1] += Psize; 

                    
                    if (h[0] == 0) {
                        
                        h[0] = 0; 
                    }

                    allocated = true; 
                    break; 
                }
            }

            if (!allocated) {
                cout << "Process " << processInfo[i][0] << " could not be allocated." << endl;
            }
        }

    }

    void WorstFit() {
        vector<vector<int>> holes;
        int size = 0;
        for (int i = 0; i < MAX; i++) {
            if (memorySize[i] == -1) {
                size++;
            } else if (size > 0) {
                holes.push_back({size, i - size});
                size = 0;
            }
        }
        if (size > 0) {
            holes.push_back({size, MAX - size});
        }
        for (int i = 0; i < n; i++) {
            int Psize = processInfo[i][1];
            auto worstHole = holes.end();
            for (auto it = holes.begin(); it != holes.end(); ++it) {
                if (Psize <= (*it)[0] && (worstHole == holes.end() || (*it)[0] > (*worstHole)[0])) {
                    worstHole = it;
                }
            }
            if (worstHole != holes.end()) {
                for (int k = (*worstHole)[1]; k < (*worstHole)[1] + Psize; k++) {
                    memorySize[k] = processInfo[i][0];
                }
                (*worstHole)[0] -= Psize;
                (*worstHole)[1] += Psize;
                if ((*worstHole)[0] == 0) {
                    holes.erase(worstHole);
                }
            } else {
                cout << "Process " << processInfo[i][0] << " could not be allocated." << endl;
            }
        }
    }
};

int main(){
    MemoryStrategy m1;
    m1.displayProcess();
    //m1.FirstFit();
    //m1.NextFit();
    m1.BestFit();
    m1.displayMemory();
    return 0;
}



