# Testing

- [Testing](#testing)
  * [User Story Tests](#user-story-tests)
+ [Manual Testing](#manual-testing)
    - [Home](#home)
    - [Products](#products)
    - [Product Detail](#product-detail)
    - [Product Management](#product-management)
    - [Shopping Bag](#shopping-bag)
    - [Checkout](#checkout)
    - [Shop Info](#shop-info)
    - [Wishlist](#wishlis)
    - [Discover](#discover)
    - [Contact](#contact)
    - [Newlsetter](#newsletter)
    - [Profile](#profile)
    - [Other](#other)

## Manual Testing

## Home

<details>

<summary>
Home Page Testing</summary><br>

Related templates:

* base.html
* main-nav.html
* mobile-top-header.html
* index.html
* footer.html

Links - direct to the correct URL and external links open in new tabs
clicking logo sends user to home page (mobile and desktop), hover on logo shows coloured underlines (indicating a live link function to user)
all buttons send user to described pages and turn yellow on hover
facebook icon and "follow us on facebook" button direct user to site facebok page (if facebook user is logged in), Rel attributes are set as noreferrer and noopener for external links.

Dropdowns
Search function - mobile & desktop works the same either way, takes user to products page, displays all related products, and number of products found.  reset button rests to full product list.
Responsive nav
Footer
all links take user to described page
copyright link opens copyright notice image in new tab
privacy policy and terms & conditions links opn PDFs in a new tab
linkedin link sends user to site creators linkedin profile (opens in new tab), rel attributes are set
Mailchimp signup - entering email address already registered produces warning message, entering an invalid email address produces an error message, entering valid email produces success message, suscribers successfully recorded in mailchimp dashboard

Account status & access rights
if not logged in
Hero images

<br>

| Auth Status     | Can Register | Can Login | Can Logout | Products Links | Hire Links | Nav/Footer Links | Profile Access | Product Management Access | Wishlist Access |
|-----------------|--------------|-----------|------------|----------------|------------|------------------|----------------|----------------------------|-----------------|
| Admin           | no/pass      | no/pass   | yes/pass   | yes/pass       | yes/pass   | yes/pass         | yes/pass       | yes/pass                   | yes/pass        |
| Registered User | no/pass      | no/pass   | yes/pass   | yes/pass       | yes/pass   | yes/pass         | yes/pass       | no/pass                    | yes/pass        |
| Anonymous User  | yes/pass     | yes/pass  | no/pass    | yes/pass       | yes/pass   | yes/pass         | no/pass        | no/pass                    | no/pass         |                    |

<br>

Home page validator testing.

<img src="../docs/testing_images/w3_1_errors.png"><br>
_W3C HTML Validator Testing Image_ 

The errors were corrected and now the Validator returns no errors.


The Home page was passed through the Wave Accesibility checker and returned no errors.

<img src="../docs/testing_images/home_wcag.png"><br>
_Wave Accessiblity Testing Image_

The Home Page was passed through Lighthouse and returned the following performance results:

<img src="../docs/testing_images/lighthouse_1.png"><br>
_Desktop Lighthouse Performance Testing Image_

<img src="../docs/testing_images/lighthouse_2.png"><br>
_Mobile Lighthouse Performance Testing Image_

In future versions of the app I hope to significantly improve mobile performance.
<br>
</details>


Home page responsivness testing.
* Fully responsive
<br>