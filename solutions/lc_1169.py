# 1169. Invalid Transactions

# A transaction is possibly invalid if: the amount exceeds $1000 , or; if it occurs within (and including) 60 minutes of another transaction with the same name in a different city .
# You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.
# Return a list of transactions that are possibly invalid.
# You may return the answer in any order .
# Example 1: Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"] Output: ["alice,20,800,mtv","alice,50,100,beijing"] Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city.
# Similarly the second one is invalid too.
# Example 2: Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"] Output: ["alice,50,1200,mtv"]
# Example 3: Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"] Output: ["bob,50,1200,mtv"] Constraints: transactions.length <= 1000 Each transactions[i] takes the form "{name},{time},{amount},{city}" Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10 .
# Each {time} consist of digits, and represent an integer between 0 and 1000 .
# Each {amount} consist of digits, and represent an integer between 0 and 2000 .

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        sortedTransactions = {}
        invalid = []

        for transaction in transactions:
            invalidBool = False
            name, (time), (price), city = tuple(transaction.split(","))

            if(int(price) > 1000):
                invalidBool = True

            if(name not in sortedTransactions.keys()):
                sortedTransactions[name] = [(int(time), int(price), city, invalidBool)]
            else: 

                otherTransactions = sortedTransactions[name]

                for i in range (len(otherTransactions)):
                    trans = otherTransactions[i]

                    timeDiff = abs(int(time)-int(trans[0]))
                    if(timeDiff <= 60 and city != trans[2]):
                        otherTransactions[i] = (trans[0], trans[1], trans[2], True)  
                        invalidBool = True

                sortedTransactions[name].append((int(time), int(price), city, invalidBool))
                sortedTransactions[name].sort()   

        print(sortedTransactions)

        for name in sortedTransactions.keys():
            transactionList = sortedTransactions[name]
            for transaction in transactionList:
                if transaction[3] == True:
                    invalid.append(f"{name},{transaction[0]},{transaction[1]},{transaction[2]}")


        return list((invalid))
        print(sortedTransactions)