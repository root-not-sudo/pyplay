bool almostIncreasingSequence(std::vector<int> sequence) {
        //if list size <= 2 then true
        //else if element i > element i+1 and element i !=element i+2 increment test by 1
        //if test > 1 then false

        if (sequence.size() <= 2) {
                return 1;
        }
        else {
                int test = 0;
                int max = sequence[0];
                for (int i = 0; i <= sequence.size()-2; i++) {
                        if (i > 1 && test > 0 && max >= sequence[i+1] && sequence[i-2] >= sequence[i]) {
                                test += 1;
                        }
                        if (sequence[i] >= sequence[i+1]) {
                                test += 1;
                        }
                        else {
                                max = sequence[i+1];
                        }

                }
                if (test > 1) {
                        return 0;
                }
                else {
                        return 1;
                }
        }
}
