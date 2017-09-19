Amadon

Topics
-Session and Post Handling
-Mixing post handling with html render - why this should be avoided
-Basic security - why you should be careful about what you put inside <form>

You've decided to build your own e-commerce site called Amadon and decide to make this into a Django app.  Without creating anything in the database (which you'll learn later), have the app remember what items you've purchased so far.  

Once your customer bought the item, say your customer reloaded the page.  Would your customer be happy if your app re-orders the same product and charges his/her credit card again?  Probably not!  Make sure your app doesn't charge the card again when the customer reloads the 'checkout' page ('checkout' page defined as localhost/amadon/checkout where they see a thank you message).