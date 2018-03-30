int makeArrayConsecutive2(std::vector<int> statues) {
    if (statues.size() > 1) {
        int miss = 0;
        //find min, max, miss = max-min+1-statues.size()
        struct pair minmax = getMinMax(statues, 0, statues.size()-1);
        cout << minmax.min << endl << minmax.max;

        miss = minmax.max - minmax.min + 1 - statues.size();
        return miss;
    }

    else {
        return 0;
    }
}


struct pair
{
  int min;
  int max;
};

struct pair getMinMax(std::vector<int> arr, int low, int high)
{
  struct pair minmax, mml, mmr;
  int mid;

  /* If there is only on element */
  if (low == high)
  {
     minmax.max = arr[low];
     minmax.min = arr[low];
     return minmax;
  }

  /* If there are two elements */
  if (high == low + 1)
  {
     if (arr[low] > arr[high])
     {
        minmax.max = arr[low];
        minmax.min = arr[high];
     }
     else
     {
        minmax.max = arr[high];
        minmax.min = arr[low];
     }
     return minmax;
  }

  /* If there are more than 2 elements */
  mid = (low + high)/2;
  mml = getMinMax(arr, low, mid);
  mmr = getMinMax(arr, mid+1, high);

  /* compare minimums of two parts*/
  if (mml.min < mmr.min)
    minmax.min = mml.min;
  else
    minmax.min = mmr.min;

  /* compare maximums of two parts*/
  if (mml.max > mmr.max)
    minmax.max = mml.max;
  else
    minmax.max = mmr.max;

  return minmax;
}
