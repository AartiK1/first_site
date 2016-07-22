from flask import Flask, render_template, request
import requests 

app = Flask("MyApp")

MAILGUN_DOMAIN = "sandbox69bd6b7fabef4c07875963a7013e6db4.mailgun.org"
MAILGUN_API_KEY = "key-7afaabe46e6598ce8e19a09ff16a0b4b"

def contact_us_message(to, first_name, msg):
    return requests.post(
        "https://api.mailgun.net/v3/%s/messages" % MAILGUN_DOMAIN, 
        auth=("api", MAILGUN_API_KEY),
        files = [("attachment", open("attachments/example.txt")), ("inline", open("static/images/happy_panda.png"))],
        data={
            "from": "Vegan Panda <mailgun@%s>" % MAILGUN_DOMAIN,
            "to": to,
            "subject": "Thank you for contacting us!",
            "text": "Hi %s!" % first_name.split(' ').pop(0),
            'html': '<html>Hi %s! <strong>Thank you</strong> for ... Inline image here: <img src="cid:happy_panda.png">.</html>' % first_name.split(' ').pop(0)
        })
        
def contact_message(to, first_name, last_name, tel, msg):
    return requests.post(
        "https://api.mailgun.net/v3/lists/contact-us@%s/members" % MAILGUN_DOMAIN,
        auth=('api', MAILGUN_API_KEY),
        data={'subscribed': True,
              'address': to,
              'name': first_name + last_name,
              'description': 'Contact Us Message',
              'vars': '{"telephone": "%s" , "comment": "%s"}' % (tel, msg)})



def subscription_message(to, full_name):
    return requests.post(
        "https://api.mailgun.net/v3/%s/messages" % MAILGUN_DOMAIN, 
        auth=("api", MAILGUN_API_KEY),
        files = [("attachment", open("attachments/example.txt")), ("inline", open("static/images/happy_panda.png"))],
        data={
            "from": "Vegan Panda <mailgun@%s>" % MAILGUN_DOMAIN,
            "to": to,
            "subject": "Welcome %s!" % full_name.split(' ').pop(0),
            "text": "Hi %s!" % full_name.split(' ').pop(0),
            'html': '<html> Hi %s! <strong>content</strong>. Thank you for subscribing to our newsletter... Inline image here: <img src="cid:happy_panda.png">. <br /> If you wish to unsubscribe, click </html>' % first_name.split(' ').pop(0)
        })


def add_list_member(to, full_name):
    return requests.post(
        "https://api.mailgun.net/v3/lists/newsletter@%s/members" % MAILGUN_DOMAIN,
        auth=('api', MAILGUN_API_KEY),
        data={'subscribed': True,
              'address': to,
              'name': full_name,
              'description': 'Newsletter Subscriber'})
             
            
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def home2():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")
    
@app.route("/thank-you.html")
def thank_you():
    return render_template("thank-you.html")
    
@app.route("/recipes.html")
def recipes():
    return render_template("recipes.html")
    
@app.route("/ingredients.html")
def ingredients():
    return render_template("ingredients.html")
    
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


    
@app.route("/thank-you.html", methods=['GET', 'POST'])
def contact_msg():
    form_data = request.form
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    to = request.form.get('email')
    tel = request.form.get('tel')
    msg = request.form.get('msg')
    contact_us_message(to, first_name, msg)
    contact_message(to, first_name, last_name, tel, msg)
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
