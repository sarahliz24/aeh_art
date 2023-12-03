# Testing

- [Testing](#testing)
    - [Authentication](#authentication)
    - [Home](#home)
    - [Shop](#shop)
    - [Product Details](#product-details)
    - [Shop Info](#shop-info)
    - [Discover](#discover)
    - [Contact](#contact)
    - [Newsletter & Newsletter Details](#newsletter-&-newsletter-details)
    - [Wishlist](#wishlist)
    - [Profile](#profile)
    - [Artwork CRUD](#artwork-crud)
    - [Newsletter CRUD](#newsletter-crud)
    - [Shopping Bag](#shopping-bag)
    - [Checkout](#checkout)
    - [CSS Testing](#css-testing)
    - [Javascript Testing](#javascript-testing)
    - [Flake8 Python Testing](#flake8-python-testing)
    - [Other](#other)

Accessibility testing was performed regularly throughout development utilising 'WAVE Web Accessibility Evaluation Tools', using this link: [WAVE Testing](https://wave.webaim.org/).

Responsiveness testing was performed using chrome inspector during development, and towards the end of development responsiveness testing was also performed on a variety of "real life" peronal and desktop devices.

Lighthouse testing was conducted at regular intervals during development, using the Lighthouse function inbuilt into the Chrome Inspector tool.

The code was regularly tested using w3c validators for HTML and CSS throughout development, using these links:
[W3C HTML Validator](https://validator.w3.org/#validate_by_input);
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

Python testing was conducted using Flake8 from the console (enter console command: 'python3 manage.py flake8' to run).

Extensive manual testing was performed during at and end of development.

Testing is further detailed below:

## Authentication

### Authentication Testing 1 - User Status

| **User status** | **Can  register** | **Can login** | **Can logout** | **Can recover password** | **Can access wishlist** | **Can access public pages** | **Can access my profile** | **Can add, edit & delete newsletters** | **Can add, edit & delete artwork** | **user story** |
|---|---|---|---|---|---|---|---|---|---|---|
| **Super user** | no | yes | yes | yes | yes | yes | yes | yes | yes | 10, 11, 12, 14, 20, 24, 27, 28, 29, 34 |
| **Registered user** | no | yes | yes | yes | yes | yes | yes | no | no | 10, 11, 12, 14, 20, 24 |
| **Non\-registered user** | yes | no \(sent to sign\-up page\) | n/a | n/a | no | yes | no | no | no | 10 |

### Authentication Testing 2 - User Actions

| Feature | Action | Expected Result | Actual Result | User Story |
|---|---|---|---|---|
| Log In | User who is not logged in selects login from account dropdown | Log in page loads | pass | 11 |
| Log In | User logs in | Success toast displays to confirm user is now logged in  | pass | 11 |
| Log In | User who is not registered selects login from account dropdown | option on log in page to go to sign up loads sign up page when clicked | pass | 10 |
| Log Out | User selects log out from   account dropdown | sign out confirmation page loads - cancel button returns user to home page (remains logged in); selecting sign   out button logs user out with toast message to confirm log out   successful  | pass | 11 |
| Sign Up | user completes signup form with   valid information | verify email address page loads, user can enter details | pass | 10, 13 |
| Password Recovery | user clicks 'forgot password' on login page | password reset page loads, user recieves email with reset link.  Reset link works, password can be successfully changed  | pass | 12 |

## Home

| Feature | Action | Expected Result | Actual Result (Desktop) | Actual Result (Mobile) | User Story |
|---|---|---|---|---|---|
| Logo | user clicks on logo | Home page loads  | pass | pass |  |
| Search bar | user enters desired search term | Products page load, number of products with search term displayed, products containing search term   displayed.  User can sort products   using sort filter.  | pass | pass | 7, 8 |
| Search bar | reset button | Button turns yellow on hover, Search cleared, all artwork displayed | pass | pass | 7, 8 |
| Search bar | user enters search term that doesn't exist within products | Products page load, number of products with search term displayed=0, no products displayed.  | pass | pass | 7, 8 |
| nav bar   links - Home, Discover, Contact, Newsletter | user clicks on link | Link turns yellow on hover.  Relevant page loads.   | pass | pass | 23 |
| nav bar   links - Shop | User clicks on link. Dropdown   opens. User can click on desired dropdown option (All, Landscapes, Soil   Profiles, Other). |  Relevant page loads (filtered by category if   relevant) | pass | pass |  |
| nav bar   links - Account | Superuser: | Add Artwork, Add Newsletter, My   Profile, My wishlist, Logout links displayed.  Relevant page loads when clicked. | pass | pass | 14, 24 |
|  | Registered User: | My Profile, My wishlist, Logout links displayed.  Relevant page loads   when clicked. | pass | pass | 14, 24 |
|  | Unregistered User: | Signup & Login links displayed.  Relevant page loads when   clicked. | pass | pass |  |
| Nav bar | Responsive test | Collapses responsively | pass | pass (expands responsively) |  |
| Shopping   bag icon, Shopping bag total | All users | Shopping Bag page loads.   | pass | pass | 15, 17 |
|  | Items added to shopping bag | Total spend tally is displayed accurately next to shopping bag | pass | pass | 15 |
| Hero   text | user clicks on hero text | Link turns yellow on hover. Shop page loads (All artwork). | pass | pass |  |
| Hero   images | user clicks on any hero image | Link turns yellow on hover. Shop page loads (All artwork). | pass | pass |  |
| Banner   text | User clicks on 'Shop now' text | Shop page loads (All artwork). | pass | pass |  |
|  | User clicks on 'Discover' text | Link turns yellow on hover. Discover page loads. | pass | pass |  |
| Footer -  Social | User clicks on 'Facebook' icon or 'Follow us on facebook' button | AEH Art facebook page opens in   new tab.  | pass | pass |  |
| Footer -  Site Links | user clicks on link |  Relevant page loads. | pass | pass |  |
| Footer -  Documents & Policies | user clicks on link |  Relevant information opens in a new   tab.  |  Relevant information opens in a new tab.  |  Relevant information opens in a new   tab.   |  |
| Footer -   Mail Chimp | User enters invalid email address | warning generated to user | pass | pass | 31 |
|  | User enters email address already used to signup for Mailchimp on this site | alert generated to user | pass | pass | 31 |
|  | user enters valid email address | Success message to user | pass | pass | 31 |
|  |  | User details added to mailchimp dashboard | pass | pass | 31 |
| Footer -  linkedin | user clicks on link | Site creators linkedin page opens in new tab.  | pass | pass |  |
| Contact email | user looks for contact email address for site | contact email is present on footer | pass | pass | 30 |

### W3C HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/home_html_checker.png">
</details>

### Wave Accesibility checker
* No significant errors.
<details><summary>Home Page Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/wave_home_page.png">
</details>

Two errors were flagged on wave testing.  As they are nav/footer related they are shown on all wave testing site-wide.
1. Missing form label.  This is within the mailchimp sign-up code, and relates to a duplicate empty form that is present to screen for form bot sign-ups.  I therefore did not amend this code, and the warning is present on every wave page tested due to it's location in the footer. 
2. Very low contrast warning.  This warning is picking up on a sr-only span that has both it's color and background color set to black - it is not intended to be visible to the sighted user, therefore I have not amended it.
<br>

### Lighthouse Testing

<details><summary>Home Page (Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/lighthouse_desktop_home.png">
</details>
<details><summary>Home Page (Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/lighthouse_mobile_home.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for mobile loading would help to improve performance.
<br>
</details>

## Shop

| Feature | Action | Expected Result | Actual Result | User Story |
|---|---|---|---|---|
| Categories   filter | User clicks to view dropdown list of available categories | Categories turns yellow.  Dropdown list appears, all links active | pass | 5, 9 |
|  | User chooses a category from   dropdown list | Filtered list of artwork within   that category is displayed.   | pass | 5, 9 |
|  | Products counter | On right of screen the number of products available in that category is displayed. | pass | 8 |
|  | Reset' button | All artwork displayed. Counter displays total number of products. | pass | 5 |
| Page   heading | - | Page heading defaults to 'Artwork' & displays all artwork | pass | 1 |
| View | User can view artwork | Artwork is displayed on shop page |  | 1 |
| Page heading | User chooses a category from   dropdown list | Page heading updates to include category depending on category chosen e.g. 'Artwork - Soil Profiles' | pass |  |
| Sort   filter | User selects from dropdown list   of available sort fuctions | products currently displayed are sorted on screen as per the sort function.  | pass | 3, 5, 6 |
| Reponsive   testing | - | Page is fully responsive | Minor layout  issue noted on screen sizes less than 385px  wide (column not centered) |  |
| Up arrow | User clicks on up arrow | Arrow is underlined. Scroll returns to top of screen | pass |  |
| Product image | User clicks product image | product details page loads for   intended product | pass | 2 |
| Product   title | User clicks product title | product details page loads for   intended product | pass | 2 |
| Category   tag | User clicks on category tag | Category filter is applied and   all artwork in that category is displayed | pass | 5, 9 |

### W3C HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/shop_html.png">
</details>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/shop_wave.png">
</details>

Two errors were flagged on wave testing as per the Home Page wave testing.

### Lighthouse Testing

<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/lighthouse_shop_desktop.png">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/lighthouse_shop_mobile.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>

## Product Details

| Feature | Action | Expected Result | Actual Result | User Story |
|---|---|---|---|---|
| Categories   filter | User clicks to view dropdown list of available categories | Categories turns yellow.  Dropdown list appears, all links active | pass | 5, 9 |
|  | User chooses a category from dropdown list | Filtered list of artwork within   that category is displayed.  | pass | 5, 9 |
|  | Products counter | On right of screen the number of products available in that category is displayed. | pass | 8 |
|  | Reset' button | All artwork displayed. Counter displays total number of products. | pass | 5 |
| Page   heading | - | Page heading defaults to 'Artwork' & displays all artwork | pass | 1 |
| View | User can view artwork | Artwork is displayed on shop page |  | 1 |
| Page   heading | User chooses a category from   dropdown list | Page heading updates to include category depending on category chosen e.g. 'Artwork - Soil Profiles' | pass |  |
| Sort filter | User selects from dropdown list of available sort fuctions | products currently displayed are sorted on screen as per the sort function.  | pass | 3, 5, 6 |
| Reponsive testing | - | Page is fully responsive | Minor layout  issue noted on screen sizes less than 385px   wide (column not centered) |  |
| Up arrow | User clicks on up arrow | Arrow is underlined. Scroll returns to top of screen | pass |  |
| Product image | User clicks product image | product details page loads for intended product | pass | 2 |
| Product title | User clicks product title | product details page loads for intended product | pass | 2 |
| Category   tag | User clicks on category tag | Category filter is applied and all artwork in that category is displayed | pass | 5, 9 |

### W3C HTML Validator
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/product_details_html.png">
</details>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/product_details_wave.png">
</details>
Two errors were flagged on wave testing as per the Home Page wave testing.

### Lighthouse Testing

<details><summary>Product Details (Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/lighthouse_prodcut_details_desktop.png">
</details>
<details><summary>Product Details (Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/lighthouse_prodcut_details_mobile.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>


## Shop Info

| Feature | Action | Expected Result | Actual Result | User Story |
|---|---|---|---|---|
| Up arrow | User clicks on up arrow | Arrow is underlined.  Scroll returns to top of screen | pass |  |
| Links - category names at start of  relevant paragraphs | User clicks on name |  | pass |  |
| FAQs | User clicks on FAQ | Text changes colour on hover.  Accordian opens to view FAQ detail. | pass | 35, 36 |
| FAQs | User clicks on FAQ again | FAQ closes | pass | 35, 36 |
| Reponsive  testing | - | Page is fully responsive | pass |  |

### W3C HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/shop_info_html.png">
</details>

### Wave Accessibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/wave_shop_info.png">
</details>
Two errors were flagged on wave testing as per the Home Page wave testing. 

### Lighthouse Testing

<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/shop_info_lighthouse_desktop.png">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/shop_info_lighthouse_mobile.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
</details>

## Discover

| Feature | Action | Expected Result | Actual Result | User Story |
|---|---|---|---|---|
| Discover |  |  |  | 23, 32 |
| Find out more' links | User clicks on link | Text changes colour on hover.   Relevant info page loads. | pass | 23, 32 |
| Up arrow  - All 4 pages (discover, artist, scientist, human) | User clicks on up arrow | Arrow is underlined.  Scroll returns to top of screen | pass |  |
| Reponsive  testing - All 4 pages (discover, artist, scientist, human) |  | All pages are fully responsive | pass |  |
| buttons  - All 4 pages (discover, artist, scientist, human) | user clicks home/back buttons | Text changes colour on hover.  Relevant info page loads. | pass | 23, 32 |
| Scientist | user clicks publications/award buttons  | Text changes colour on hover.   Relevant info page loads. | pass | 23, 32 |
| Publications | User can view publications | User can view publications | pass | 23, 32 |
| pagination | user clicks page number | Text changes colour on hover. New page of publications loads. | pass |  |
| DOI | user clicks DOI link | Text changes colour on hover. Each link tested, and each opens linked article on a new tab. | pass |  |
| Awards | User can view awards | User can view awards | pass | 23, 32 |
| pagination | user clicks page number | Text changes colour on hover. New page of publications loads. | pass |  |

### W3C HTML checker
* no errors
<details><summary>Discover W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/discover.html.png">
</details>
<details><summary>Artist W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/awards_html.png">
</details>
<details><summary>Human W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/html_human.png">
</details>
<details><summary>Scientist W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/scientist_html.png">
</details>
<details><summary>Awards W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/awards_html.png">
</details>
<details><summary>Publications W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/publications_html.png">
</details>

### Wave Accesibility checker
* No significant errors.
<details><summary>Discover Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/discover_wave.png">
</details>
<details><summary>Artist Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/artist_wave.png">
</details>
<details><summary>Scientist Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/scientist_wave.png">
</details>
<details><summary>Human Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/wave_human.png">
</details>
<details><summary>Awards Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/awards_wave.png">
</details>
<details><summary>Publications Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/publications_wave.png">
</details>

Two errors were flagged on wave testing as per the Home Page wave testing. 

### Lighthouse Testing

<details><summary>Discover (Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/discover_lighthouse_desktop.png">
</details>
<details><summary>Discover (Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/discover_lighthouse_mobile.png">
</details>
<details><summary>Artist (Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/artist_lighthouse_desktop.png">
</details>
<details><summary>Artist (Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/artist_lighthouse_mobile.png">
</details>
<details><summary>Scientist(Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/scientist_lighthouse_desk.png">
</details>
<details><summary>Scientist(Mobile) Lighthouse Testing</summary>
    <img src="">
</details>
<details><summary>Human (Desktop) Lighthouse Testing</summary>
    <img src="">
</details>
<details><summary>Human (Mobile) Lighthouse Testing</summary>
    <img src="">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>

## Contact

| Feature | Action | Expected Result | Actual Result | User Story |
|---|---|---|---|---|
| Up arrow | User clicks on up arrow | Arrow is underlined.  Scroll returns to top of screen | pass |  |
| Buttons | user clicks home/back buttons | Text changes colour on hover.  Relevant page loads. | pass |  |
| User enters details | invalid details entered | warning to user | pass | 30 |
| User | enters valid details | success toast | pass |  |
|  |  | user receives email to nominated email inbox confirmed message sent, with copy of message | pass | 30 |
| Registered user | form is pre-populated with user   details | user can submit with   pre-populated details or amend to any other valid input | pass | 30 |
| Reponsive   testing |  | Page is fully responsive | pass |  |

<details><summary>Email to user to confirm contact message sent</summary>
    <img src="/workspace/aeh_art/assets/readme/images/contact_user_email.png">
</details>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/contact_wave.png">
</details>

Two errors were flagged on wave testing as per the Home Page wave testing. 

### Lighthouse Testing
<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/lighthouse_desk_contact.png">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/lighthouse_mob_contact.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>

## Newsletter & Newsletter Details

| Feature | Action | Expected Result | Actual Result | User Story |
|---|---|---|---|---|
| Intro to newsletter detail | User views newsletter page | User can see truncated version   of each newsletter detail | pass | 37 |
| Up arrow | User clicks on up arrow | Arrow is underlined. Scroll returns to top of screen | pass |  |
| Read   more' links | user clicks link | Text changes colour on hover. Newsletter detail page loads. | pass | 37 |
| Reponsive   testing |  | All pages are fully responsive | pass |  |
| Newsletter detail | / | / | / | / |
| buttons | user clicks home/back buttons | Text changes colour on hover. Relevant page loads. | pass | 37 |

### W3C HTML checker
* no errors
<details><summary>Newsletter W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/newsletter_html.png">
</details>
<details><summary>Newsletter Detail W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/news_detail_html.png">
</details>

### Wave Accesibility checker
* No significant errors.
<details><summary>Newsletter Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/newsletter_wave.png">
</details>
<details><summary>Newsletter Detail Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/news_detail_wave.png">
</details>

Two errors were flagged on wave testing as per the Home Page wave testing. 

### Lighthouse Testing
<details><summary>Newsletter (Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/newlsetter_desk_lighthouse.png">
</details>
<details><summary>Newsletter (Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/newlsetter_mob_lighthouse.png">
</details>
<details><summary>Newsletter Detail (Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/lighthouse_news_details.png">
</details>
<details><summary>Newsletter Detail (Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/lighthouse_news_details_mob.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
</details>

## Wishlist

| Feature | Action | Expected Result | Actual Result | User Story |
|---|---|---|---|---|
| Up arrow | User clicks on up arrow | Arrow is underlined.  Scroll returns to top of screen | pass |  |
| Links -   category names at start of relevant paragraphs | User clicks on name |  | pass |  |
| Wishlist   (on product details page) | Unregistered user clicks add to wishlist icon | Sign-in page loads | pass | 24 |
|  | Registered user clicks add to   wishlist icon | Success toast displayed confirming specific product title has been added to wishlist | pass | 24, 25 |
|  | Registered user clicks remove from wishlist icon | Info toast displayed confirming   specific product title has been removed from wishlist. Wishlist page loads. | pass | 25, 26 |
| Wishlist Page | Wishlist view | Items added to wishlist are  displayed (image, title, description, price, date added) & remove icon | pass | 24, 25 |
|  | Remove icon - user clicks | Info toast displayed confirming specific product title has been removed from wishlist.  Item is removed from wishlist user display.   Wishlist page reloads. | pass | 25, 26 |
|  | Back button | Text changes colour on hover. All products page loads (shop). | pass |  |
| Reponsive testing |  | All pages are fully responsive | user must scroll horizontally on  screen size less than 410 px wide |  |

### W3C HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/wishlist_html.png">
</details>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/wish_wave.png">
</details>

Two errors were flagged on wave testing as per the Home Page wave testing. 

### Lighthouse Testing

<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/wish_desk_light.png">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/wish_mob_light.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
</details>

## Profile

| Feature | Action | Expected Result | Actual Result | User Story |
|---|---|---|---|---|
| Up arrow | User clicks on up arrow | Arrow is underlined.  Scroll returns to top of screen | pass |  |
| Unregistered   user | cannot access | returns 404 page if entered into   URL | pass |  |
| Registered   User |  |  |  |  |
| Default delivery info | data fields for name, address   etc visible, with helper text if no entry | pre-populated information from database | pass | 10, 14 |
| Update   button | user clicks button | Text changes colour on hover. Info toast shown to confirm update successful. | pass |  |
| Order history | Previous orders (if any) are displayed | Order number, date, items and   total displayed |  | 10, 14 |
|  | no previous orders | no orders are displayed | pass |  |
| Order history details | Click on order number | Text changes colour on hover.   Individual order event details displayed. Toast to inform user this is a previous order is displayed. | pass | 10, 14 |
|  | user clicks back button | Text changes colour on hover. Profile page loads.  | pass |  |

### W3C HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/profile_html.png">
</details>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/profile_wave.png">
</details>

The same error was flagged across 7 fields in the update details section - there is no form label on the fields for screen readers. I did not amend as the form is automatically generated from the model. This will be amended in a future release. 

### Lighthouse Testing

<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/profile_desk_wave.png">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/profile_mob_wave.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
</details>

## Artwork CRUD

| Feature | Action | Expected Result | Actual Result | User Story |
|---|---|---|---|---|
| Up arrow | User clicks on up arrow | Arrow is underlined. Scroll returns to top of screen | pass |  |
| Unregistered user | cannot access artwork CRUD | returns 404 page if entered into   URL | pass |  |
| Registered   User | cannot access artwork CRUD |  |  |  |
| Superuser | Can access artwork CRUD |  |  |  |
| Reponsive testing |  | All pages are fully responsive | pass |  |
| Add   Artwork | add artwork only appears in account menu for superuser | unregistered user tries to enter   via url - 404 page returned | pass |  |
|  | add artwork only appears in account menu for superuser | registered user tries to enter   via url - toast error message to inform only for authorised users | pass | 27 |
|  | user enters invalid information into any field | warning text generated &   submission does not proceed | pass |  |
|  | user enters valid information into all fields | Artwork added. Toast info message to confirm successful add displayed. Relevant product details page loads. | pass |  |
|  | Cancel button selected | All products page loads. | pass |  |
| Edit Artwork | Edit artwork only appears in   account menu for superuser | unregistered user tries to enter via url - 404 page returned | pass | 28 |
|  | Edit artwork only appears in account menu for superuser | registered user tries to enter via url - toast error message to inform only for authorised users | pass | 28 |
|  | Superuser accesses add artwork from product card | Edit artwork page loads.  Toast shows to inform user of name of artwork they are about to edit. | pass | 28 |
|  | user enters invalid information   into any field | warning text generated &   submission does not proceed | pass |  |
|  | user enters valid information into all fields | Artwork amended.  Toast info message to confirm successful update displayed. Relevant product details page loads. | pass | 27 |
|  | Cancel button selected | All artwork page loads. | pass |  |
|  | Remove image ticked | image is removed & replaced with 'no image' icon. Info toast to confirm displayed. | pass | 28 |
|  | Image button selected | Text changes colour on hover. File upload window opens.  Text appears to advise of file name for upload. Selecting edit artwork button successfully   adds image. | pass | 28 |
| Delete Artwork | Superuser clicks delete button on artwork card | modal appears - queries user if they really want to delete item (specifies name of particular item).  | pass | 29 |
|  | Superuser clicks cancel on warning modal | Returns to page, no changes made | pass | 29 |
|  | Superuser clicks delete on warning modal | Artwork deleted. Success toast displays to confirm deletion. | pass | 29 |

### W3C HTML checker
* no errors
<details><summary>Add Artwork W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/add_artwork_html.png">
</details>
<details><summary>Edit Artwork W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/edit_artwork_html.png">
</details>

### Wave Accesibility checker
* No significant errors.
<details><summary>Add Art Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/add_artwork_wave.png">
    There is new error on this page - the select image button does not have a form label.  This button's behaviour is controlled by a widget and javascript.  I added an aria-label to improve but this was not effective, and I did not want to cause issue with the functioning of the button.  This would be addressed in a future release.
</details>
<details><summary>Edit Art Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/edit_art_wave.png">
    Second error as above.
</details>

### Lighthouse Testing
<details><summary>Add Art (Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/add_artwork_light_desk.png">
</details>
<details><summary>Add Art (Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/add_artwork_light_mob.png">
</details>
<details><summary>Edit Art (Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/edit_artwork_light_desk.png">
</details>
<details><summary>Edit Art (Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/edit_artwork_mob_light.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
</details>

## Newsletter CRUD

| Feature | Action | Expected Result | Actual Result | User Story |
|---|---|---|---|---|
| Up arrow | User clicks on up arrow | Arrow is underlined.  Scroll returns to top of screen | pass |  |
| Reponsive   testing |  | All pages are fully responsive |  |  |
| Add   Newsletter | add Newsletter only appears in   account menu for superuser | unregistered user tries to enter   via url - 404 page returned | pass | 34 |
|  | add Newsletter only appears in account menu for superuser | registered user tries to enter via url - toast error message to inform only for authorised users | pass | 34 |
|  | superuser enters invalid information into any field | warning text generated &   submission does not proceed | pass | 34 |
|  | superuser enters valid   information into all fields | Artwork added.  Toast info message to confirm successful add displayed. Newsletters page loads. | pass | 34 |
|  | Cancel button selected | Newsletters page loads. | pass |  |
| Edit Newsletter | Edit newsletter only appears in   account menu for superuser | unregistered user tries to enter via url - 404 page returned | pass | 34 |
|  | Edit newsletter only appears in account menu for superuser | registered user tries to enter via url - toast error message to inform only for authorised users | pass | 34 |
|  | Superuser accesses Edit   newsletter from account dropdown | Edit newsletter page loads. Toast shows to inform user of name of artwork they are about to edit. | pass | 34 |
|  | user enters invalid information into any field | warning text generated &   submission does not proceed | pass | 34 |
|  | user enters valid information into all fields | Newsletter added. Newsletter detail page loads so user can review edits if needed. | pass | 34 |
|  | Cancel button selected | Newsletters page loads. | pass |  |
| Delete Newsletter | Superuser clicks delete button on artwork card | modal appears - queries user if they really want to delete newsletter (specifies name of particular   newsletter).  | pass | 34 |
|  | Superuser clicks cancel on warning modal | Returns to page, no changes made | pass | 34 |
|  | Superuser clicks delete on   warning modal | Newsletter deleted. Success toast displays to confirm deletion. | pass | 34 |
|  | Home button clicked | Button changes colour on hover.  Home page loads. | pass |  |

### W3C HTML checker
* no errors
<details><summary>Add Newsletter W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/add_news_html.png">
</details>
<details><summary>Edit Newsletter W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/edit_news_html.png">
</details>

### Wave Accesibility checker
* No significant errors.
<details><summary>Add Newsletter Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/add_news_wave.png">
</details>
<details><summary>Edit Newsletter Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/edit_news_wave.png">
</details>

### Lighthouse Testing

<details><summary>Add Newsletter (Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/add_news_light_desk.png">
</details>
<details><summary>Add Newsletter (Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/add_news_light_mob.png">
</details>
<details><summary>Edit Newsletter (Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/edit_news_desk_light.png">
</details>
<details><summary>Edit Newsletter (Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/edit_news_mob_light.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
</details>

## Shopping Bag

| Feature | Action | Expected Result | Actual Result | User Story |
|---|---|---|---|---|
| Up arrow | User clicks on up arrow | Arrow is underlined. Scroll returns to top of screen | pass |  |
| Reponsive   testing |  | All pages are fully responsive | pass |  |
| Any user | user clicks shopping bag icon or shopping bag total numerical display | shopping bag page loads | pass | 15 |
|  | Bag displays each item in bag (image, title, artwork id, quantity, price, subtotal) |  | pass | 15, 17 |
|  | Grand total is displayed correctly |  | pass | 15 |
|  | free delivery threshold is calculated and display to user how much more to spend to qualify |  | pass |  |
|  | User clicks  keep shopping button | all products page loads | pass |  |
|  | User clicks  keep checkout  button | checkout page loads | pass |  |
|  | User clicks + or - on quantity selector  |  | pass |  |
| Quantity selector | Default | Defaults to number of items chosen at product details stage | pass | 16 |
|  | User clicks +/- button | Value increments or decrements accordingly, cannot go smaller than 1 | pass | 16, 18 |
|  |  |  | pass |  |
|  | User enters number manually into quantity box outside accepted range (0 or less) & clicks udpate total | 500 error page displayed with button to return to home page | pass | 16 |
|  | User clicks update total with valid quantity entry |  |  | 16 |
|  | User clicks add to bag | bag updated with amount user has selected. Success message displays  with bag summary & link to checkout | pass |  |
|  | User clicks changes quantity and clicks add to bag | bag updated to show amount user  has selected for that item.  Succesmessage displays with bag summary & link to checkout | pass | 15, 17, 18 |
|  | User clicks 'remove item' | item removed from bag and grand   total recalculates accordingly | pass | 15, 18 |
|  | User clicks 'secure checkout' button | checkout page loads | pass | 20 |
|  | User clicks 'keep shopping' button | button changes colour on hover.  All artwork page loads. | pass |  |

### W3C HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/media/bag_html.png">
</details>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/bag_wave.png">
</details>

### Lighthouse Testing
<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/bag_desk_light.png">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/bag_mob_light.png">
</details>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>

## Checkout

| Feature | Action | Expected Result | Actual Result | User Story |
|---|---|---|---|---|
| Reponsive   testing |  | All pages are fully responsive |  |  |
| Any user | Order summary displayed | User can view bag contents (iten, title, quantity, subtotal, delivery fee, grand total) &   calculations are correct | pass |  |
|  | Order summary displayed | free delivery threshold is calculated and display to user how much more to spend to qualify | pass |  |
|  | User clicks  keep shopping button | all products page loads | pass |  |
|  | User clicks  keep checkout  button | checkout page loads | pass |  |
|  | User enters invalid details into   order information | warning text appears to prompt   user, form does not submit | pass |  |
| Unregistered user | options to create account or login given to save entered information | create account link loads sign up page, login link loads login page | pass | 14 |
| Registered user | Form is pre-populated with user details from database | User can amend details (as long as valid entries) or keep same and successfully submit form | pass |  |
|  | user ticks 'save details to profile' | profile is updated with revised details upon form submission  | pass | 14 |
| Any user | user enters cards details for payment | invalid details prompt warning text to user to explain the issue | pass | 19 |
|  | user enters cards details for   payment | valid details entered - loading spinner while processing | pass | 19 |
|  | User clicks 'adjust bag'  | shopping bag page reloads | pass | 18 |
|  | successful order | success toast displayed with   order number, and confirmation email advice. Order details displayed on   screen. | pass | 20, 21 |
|  | successful order - user clicks 'browse products' button | all artwork page loads | pass |  |
|  | successful order | Order confirmation email generated & sent to users nominated email address | pass | 22 |

Payment tests
*
<details><summary></summary>
    <img src="">
</details>
* Order email sent to customer after successful purchase
<details><summary></summary>
    <img src="/workspace/aeh_art/assets/readme/images/order_success_email.png">
</details>
* Order successful on stripe dashboard
<details><summary>Stripe payment succeeded</summary>
    <img src="/workspace/aeh_art/assets/readme/images/stripe_payment_succeeded.png">
</details>

### W3C HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/checkout_html.png">
</details>

### Wave Accesibility checker
*   Form label errors on this page - the form fields sdo not have adequate accessiblity labels.  This will be addressed in a future release.
<details><summary>Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/checkout_wave.png">
</details>

### Lighthouse Testing
<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/checkout_wave_desk.png">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/checkout_wave_mob.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
</details>

## CSS Testing
* All CSS files were tested using the W2C CSS Validator, with no issues.
<details><summary>Base CSS</summary>
    <img src="/workspace/aeh_art/assets/readme/images/css_base.png">
</details>
<details><summary>Checkout CSS</summary>
    <img src="/workspace/aeh_art/assets/readme/images/css_checkout.png">
</details>
<details><summary>Pages CSS</summary>
    <img src="/workspace/aeh_art/assets/readme/images/css_pages.png">
</details>
<details><summary>Profiles CSS</summary>
    <img src="/workspace/aeh_art/assets/readme/images/css_profiles.png">
</details>

## Javascript Testing
All Javascript was testing using Jshint - no errors.
<details><summary> Remove item from bag JShint Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/jshint remove item bag .png">
</details>
<details><summary>Update quantity bag JShint Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/jshint update quantity bag.png">
</details>
<details><summary> JShint Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/jshint_add_product_new_image.png">
</details>
<details><summary>Base JShint Testing</summary>
     <img src="/workspace/aeh_art/assets/readme/images/jshint_base.png">
</details>
<details><summary>Quantity Input Script JShint Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/jshint_quantity_input_script.png">
</details>
<details><summary>Sort selector products JShint Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/jshint_sort_selector_products_pg.png">
</details>
<details><summary>Stripe Elements JShint Testing</summary>
     <img src="/workspace/aeh_art/assets/readme/images/jshint_stripe_elements.png">
</details>
* There was one unedifned variable noted in the Stripe Elements test, however I have not amended this as it relates to the Stripe API function, and is not affecting performance.
<details><summary>Up arrow JShint Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/jshint_up_arrow.png">
</details>

## Flake8 Python Testing
Flake 8 testing was performed in the console.  Results were clear with migrations excluded.  Testing with migrations included shows only migration files with alerts (which can be ignored).
<details><summary>Flake8 excluding migrations Testing</summary>
     <img src="/workspace/aeh_art/assets/readme/images/flake8.png">
</details>
<details><summary>Flake8 including migrations Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/flake8wMigrations.png">
</details>

## Other

* All external links have 'rel' attributes; set to noreferrer and noopener. 

* Mailchimp - tested and fully functional
<details><summary>Email to user after suscribing via Mailchimp</summary>
    <img src="/workspace/aeh_art/assets/readme/images/mailchimp_subscribers.png">
</details>
