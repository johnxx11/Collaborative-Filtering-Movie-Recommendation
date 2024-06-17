Movie Recommendation System The Training Data
[train.txt] The training data: a set of movie ratings by 200 users (userid: 1-200) on 1000 movies (movieid: 1-1000). The format of the data is as follows: the file contains 200 blocks (users) of lines. Each line contains a triple : (U, M, R), which means that user U gives R points to movie M. In other words, U is the User ID, M is the Movie ID, and R is the corresponding rating. A rating is a value in the range of 1 to 5, where 1 is "least favored" and 5 is "most favored".
Please download the training data here: train.txt.
The Test Data
There are three test files: test5.txt, test10.txt and test20.txt.
[test5.txt] A pool of movie ratings by 100 users (userid: 201-300). Each user has already rated 5 movies. The format of the data is as follows: the file contains 100 blocks of lines. Each block contains several triples : (U, M, R), which means that user U gives R points to movie M. Please note that in the test file, if R=0, then you are expected to predict the best possible rating which user U will give movie M. The following is a block for user 276. (line 6545-6555 of test5.txt)
