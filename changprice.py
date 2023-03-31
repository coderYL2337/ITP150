def main():


     #hard code prod[] and price[], each with 5 values


     prod=["hat","jeans","polo","shorts","tee"]


     price=[19,55,30,25,15]


    #call changePrices() function from main(); Pass value of price[] list in main() to changePrices() function;


    #assign returned value from changePrices() to newPrice[] list


     newPrice=changePrices(price)


     print('''New Price Report


               PRODUCT   PRICE


              --------------------------''')


    #use for loop, print out each product with changed price


     for i in range(len(prod)):


         print(f"{prod[i] }    $ {newPrice[i]}")


     print("----------------------------------------")


 


#def changePrices() function;Pass value of price[] list in main() to priceN[] list in changePrices() function;


def changePrices(priceN):


     #declare countPTwo to count number of products with $2 increase, set initial value at 0


      countPTwo=0


      #declare countPFive to count number of products with $5 increase, set initial value at 0


      countPFive=0


     #for loop, check each item in the list of priceN[], and change prices


      for i in range(len(priceN)):


           #add 5 to orignal price if original price>25; add 1 to countPFive


           if priceN[i]>25:


              priceN[i]=priceN[i]+5


              countPFive+=1


           #add 2 to orignal price if original price<=25; add 1 to countPTwo


           if priceN[i]<=25:


               priceN[i]=priceN[i]+2


               countPTwo+=1


     #output countPTwo


      print(f"The number of products that increased by $2:  {countPTwo}")


      #output countPFive


      print(f"The number of products that increased by $5:  {countPFive}")


     #return changed priceN[] list from changePrices() function back to main(), assign changed price values to list of newPrice[]


      return priceN


                 


#call main


main()
