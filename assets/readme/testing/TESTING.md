# Testing

- [Testing](#testing)
  * [User Story Tests](#user-story-tests)
+ [Manual Testing](#manual-testing)
    - [Authentication](#authentication)
    - [Home](#home)
    - [Products](#products)
    - [Product Detail](#product-detail)
    - [Product Management](#product-management)
    - [Shopping Bag](#shopping-bag)
    - [Checkout](#checkout)
    - [Shop Info](#shop-info)
    - [Wishlist](#wishlist)
    - [Discover](#discover)
    - [Contact](#contact)
    - [Newlsetter](#newsletter)
    - [Profile](#profile)
    - [Other](#other)

## Manual Testing

## Authentication

Authentication Testing

| **User status** | **Can  register** | **Can login** | **Can logout** | **Can access wishlist** | **Can access public pages** | **Can access my profile** | **Can add, edit & delete newsletters** | **Can add, edit & delete artwork** |
|---|---|---|---|---|---|---|---|---|
| **Super user** | no | yes | yes | yes | yes | yes | yes | yes |
| **Registered user** | no | yes | yes | yes | yes | yes | no | no |
| **Unregistered user** | yes | no (reffered to sign-up page) | n/a | no | yes | no | no | no |


## Home Page Testing

Related templates:
* base.html
* main-nav.html
* mobile-top-header.html
* index.html
* footer.html

Links - Rel attributes are set as noreferrer and noopener for external links.

### W3C CSS HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/home_html_checker.png">
</details>
<br>

### Wave Accesibility checker
* No significant errors.
<details><summary>Home Page Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/wave_home_page.png">
</details>

Two errors were flagged on wave testing.  
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

## Shop Page Testing

Templates:
products.html

### W3C CSS HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/shop_html.png">
</details>
<br>

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

## Product Details Page Testing

Templates:
product_detail.html

### W3C HTML Validator
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/product_details_html.png">
</details>
<br>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/product_details_wave.png">
</details>

Two errors were flagged on wave testing as per the Home page testing only.
<br>

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


## Shop Info Page Testing

Templates:
pages/shop_info.html


### W3C CSS HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/shop_info_html.png">
</details>
<br>

### Wave Accessibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/wave_shop_info.png">
</details>

Two errors were flagged on wave testing as per the Home Page wave testing. 

<br>

### Lighthouse Testing

<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/shop_info_lighthouse_desktop.png">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/shop_info_lighthouse_mobile.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>

## Discover & Related Pages Testing

Templates:
discover.html
artist.html
scientist.html
human.html
publications.html
awards.html


### W3C CSS HTML checker
* no errors
<details><summary>Discover W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/discover.html.png">
</details>
<br>
<details><summary>Artist W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/awards_html.png">
</details>
<br>
<details><summary>Human W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/html_human.png">
</details>
<br>
<details><summary>Scientist W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/scientist_html.png">
</details>
<br>
<details><summary>Awards W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/awards_html.png">
</details>
<br>
<details><summary>Publications W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/publications_html.png">
</details>
<br>

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

<br>

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

## Contact Page Testing

Templates:
contact.html
confirmation_email_body_txt
confirmation_email_subject.html

### W3C CSS HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="">
</details>
<br>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="">
</details>

Two errors were flagged on wave testing as per the Home Page wave testing. 

<br>

### Lighthouse Testing

<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>

## Newsletter & Newsletter Details Page Testing

Templates:


### W3C CSS HTML checker
* no errors
<details><summary>Newsletter W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/newsletter_html.png">
</details>
<br>
<details><summary>Newsletter Detail W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/news_detail_html.png">
</details>
<br>

### Wave Accesibility checker
* No significant errors.
<details><summary>Newsletter Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/newsletter_wave.png">
</details>
<details><summary>Newsletter Detail Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/news_detail_wave.png">
</details>

Two errors were flagged on wave testing as per the Home Page wave testing. 

<br>

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
<br>
</details>

## Wishlist Page Testing

Templates:
wishlist.html

### W3C CSS HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/wishlist_html.png">
</details>
<br>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/wish_wave.png">
</details>

Two errors were flagged on wave testing as per the Home Page wave testing. 

<br>

### Lighthouse Testing

<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/wish_desk_light.png">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/wish_mob_light.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>

## Profile Page Testing

Templates:


### W3C CSS HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/profile_html.png">
</details>
<br>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/profile_wave.png">
</details>

The same error was flagged across 7 fields in the update details section - there is no form label on the fields for screen readers.  This would be amended in a future release. 

<br>

### Lighthouse Testing

<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/profile_desk_wave.png">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="/workspace/aeh_art/assets/readme/images/profile_mob_wave.png">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>

## ArtWork Page & CRUD Testing

### W3C CSS HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="">
</details>
<br>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="">
</details>



<br>

### Lighthouse Testing

<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>

## xxx Page Testing

Templates:


### W3C CSS HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="">
</details>
<br>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="">
</details>

<br>

### Lighthouse Testing

<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>

## xxx Page Testing

Templates:

### W3C CSS HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="">
</details>
<br>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="">
</details>
<br>

### Lighthouse Testing

<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>

## xxx Page Testing

Templates:

### W3C CSS HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="">
</details>
<br>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="">
</details>
<br>

### Lighthouse Testing

<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>

## xxx Page Testing

Templates:

### W3C CSS HTML checker
* no errors
<details><summary>W3C HTML Validator Testing</summary>
    <img src="">
</details>
<br>

### Wave Accesibility checker
* No significant errors.
<details><summary>Wave Testing</summary>
    <img src="">
</details>
<br>

### Lighthouse Testing

<details><summary>(Desktop) Lighthouse Testing</summary>
    <img src="">
</details>
<details><summary>(Mobile) Lighthouse Testing</summary>
    <img src="">
</details>
<br>
In future releases the mobile lighthouse performance will be prioritised. Adding alternate smaller sized images for loading into the cards would help to improve performance.
<br>
</details>

## CSS Testing

## Javascript Testing
All Javascript was testing using Jshint - no errors.
<details><summary> JShint Testing</summary>
    <img src="">
</details>
<br>
<details><summary> JShint Testing</summary>
    <img src="">
</details>
<br>
<details><summary> JShint Testing</summary>
    <img src="">
</details>
<br>
<details><summary> JShint Testing</summary>
     <img src="">
</details>
<br>
<details><summary> JShint Testing</summary>
    <img src="">
</details>
<br>


## Flake8 Python Testing