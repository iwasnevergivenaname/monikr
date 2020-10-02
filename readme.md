# welcome to monikr!
our website is aimed for indie artists who wish to showcase their original art pieces only and for users who are in interested in viewing their art or seeking for an artists to paint for their next big print.
## General Approach we took
Han and Alpha had decided to split the backend and frontend between the two. One person tackles the backend while the other person starts designing the website to make it move fast and smoothly without few conflicts (if any were to occur).
Alpha: Frontend -
1. Han had sent me some websites that she felt inspired from and I looked over them. I knew this was going to be tough, but I wanted to also get creative (and colorful) as much as I could. Thef first that I felt was easy to accomplish was the about us page. From there, I felt like every website I went to had a nav bar, so I went to materialize css and looked at my options. From there, Han and I had decided on a rough color scheme. I wanted to implemenet a different color for the nav than the standard one I got from materialize. I combined Han's favorite colors and attempted a linear gradient like so:
```css
nav {
    background: linear-gradient(to right, rgb(224, 153, 165), rgb(243, 167, 243), rgb(206, 73, 206), grey);
}
```
2. From the about page, I knew the more difficult pages to create was going to be the welcoming page, the profile page, the salon and the salon/post pages because those were supposed to be created in a way that makes the whole website like a gallery. For the homepage, I needed to look up different grid views for photos and needed to shape them in a way that actually had them in a gallery view instead of a regular table like grid. I hard coded the photos since we didn't have any photos from the users to use yet and tested out how it'd would look like. Essentially, I have three different divs with the css looking like so:
```css
.outer-grid {
    display: flex;
    flex-wrap: wrap;
    padding: 0 4px;
}
.inner-grid {
    flex: 25%;
    max-width: 25%;
    padding: 0 4px;
}
.inner-grid img {
    margin-top: 8px;
    width: 100%;
    padding: 10px;
}
```
This is also responsive which made everything work even better. The photos are randomly placed on the webpage, so I had to see where each one of the photos I had implemented went and eventually, go the results I had wanted. I also have them in different divs because I wanted a clean transition from the different types of art we hold on the website and it made everything look perfect.
3. As for the profile page, Han had an idea that I thought I couldn't accomplish at first but she gave me a starter idea where you can have three divs and then play around with it then. So, I ended up using float positioning and added a media responsiveness because I realized without it, the divs overlapped one another. As you make the screen smaller, it does overlap but then reaches a point where they fix themselves in a proper positioning. The css I used for this was:
```css
/* Create three equal columns that floats next to each other */
.column {
    float: left;
    width: 33.33%;
    padding: 10px;
    text-align: center;
  }
  /* Clear floats after the columns */
  .row:after {
    content: "";
    display: table;
    clear: both;
}
  /* Responsive layout - makes the three columns stack on top of each other instead of next to each other */
@media screen and (max-width: 600px) {
.column {
    width: 100%;
    }
}
```
credits to w3schools for helping me out creating this.
4. For the salon pages, I had to create their own html boilerpoint because we wanted to incorporate a banner underneath the nav bar, but there was a div that was making the banner and the nav bar have a white space. Once I figured how to implement the styling and html coding needed to make the banner look nice, everything else became easier in terms of adding the information needed for the page.  Besides these main pages, the forms were easier to create and style as well as the search bar and the lists to view artists and tags.

Backend - 

from views.py
```python def page(request, pk):
	artist = Artist.objects.get(pk=pk)
	user = User.objects.filter(artist=artist)
	try:
		currentUser = User.objects.get(username=request.user.username)
	except Exception as e:
		print(f'page error {e}')
		currentUser = None
	text_exhibit = TextExhibit.objects.filter(artist=artist)
	photo_exhibit = PhotoExhibit.objects.filter(artist=artist)
	try:
		icon = Icon.objects.get(artist=artist)
	except Exception as e:
		icon = None
	contact = Contact.objects.filter(artist=artist)
	commission = Commission.objects.filter(artist=artist)
	return render(request, 'artists/page.html',
	              {'artist': artist, 'text_exhibit': text_exhibit, 'photo_exhibit': photo_exhibit,
	               'contact': contact, 'commission': commission, 'user': user, 'currentUser': currentUser, 'icon': icon
	               })
```

this was difficult for me, Han, to originally get the correct page auth. The User model is connected to both the Artist and the regular user, and user variable is connected to the artist page. i needed to make sure that a random regular user couldn't edit an Artist page, so i had to store the current user username, which i then checked against the artist user name in my page.html

```{% if currentUser.username == u.username %}```

## to run
make sure you have django installed
fork and clone this repo
run `pip3 install  django-materializecss-form` <br>
run `pip3 install psycopg2` <br>
then `createdb monikr` <br>
run these next 2 lines of code after any database changes you have <br>
`python3 manage.py makemigrations`
and `python3 manage.py migrate`
if you add any new models, to see them on the admin page, you must
import and register them in admin.py
## artist profiles
![timothy page](https://i.imgur.com/8OBAXP5.png)
![sleepy page](https://i.imgur.com/XbVmxZk.png)
![boy bloom](https://i.imgur.com/qBh51bz.png)
## User Stories
‣ as a user i want to come to a home page of carosoling pieces of art <br>
‣ as a user i can search from any number of fields, like name, medium, location <br>
‣ as a user i want my results to be returned in a visually pleasing manner <br>
‣ as a user i can click on any artist to see more about them <br>
‣ as a user i can click on the art displayed on their profile <br>
## routes
| path | description |
| ---- | ------ |
| / | home |
| /artist/:pk/ | artist profile |
| /exhibit/:pk/ | specific artist post |
| /artist/<int:pk>/salon | artist salon |
| /artist/<int:pk>/salon/<id> | specific salon post |
| /artist/:pk/update/ | edit profile |
| /text_exhibit/create/ | create text post |
| /text_exhibit/<int:pk>/update/ | edit text post |
| /search/:id | search resaults |
## Unsolved problems or major hurdles
Alpha - Frontend:
1. As I was styling the website, I had originally had started out with a footer and the idea was that the footer would essentially hold the about us page and any other page that we felt didn't necessarily need to be on the nav bar. However, whenever I kept changing a lot of my css style for the body, my footer also ended up taking the changes in and essentially kept getting messed up. I decided to cut it out and would hope to revisit in the future to see what I kept messing up in my code to fix that.
2. Another thing that I kept having issues was implementing the base.html. Whenever I wanted to change something in one page (example: the about us page), I'd use the class name but for some reason was unable to change anything within that page. Essentially, the only way I was able to change the style of the current page was either using inline styling or had to make a decision which on which color to use for all tags (example: implementing a color for all h1 tags). That was another way I was able to implement a color change or text-align change, by setting it for all tags. I'd probably have to recheck how to properly style each page and understanding how
```django
{% block content %}
{% endblock %}
```
fully works.
3. Another hurdle I also faced was implementing materialize css onto our forms. At first, I thought I was using the correct scripts and inputting the correct links needed to get the forms working correctly for the forms (since we had selective for some of them) but realized that I actually was missing some. After realizing my mistake, I was able to get the forms 90% working. The  next hurdle was getting the boolean to be recognized on the form.
## Future implementations for monikr
- revisit footer and make it work for our website :blush:
- adding a drop down to search bar with colors
