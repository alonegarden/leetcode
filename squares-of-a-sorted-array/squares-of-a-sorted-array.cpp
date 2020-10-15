
//

/*
    已经是排好序的， 把正负值分离出来。
    分别平方， 然后合并

*/ 

class Solution {
public:
    vector<int> merge(vector<int>& B,vector<int>& C)
    {// 用于归并2个有序向量B，C
        int bSize = B.size(); 
        int cSize = C.size();
        vector<int> A(bSize+cSize,0);

        for(int i=0,j=0,k=0; (j<bSize || k<cSize); ) {// i,j,k是A,B,C指针

            if(j<bSize && (!(k<cSize) || B[j]<C[k])) A[i++]=B[j++];
            if(k<cSize && (!(j<bSize) || B[j]>=C[k])) A[i++]=C[k++];
        }
        return A;
    }

    vector<int> sortedSquares(vector<int>& A) {
        int flag;
        int n=A.size();
        for(int i=0; i<n; i++){
            if(A[i] >= 0){
                flag = i;
                break;
            }
        }

        //然后分出来正负数向量
        vector<int> pos{A.begin()+flag, A.end()};
        vector<int> neg{A.begin(), A.begin()+flag};

        
        for(int i=0; i<pos.size(); ++i) pos[i] = pos[i]*pos[i];
        for(int i=0; i<neg.size(); ++i) neg[i] = neg[i]*neg[i];

        reverse(neg.begin(), neg.end()); // 这样才是递增序列,之后让2个递增序列merge  

        // 然后merge起来2个递增向量即可。有序向量归并是O(n)的算法
        vector<int> ans=merge(pos,neg);

        return ans;
    }
};