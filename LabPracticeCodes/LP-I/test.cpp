#include<iostream>
#include<queue>
#include<vector>
#include<unordered_map>
#include<algorithm>
using namespace std;

class PageReplacement{
    int frames;
    vector<int>pages;

    PageReplacement(int frames,vector<int>pages){
        this->pages=pages;
        this->frames=frames;
    }

    void FIFO(){
        int pageFaults=0;
        queue<int>memory;
        unordered_map<int,bool>isInMemory;

        for(int page:pages){
            if(isInMemory[page]==false){
                pageFaults++;
                if(memory.size()==frames){
                    int pageToReplace=memory.front();
                    memory.pop();
                    isInMemory[pageToReplace]=false;
                }
                memory.push(page);
                isInMemory[page]=true;
                cout<<"Page fault for "<<page<<endl;
            }
            else
                cout<<"Hit for "<<page<<endl;
        }
        cout<<"Page Faults:"<<pageFaults<<endl;
    }

    void LRU(){
        int pageFaults=0;
        vector<int>memory;

        for(int page:pages){
            auto it=find(memory.begin(),memory.end(),page);
            if(it==memory.end()){//page faults
                pageFaults++;
                if(memory.size()==frames){
                    memory.erase(memory.begin());
                }
                memory.push_back(page);
            }else{//hit
                memory.erase(it);
                memory.push_back(page);
            }
        }
    }

    void Optimal(){
        vector<int>memory;
        int pageFaults=0;

        for(int i=0; i<pages.size(); i++){
            int page=pages[i];
            auto it=find(memory.begin(),memory.end(),page);
            if(it==memory.end()){
                pageFaults++;
                if(memory.size()==frames){
                    int farthestIndex=-1,pageToReplace=-1;
                    for(int memPage:memory){
                        auto nextUsage=find(pages.begin()+i+1,pages.end(),memPage);
                        int dist;
                        if(nextUsage==pages.end())
                            dist=pages.size();
                        else
                            dist=distance(pages.begin(),nextUsage);

                        if(dist>farthestIndex){
                            farthestIndex=dist;
                            pageToReplace=memPage;
                        }
                    }
                    memory.erase(find(memory.begin(),memory.end(),pageToReplace));
                }
                memory.push_back(page);
            }else
                cout<<"HIT";
        }
    }
};