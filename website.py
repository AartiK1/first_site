from flask import Flask, render_template, request
import requests 

app = Flask("MyApp")

MAILGUN_DOMAIN = "sandbox69bd6b7fabef4c07875963a7013e6db4.mailgun.org"
MAILGUN_API_KEY = "key-7afaabe46e6598ce8e19a09ff16a0b4b"

""" CONTACT US EMAIL """
def contact_us_message(to, first_name, msg):
    return requests.post(
        "https://api.mailgun.net/v3/%s/messages" % MAILGUN_DOMAIN, 
        auth=("api", MAILGUN_API_KEY),
        files = [("attachment", open("attachments/example.txt")), ("inline", open("static/images/happy_panda.png"))],
        data={
            "from": "WEBSITE NAME Support <mailgun@%s>" % MAILGUN_DOMAIN,
            "to": to,
            "subject": "Thank you for contacting us!",
            "text": "Hi %s!" % first_name.split(' ').pop(0),
            'html': '<html>Hi <strong>%s</strong>! Thank you for contacting us. Someone will be back to you within 24 hours. In the meantime, why not check out our blog posts, coding resources or quiz for your coding essentials. <br /> Your message: <br /> %s <br /><br /> <img src="cid:favicon2.png"> </html>' % (first_name.split(' ').pop(0) , msg)
        })

""" CONTACT US - STORE MESSAGE ON MAILGUN LIST """        
def contact_message(to, first_name, last_name, tel, msg):
    return requests.post(
        "https://api.mailgun.net/v3/lists/contact-us@%s/members" % MAILGUN_DOMAIN,
        auth=('api', MAILGUN_API_KEY),
        data={'subscribed': True,
              'address': to,
              'name': first_name + ' ' + last_name,
              'description': 'Contact Us Message',
              'vars': '{"telephone": "%s" , "comment": "%s"}' % (tel, msg)})

""" NEWSLETTER SUB FROM CONTACT FORM - EMAIL"""
def subscription_message_contact(to, first_name):
    return requests.post(
        "https://api.mailgun.net/v3/%s/messages" % MAILGUN_DOMAIN, 
        auth=("api", MAILGUN_API_KEY),
        files = [("attachment", open("attachments/example.txt")), ("inline", open("static/images/happy_panda.png"))],
        data={
            "from": "WEBSITE NAME <mailgun@%s>" % MAILGUN_DOMAIN,
            "to": to,
            "subject": "Welcome %s!" % first_name.split(' ').pop(0),
            "text": "Hi %s!" % first_name.split(' ').pop(0),
            'html': '<html> Hi %s! <strong>content</strong>. Thank you for subscribing to our newsletter... Inline image here: <img src="cid:happy_panda.png">. <br /> If you wish to unsubscribe, click </html>' % first_name.split(' ').pop(0)
        })

"""NEWSLETTER SUB FROM CONTACT FORM - Add to mail list"""
def add_list_member_contact(to, first_name, last_name, tel):
    return requests.post(
        "https://api.mailgun.net/v3/lists/newsletter@%s/members" % MAILGUN_DOMAIN,
        auth=('api', MAILGUN_API_KEY),
        data={'subscribed': True,
              'address': to,
              'name': first_name + ' ' + last_name,
              'description': 'Newsletter Subscriber',
              'vars': '{"telephone": "%s"}' % tel
              })

""" NEWSLETTER SUB - EMAIL"""
def subscription_message(to, full_name):
    return requests.post(
        "https://api.mailgun.net/v3/%s/messages" % MAILGUN_DOMAIN, 
        auth=("api", MAILGUN_API_KEY),
        files = [("attachment", open("attachments/example.txt")), ("inline", open("static/images/happy_panda.png"))],
        data={
            "from": "WEBSITE NAME <mailgun@%s>" % MAILGUN_DOMAIN,
            "to": to,
            "subject": "Welcome %s!" % full_name.split(' ').pop(0),
            "text": "Hi %s!" % full_name.split(' ').pop(0),
            'html': '<html> Hi %s! <strong>content</strong>. Thank you for subscribing to our newsletter... Inline image here: <img src="cid:happy_panda.png">. <br /> If you wish to unsubscribe, click </html>' % full_name.split(' ').pop(0)
        })

""" NEWSLETTER SUB - ADD TO MAIL LIST"""
def add_list_member(to, full_name):
    return requests.post(
        "https://api.mailgun.net/v3/lists/newsletter@%s/members" % MAILGUN_DOMAIN,
        auth=('api', MAILGUN_API_KEY),
        data={'subscribed': True,
              'address': to,
              'name': full_name,
              'description': 'Newsletter Subscriber'})
             
""" MAIN PAGES """            
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def home2():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/blog.html")
def blog():
    return render_template("blog.html")
    
@app.route("/terms.html")
def terms():
    return render_template("terms.html")

@app.route("/privacy-policy.html")
def privacy():
    return render_template("privacy-policy.html")
    
@app.route("/sitemap.html")
def sitemap():
    return render_template("sitemap.html")
    
@app.route("/thank-you.html")
def thank_you():
    return render_template("thank-you.html")
    

""" RECIPE PAGES """    
@app.route("/recipes.html")
def recipes():
    return render_template("recipes.html")
     
@app.route("/recipes/cuisine.html")
def recipes_cuisine():
    return render_template("recipes/cuisine.html")
    
@app.route("/recipes/staples.html")
def recipes_staples():
    return render_template("recipes/staples.html")
    
@app.route("/recipes/breakfast.html")
def recipes_breakfast():
    return render_template("recipes/breakfast.html")

@app.route("/recipes/starter.html")
def recipes_starter():
    return render_template("recipes/starter.html")

@app.route("/recipes/entree.html")
def recipes_entree():
    return render_template("recipes/entree.html")

@app.route("/recipes/dessert.html")
def recipes_dessert():
    return render_template("recipes/dessert.html")
    
@app.route("/recipes/snacks.html")
def recipes_snacks():
    return render_template("recipes/snacks.html")


""" CUISINE PAGES """

@app.route("/recipes/cuisine/korean.html")
def recipes_korean():
    return render_template("recipes/cuisine/korean.html")

@app.route("/recipes/cuisine/japanese.html")
def recipes_japanese():
    return render_template("recipes/cuisine/japanese.html")

@app.route("/recipes/cuisine/indian.html")
def recipes_indian():
    return render_template("recipes/cuisine/indian.html")

@app.route("/recipes/cuisine/chinese.html")
def recipes_chinese():
    return render_template("recipes/cuisine/chinese.html")
    
@app.route("/recipes/cuisine/lebanese.html")
def recipes_lebanese():
    return render_template("recipes/cuisine/lebanese.html")

@app.route("/recipes/cuisine/south-american.html")
def recipes_south_american():
    return render_template("recipes/cuisine/south-american.html")

@app.route("/recipes/cuisine/north-american.html")
def recipes_north_american():
    return render_template("recipes/cuisine/north-american.html")

@app.route("/recipes/cuisine/european.html")
def recipes_european():
    return render_template("recipes/cuisine/european.html")

""" INGREDIENTS PAGES """

@app.route("/ingredients.html")
def ingredients():
    return render_template("ingredients.html")

@app.route("/ingredients/indian.html")
def ingredients_indian():
    return render_template("ingredients/indian.html")

@app.route("/ingredients/korean.html")
def ingredients_korean():
    return render_template("ingredients/korean.html")
    
@app.route("/ingredients/japanese.html")
def ingredients_japanese():
    return render_template("ingredients/japanese.html")

@app.route("/ingredients/chinese.html")
def ingredients_chinese():
    return render_template("ingredients/chinese.html")

@app.route("/ingredients/south-american.html")
def ingredients_south_american():
    return render_template("ingredients/south-american.html")

@app.route("/ingredients/baking.html")
def ingredients_baking():
    return render_template("ingredients/baking.html")


    
@app.route("/thank-you.html", methods=['GET', 'POST'])
def contact_msg():
    form_data = request.form
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    to = request.form.get('email')
    tel = request.form.get('tel')
    msg = request.form.get('comments')
    contact_us_message(to, first_name, msg)
    contact_message(to, first_name, last_name, tel, msg)
    if request.form.get('sub'):
        subscription_message_contact(to, first_name)
        add_list_member_contact(to, first_name, last_name, tel)
    return render_template("thank-you.html")

@app.route("/newsletter-sub.html", methods=['GET', 'POST'])
def sign_up():
    form_data = request.form
    full_name = request.form.get('name')
    to = request.form.get('email')
    subscription_message(to, full_name)
    add_list_member(to, full_name)
    return render_template("newsletter-sub.html")

app.run()
