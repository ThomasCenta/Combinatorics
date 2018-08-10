This is a list of problems in combinatorics along with their solutions

<details>
<summary>(1) The number of integer solutions to x<sub>1</sub> + x<sub>2</sub> + ... + x<sub>k</sub> = r where each 
x<sub>i</sub> has a lower bound</summary>
<br>
The number of nonnegative integer solutions is (r+k-1) choose r. if x<sub>i</sub> >= l<sub>i</sub>, create new variables
<br>
y<sub>i</sub> = x<sub>i</sub> - l<sub>i</sub>
and now the solution is summing over new variables = r- sum of l<sub>i</sub>
</details>


<details>
<summary>(2) The number of r-combinations of a multiset with k infinite repetition numbers</summary>
<br>
Let S be a multiset with objects of k types, each with an infinite repetition number (or at least r). Then the number of
r-combinations of S equals
(r+k-1) choose r
</details>

<details>
<summary>(3)The number of ways to partition a finite multiset into boxes</summary>
(a) Let n be a positive integer and n<sub>1</sub>, n<sub>2</sub>, ..., n<sub>k</sub> be positive integers with 
n = n<sub>1</sub> + n<sub>2</sub> + ... + n<sub>k</sub>. The number of ways to partition a set of n objects into k 
labeled boxes in which Box 1 contains n<sub>1</sub> objects, ... Box k contains n<sub>k</sub> is
n!/(n<sub>1</sub>!* n<sub>2</sub>!* ... * n<sub>k</sub>!)

(b) If the boxes are not labeled:
n!/(k!* n<sub>1</sub>!* n<sub>2</sub>!* ... * n<sub>k</sub>!)
</details>

<details>
<summary>(4) The number of permutations of a finite multiset</summary>
Let S be a multiset with objects of k different types with finite repetition numbers n<sub>1</sub>, 
n<sub>2</sub>, ..., n<sub>k</sub> where the size of S is n = n<sub>1</sub> + n<sub>2</sub> + ... + n<sub>k</sub>. 
Find the number of permutations of S
n!/(n<sub>1</sub>* n<sub>2</sub>* ... * n<sub>k</sub>)
</details>