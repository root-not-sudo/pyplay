int firstDuplicate(std::vector<int> a) {
     int temp  = 0;
     for(int i = 0;i<a.size();i++)
     {
          temp = abs(a[i])-1;
          if(a[temp]<0){
               return abs(a[i]);
          }
          else{
               a[temp] = -a[temp];
          }
     }
     return -1;
}
