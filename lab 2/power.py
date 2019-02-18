import numpy as np

def power(sample1, sample2, reps, size, alpha):
    obs = sample2.mean() - sample1.mean();
    cout = 0

    for it in range(reps):
        s1 = np.random.choice(sample1,size=size,replace=True)
        s2 = np.random.choice(sample2, size=size, replace=True)
        aux = 0
        sample = np.concatenate((sample1,sample2))

        for it in range(reps):
            s = np.random.choice(sample, size=len(sample), replace= False)
            sAux1 = s[:size]
            sAux2 = s[size:]

            perm = sAux1.mean() - sAux2.mean()

            if tperm > obs:
                aux +=1

        pval = aux/reps
        if pavl < (1-alpha) :
            count +=1
        return count / reps
