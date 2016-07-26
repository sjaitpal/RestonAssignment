Overview of the solution:

1. Get search string from the user
2. Call the search API based on the search string 
3. Take the first itemID to query the Product Recommendation API
4. For each of the first 10 recommended products
	a. search the Reviews API using the itemID
	b. calculate the average rating using the ratings provided by reviewers
5. Store the product name and average rating of the product in a dictionary
6. Sort the dictionary and print the product with highest rating first.

Instructions to run the code:

required python version: python2.7.5
run command : python filename.py
enter the search string : eg. ipod
expected output: descending ordered recommended products based on average ratings

 
Example:

python filename.py
ipod
output

	