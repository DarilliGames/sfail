# MONICA'S AUCTION - project IV

Full Stack Frameworks with Django Milestone Project. This project consist of a full-stack site based on centrally-owned dataset  for an auction place. This site provides an  authentication mechanism for users, so that they will be able to find, bid and purchase antique artifacts. 

This project is deployed at [Heroku](https://monica-auction.herokuapp.com/)


## UX
This website has been designed to offer the users a nice experience at acquiring antique artifacts of their interest. This auction site is targeting antique items collector users.
The visitors of this website will be able to look for artifacts based on price, age and origin. Once selected the desired criteria, a list of artifacts that fit the search criteria will be displayed. For each item, the user will be able to see a picture, the name and the item price.
After clicking on an artifact, the user will be redirected to a page where he/she would be able to know more about the object ( name, price, age, description, crafting and trajectory). If the user is interested on acquiring this item, he can bid on it or purchase it immediately for a higher price.
In order to purchase or bid, the user has to be registered and logged in.
Once the user has bought his desired products, while authenticated, he can write a review about his experience in the site. 
The owner of the site will be able to earn money through each purchase.
The user will be able to pay with credit card.

- As a user, I would like a website that displays the featured artifacts, such as the last arrived item. Then the home page of the site should display those in a place easy to locate.
 
- As a user, I may be interested in objects that come from a particular age or culture. Then the site should provide the option to filter results based on age and origin.


- As user, I may have a budget to expend, so that I am interested in looking for my item based on price. Then the side should filter items by price also.

- As a user, I may be interested in an artifact; I may find interesting how it was made, where it comes from, how old it is. Then the site should provide a picture and information about the history, origin, age, crafting and trajectory of each artifact.

- As a user, I may want to bid on an item. Then the site should provide a bidding section for each artifact, besides the user has to be authenticated before being able to bid.

- As a user, I may be pretty sure I want to acquire a special artifact, so that I dare to pay more than the bidding price to ensure the item will be mine. Then, the site should provide a mechanism that allows the user to pay a higher price to acquire the item immediately.

- As a user, I would like to pay for my purchased item, and feel secure that my card data won’t be stolen. Then the side should provide a secure payment mechanism that doesn’t expose its users to insecure situations.

- As a user, I could be interested in giving a feedback about my experience at participating at this auction site. Then the site should provide an area to display messages of users who completed their purchases process. 
 
- As a user, I would like to follow up this website through social media (twitter or instagram) so I can be updated of new recipes or to know what the community is doing. Then the website should contain link that allow the user to check its available social media.

## Features

This project works with databases collections (mongoDB Atlas). The backend of the 
project is centered in the app.py, from there are made all the routes of the priject.
The principal template of this project is the cookbook.html.  All the general html
code is donde in the base.html template, this one is shared by all the other templates
through the use of block-contents.


### Existing Features

**Apps** (backend) Here are imported all the neccesary libraries in order to make the 
caractheristics of the project work. There are a total of 24 routes, together they 
help to render templates, redirect to other template of make calculus of variables.
- Accounts app
- Artifacts app
- Bidding app
- django_forms_bootstrap3.1.0
- Routes: 
   * '/cookbook': Home website
  
**templates** There are 13 html templates. Each of them displays a different functionality
of this website.
- base: it has all the rehusable html that is share to all the other templates. Here 
 it is contained the navbar and the footer, here is added all the style-sheets and 
scripts.  The navbar allows the user to navegate through the different sections of the 
cookbook template, to check directly all recipes and/or add a new recipe. The footer
contains links to social media and copy-right text.
- cookbook: It is the home of the site.It has 5 sections
   * Home: Welcome to the website and invitation to the user to know 'what do they would like to eat today?
   
- addcategory / addcuisine / addrecipe: All of them allow to the user to add the 
 respective feature. Each template gives the option to save or cancel the action.
    * addcategory: The user is requested to write the name for the new category. The number of recipes variable is fixed to 0 automatically.

- allrecipes / recipesbycategory / recipesbycuisine / recipesbydifficulty: Display  of each criteria recipes a list  based on the number of views. The user can view, edit and/or delete the recipe. 
- editcategory / editcuisine / editrecipe: Edit the selected feature. The user can save chamges or cancel the action
- recipe: display the actual recipe.

**style** The bootstrap library was used to apply style. Besides there is the own style.
The project was made considering the "first small screen" principle, from there it
was adapted to larger sizes of screens.

**JavaScript** The project content the neccesary JS to make its components to work.
Some come from the bootstrap/ bootstrap-select functionality. There is also own JS 
to make the add/ edit recipe form works.
- Ingredients Add: jQuery that allow user to add a new ingredient to the list of ingredients
- Method Add: jQuery that allow user to add a new steep in to the method.

### Features Left to Implement
- Authentification of user, then only the registered user would be allowed to add recipes. And the site administrator would be to only one who could be able to delete or edit recipes.
- Pagination: eventually the site will gorup up and pagination for the recipes would be neccesary.
 
 
## Technologies Used

This project was made with HTML5, CSS3, JavaScript and python3. Besides those, the following tools were used:

- Language: English.
- [MongoDB Atlas](https://www.mongodb.com/)
- [Heroku](https://www.heroku.com/)
- [Jinja 2.10](http://jinja.pocoo.org/docs/2.10/)


Libraries: 
- [Bootstrap v4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/) scripts (JavaScript, jQuery and Popper.js) to get functionality in the Bootstrap's components, and css  for most of the applied style 
- [Bootstrap-Select v1.13.9](https://developer.snapappointments.com/bootstrap-select/) scripts and css to have a more interective and styled select bottom.
- [Fontawesome Version 5.9.0](https://fontawesome.com/).
- [Google Fonts](https://fonts.google.com/specimen/Charm), from here it is got the font type of the whole website ('Charm', cursive).


Own CSS style sheet. To make my own styles and overwrite some of the Bootstrap style library.
Own JavaScript file. To make the functionality of the add/remove ingredients and steeps in the method, also to change the color of the heart icom for the 'likes' .

## Testing
The whole code (html & CSS) was validated through the [Markup Validation Service](https://validator.w3.org/). The JavaScript was evaluated by [JSHint](https://jshint.com/)
The code was continuously monitored through the "Inspect" function of the Google Chrome Browser. Making sure that the website was completely responsive. The  project looks as expected in different browsers (GoogleChrome, InternetExplorer, Samsung internet).

Testing for the app.py:
1. each time a new collection was introduced, its content was corroborate through the
print function of python. Same was done while creating the diferents for's that belong 
to the routes. Example: for index, category in enumerate(categories): 
print (index,category['category_name'])
2.  navbar: all links of the navbar where manually tested.
3.  All the Searches by Category/ Cuisine / Difficulty Level give the expected result.
4.  All buttoms work as expected. 
5.  Each time the user want to add a new ingredient or steep method, the form works perfect. Same at editing.
6.  When clicking at the name of a recipe you are redirect to where you can get more infor about it.
7.  Form: if you try to submit it empty, a message telling you to fill the missing area appears.


Problems unsolved:
- origin filter

Problems solved:
- local variable 'artifact' referenced before assignment. Solved by declaring the variable at the beginning of the view and not inside the if.
- Reverse for 'checkout' with no arguments not found. 1 pattern(s) tried: ['checkout/(?P<pk>\\d+)/$']. Solved by intrucing the respective pk value together with the checkout url
- AttributeError: 'str' object has no attribute 'fields'. Solved by making sure that when passing multiple variables through the return statements so that they're accessible from the template,they were all in the same dictionary.
- Stripe was unable to pay with this car. Solved throughmaking sure the scripts for stripe were after the jquery scripts.

Problems found by the code validator and solved:
- CSS: no errors
- HTML: It is the home of the site.It has 5 sections
   *  Error: Stray end tag div. Fixed deleting the extra </div>
   *  Error: Element spam not allowed as child of element h3 in this context. The spam wasnt really neccesary, so it was taken out.
   *  Error: Duplicate ID method. Delete the duplicated ids, they resulted to be unnecessaries.

Problems found by the code validator and NO solved (HTML):

- Error: The element a must not appear as a descendant of the button element.
- Warning: The document is not mappable to XML 1.0 due to two consecutive hyphens in a comment.
- Warning: The type attribute is unnecessary for JavaScript resources.


Result of evaluation with JSHint:
- Missing semicolon. Fixed adding the respective semicolons.
- Metrics for own script located at the end of base.html: There are 5 functions in this file. Function with the largest signature take 1 arguments, while the median is 1. Largest function has 12 statements in it, while the median is 4. The most complex function has a cyclomatic complexity value of 2 while the median is 1.


## Deployment
- This project is available in Github platform under the name of  [Cookbook](https://github.com/Rasquin/cookbook)
- This project is available in Heroku  platform under the name of [ monicas-cookbook](https://git.heroku.com/monicas-cookbook.git)


- The wireframes are located in [static/wireframes/](https://github.com/Rasquin/cookbook/tree/master/static/wireframes)

- You can check this project in the next  [Link](https://monicas-cookbook.herokuapp.com/ )


## Credits
### Content
The Auction Conditions content was taken from [Heritage Auctions](https://www.ha.com/)
The artifacts information was taken from the next websites:
- [Canvas  Place de la Bastille](https://fineart.ha.com/itm/edouard-leon-cortes-french-1882-1969-place-de-la-bastille-oil-on-canvas-21-1-2-x-18-inches-546-x-457-cm-signe/a/5436-68001.s?ic4=GalleryView-ShortDescription-071515)
- [Gemstone: Chrome Tourmaline - 32.6 Cts.](https://fineart.ha.com/itm/nature-and-science/gemstone-chrome-tourmaline-326-cts-tanzania/p/5434-11086.s?ic4=GalleryView-ShortDescription-071515)
- [Gemstones: Garnet (Set of 40)](https://fineart.ha.com/itm/nature-and-science/gemstones-garnet-set-of-40-various-localities-total-40-/p/5434-11105.s?ic4=GalleryView-ShortDescription-071515)
- [A Superb Diquis Gold Figure](https://fineart.ha.com/itm/pre-columbian/a-superb-diquis-gold-figure/a/5424-70222.s?ic4=GalleryView-ShortDescription-071515)
- [A Large Diquis Gold Frog Pendant](https://fineart.ha.com/itm/pre-columbian/a-large-diquis-gold-frog-pendant/a/5424-70224.s?ic4=GalleryView-ShortDescription-071515)
- [A Tibetan Painted Wood Chest](https://fineart.ha.com/itm/asian-art/a-tibetan-painted-wood-chest-18th-19th-century-29-3-4-x-56-3-4-x-20-1-2-inches-756-x-1441-x-521-cm-/p/13152-28001.s?ic4=GalleryView-ShortDescription-071515)
- [A Large Dogon Post for Meeting House, Toguna](https://fineart.ha.com/itm/tribal-art/a-large-dogon-post-for-meeting-house-toguna/a/5424-70254.s?ic4=GalleryView-Thumbnail-071515)
- [Fourteen Louis XVI and Louis XVI-Style Giltwood and Upholstered Oval Back Side Chairs](https://fineart.ha.com/itm/furniture/fourteen-louis-xvi-and-louis-xvi-style-giltwood-and-upholstered-oval-back-side-chairs-circa-1775-and-later-33-x-22-x-21-in-total-/a/241950-21115.s?ic4=GalleryView-ShortDescription-071515)
- [6 wood panel Jean Dunand](https://fineart.ha.com/itm/furniture/jean-dunand-french-1877-1942-two-figures-six-panel-screen-circa-1928-lacquered-wood-57-3-4-x/a/5378-79039.s?ic10=FeaturedPastSalePrices-ItemImageDesc-052317&tab=ArchiveSearchResults-012417)
- [The Largest Gold Nugget from the Western Hemisfere - Boot of Cortez](https://fineart.ha.com/itm/nature-and-science/the-largest-gold-nugget-from-the-western-hemisphere-boot-of-cortez/a/5000-48202.s?ic10=FeaturedPastSalePrices-ItemImageDesc-052317&tab=ArchiveSearchResults-012417)
- [Rose Quartz . "La Madona Rosa"](https://fineart.ha.com/itm/nature-and-science/rose-quartz-la-madona-rosa-lavra-berilo-branco-sapucaia-do-norte-galileia-doce-v/a/5110-87153.s?ic10=FeaturedPastSalePrices-ItemImageDesc-052317&tab=ArchiveSearchResults-012417)
- [The Fighting Pair - Allosaurus vs Stegosaurus](https://fineart.ha.com/itm/nature-and-science/the-fighting-pair-allosaurus-vs-stegosaurus/a/6061-49071.s?ic10=FeaturedPastSalePrices-ItemImageDesc-052317&tab=ArchiveSearchResults-012417)

### Media
The photos used in this project are labelled  for reuse.
- The imagen for Good_Food_Display can be found at  [Link](https://upload.wikimedia.org/wikipedia/commons/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg)

## Acknowledgements
The brief for this project was given by Code Institute. I received inspiration for this project from my siter Aurora, who is studying to become a cook. I always wished that we had our own cookbook full of our crazy recipes that we invent during the weekends when we share on family.

[![Build Status](https://travis-ci.org/Rasquin/auction.svg?branch=master)](https://travis-ci.org/Rasquin/auction)



texto para cobdidiciones de la subastea
Heritage Auctions strives to provide as much information as possible but encourages
in-person inspection by bidders. Statements regarding the condition of objects are
only for general guidance and should not be relied upon as complete statements of 
fact, and do not constitute a representation, warranty or assumption of liability 
by Heritage. Some condition issues may not be noted in the condition report but are
apparent in the provided photos which are considered part of the condition report.
Please note that we do not de-frame lots estimated at $1,000 or less and may not be able to provide additional details for lots valued under $500. All lots are sold "AS IS" under the Terms & Conditions of Auction.