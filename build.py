# Static page builder for The Garage Door Co. of Carolina concept. Run: python3 build.py
import json
BASE = 'https://garage-door-co-of-carolina-demo.vercel.app/'
TEL, TEL_H = '+19105082108', '(910) 508&#8209;2108'
EMAIL = 'info@thegaragedoorcompany.biz'
EXA = 'https://exa.ai/library/place/h1qqmh4v40j'
ORG = {"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"The Garage Door Co. of Carolina",
 "url":BASE,"telephone":"+1-910-508-2108","email":EMAIL,
 "founder":{"@type":"Person","name":"Joel Greco"},
 "address":{"@type":"PostalAddress","addressLocality":"Wilmington","addressRegion":"NC","addressCountry":"US"},
 "openingHours":"Mo-Sa 06:00-20:00","areaServed":"Southeastern North Carolina",
 "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"97"}}
SVC_LD = {"@context":"https://schema.org","@type":"Service","serviceType":"Garage door and opener installation and repair","provider":{"@type":"HomeAndConstructionBusiness","name":"The Garage Door Co. of Carolina"},"areaServed":"Wilmington, NC"}

def K(t): return f'<p class="kicker">{t}</p>'
def SEAMS(cls=''): return f'<span class="seams {cls}" aria-hidden="true"><i></i><i></i><i></i></span>'

HEAD = '''<!doctype html><html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="The Garage Door Co. of Carolina (concept)"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{base}og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{base}og.png">
<meta name="robots" content="noindex, nofollow"><!-- concept demo, not for indexing -->
<meta name="theme-color" content="#5e0021">
<link rel="preload" as="font" type="font/woff2" href="fonts/archivo-normal-800-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="fonts/figtree-normal-400-700-latin.woff2" crossorigin>
<link rel="stylesheet" href="css/design-system.css"><link rel="stylesheet" href="css/components.css"><link rel="stylesheet" href="css/pages.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%238f0033'/%3E%3Cpath d='M6 10h20M6 16h20M6 22h20' stroke='%23fff' stroke-width='3'/%3E%3C/svg%3E">
<script>document.documentElement.classList.replace('no-js','js-ready')</script><script type="application/ld+json">{ld}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="demo-bar">Concept by <a href="https://luminarch.pro">LuminArch</a>. Not the official Garage Door Co. of Carolina site. Reviews are real and sourced; placeholders are labeled.</div>
<header class="top"><div class="wrap nav"><a class="mark" href="index.html"><span class="mk" aria-hidden="true"><i></i><i></i><i></i></span><span><b>The Garage Door Co. of Carolina</b><small>Joel Greco &middot; Wilmington, NC</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button><ul id="menu">{nav}</ul><a class="btn btn--call" href="tel:{tel}">Call {telh}</a></div></header><main id="main">'''

FOOT = f'''</main><footer class="site-foot">{SEAMS('seams--rule')}<div class="wrap">
<div class="sign">
 <p class="sign-k">Door stuck?</p>
 <p class="sign-h">Call Joel. You get the owner, not a call center.</p>
 <a class="sign-num" href="tel:{TEL}">{TEL_H}</a>
 <p class="sign-sub">Monday to Saturday, 6am to 8pm (per the Google listing) &middot; Wilmington and Southeastern NC</p>
</div>
<div class="foot-grid">
 <p class="foot-quote">&ldquo;Deal directly with the owner for fast response times and easy scheduling.&rdquo;<span>From the company&rsquo;s own website</span></p>
 <nav aria-label="Footer"><a href="services.html">Repairs and installs</a><a href="reviews.html">Reviews</a><a href="about.html">About Joel</a><a href="contact.html">Get a quote</a><a href="mailto:{EMAIL}">Email</a></nav>
</div>
<div class="foot-row"><span>The Garage Door Co. of Carolina &middot; Wilmington, North Carolina</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>
<nav class="callbar" aria-label="Quick contact"><a class="cb-call" href="tel:{TEL}">Call Joel &middot; {TEL_H}</a><a class="cb-q" href="contact.html">Quote</a></nav>
<script src="js/main.js"></script></body></html>'''

NAV = [('services.html','Services'),('reviews.html','Reviews'),('about.html','About Joel'),('contact.html','Get a quote')]
def bc(*n): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":a,"item":BASE+b} for i,(a,b) in enumerate(n)]}
def page(fn, t, d, body, ld=None):
    assert 50 <= len(t) <= 60, (fn, len(t), t)
    assert 140 <= len(d) <= 160, (fn, len(d), d)
    nav = ''.join(f'<li><a href="{h}"' + (' aria-current="page"' if h == fn else '') + f'>{n}</a></li>' for h, n in NAV)
    url = BASE + ('' if fn == 'index.html' else fn)
    open(fn,'w').write(HEAD.format(t=t,d=d,url=url,base=BASE,nav=nav,ld=json.dumps(ld or [ORG]),tel=TEL,telh=TEL_H) + body + FOOT)

# Google reviews, word for word, from Google listing data via the Exa place page (checked 9 Oct 2026). All 5 of 5.
# Two longer reviews (2020-01-29, 2018-09-03) are truncated in the source and are not used.
REV = [
 ('2026-02-24','Feb 2026','The Garage Door Company came through and exceeded our expectations! Garage door stopped working on a Sunday. They were here Monday morning before noon. Got it fixed in 45 minutes at a reasonable price. More importantly, they gave us an honest opinion and an option for us to make our own decision about saving money or replacing the entire part. Greatly appreciated that. Highly recommended!'),
 ('2026-03-06','Mar 2026','Support our local small businesses and hire Joel and his crew next time your garage door needs service or if you need to replace your existing door. This is a wonderful local company with excellent service and fair pricing. Joel&rsquo;s company was recommended by a friend. Joel was very prompt in responding and coming over to secure our door which had broken the night before. Would highly recommend his company!'),
 ('2022-02-03','Feb 2022','Great locally owned business! Joel was knowledgeable and was able to fit me in the day after I called him. He called me before he arrived and showed up on time. I had an issue with my sensors which I replaced but still had issues. Joel came out and found a short in the wires between the sensors and the garage door opener. He quickly resolved the issue and even tuned up the door. Professional, friendly, quick, punctual, and locally owned! I&rsquo;ve got a new garage door company. Thanks Joel!'),
 ('2021-10-24','Oct 2021','To start off I would like to say I am so grateful for Joel and his team. After contracting several garage door &ldquo;experts&rdquo; and facing similar issues days after work was performed, Joel and his son finally gave me an honest explanation of the doors problem and worked with me to determine a permanent solution that was within my budget. It&rsquo;s been about 3 weeks and my garage door finally opens 100% of the time without any trouble for the first time since I&rsquo;ve owned this home. Could honestly not recommend anybody more then them.'),
 ('2025-05-15','May 2025','Great local company with excellent service and super fair pricing. If you&rsquo;re having a problem with your garage door or it just needs to be replaced, don&rsquo;t hesitate to give them a call, you won&rsquo;t be disappointed. John H.'),
 ('2017-07-21','Jul 2017','What an excellent small company. Joel did an excellent job recommending and installing new doors and openers. He and his team were diligent in removing and disposing of the old doors and cleaned up the site. I would highly recommend this company for any garage door project you have.'),
]
def rcard(r):
    iso,d,txt = r
    return (f'<figure class="rcard rv"><span class="stars" aria-label="5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
            f'<blockquote><p>{txt}</p></blockquote><figcaption>Google review &middot; <time datetime="{iso}">{d}</time></figcaption></figure>')

FIX = [('Broken springs','When a spring goes, the door won&rsquo;t lift. Joel services and replaces just about any spring.'),
 ('Cables','Should be checked at least once a year along with the rest of the door.'),
 ('Tracks','A major part of the door. They need a smooth running surface.'),
 ('Hinges and rollers','They take the brunt of the door&rsquo;s weight. Keep them aligned and lubricated.'),
 ('Openers and sensors','Almost every make and model. One reviewer&rsquo;s fix was a short in the sensor wiring.'),
 ('Scheduled maintenance','Maintenance plans to keep the door rolling.')]

DOOR = f'''<div class="door rv" aria-hidden="false"><div class="door-frame" aria-hidden="true">{''.join('<div class="panel"><i></i><i></i><i></i><i></i></div>' for _ in range(4))}</div>
<a class="door-handle" href="tel:{TEL}"><small>Tap to call Joel</small>{TEL_H}</a></div>'''

# ---------- HOME ----------
page('index.html','Garage Door Repair and Installation | Wilmington, NC',
 'Garage door repair and new doors in Wilmington, NC from Joel Greco, installing since 1996. Springs, cables, openers. 4.9 stars on Google. Tap to call Joel now.', f'''
<section class="hero"><div class="wrap hero-grid">
 <div>{K(f'Wilmington, NC {SEAMS()}')}
  <h1>Door won&rsquo;t open? <em>Call the owner.</em></h1>
  <p class="lede">Joel Greco has installed and repaired garage doors and openers since 1996. Springs, cables, tracks, openers, and full new doors across Southeastern North Carolina.</p>
  <div class="cta"><a class="btn btn--call" href="tel:{TEL}">Call {TEL_H}</a><a class="btn btn--line" href="contact.html">Ask for a quote</a></div>
  <dl class="hero-facts"><div><dt>Google</dt><dd><b>4.9</b> <span class="stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span> 97 reviews</dd></div><div><dt>Hours</dt><dd>Mon to Sat, 6am to 8pm</dd></div><div><dt>Doors</dt><dd>Amarr &middot; LiftMaster openers</dd></div></dl>
 </div>
 <div>{DOOR}<p class="door-cap">The whole site is built around one tap: the phone number.</p></div>
</div></section>

<section class="breaks on-dark" aria-labelledby="br-h"><div class="wrap breaks-grid">
 <div class="breaks-head rv">{K('Repairs')}<h2 id="br-h">Most calls are one of six things.</h2><p>Joel services and repairs almost every make and model of door and opener. Here is what usually breaks.</p><a class="btn btn--call" href="tel:{TEL}">Call about a repair</a></div>
 <ol class="ledger rv">{''.join(f'<li><span class="n">{i+1:02d}</span><b>{a}</b><span>{b}</span></li>' for i,(a,b) in enumerate(FIX))}</ol>
</div></section>

<section class="install wrap" aria-labelledby="in-h"><div class="install-grid">
 <div class="rv">{K('New doors')}<h2 id="in-h">A new door, start to finish.</h2>
  <p>Sales and installation of garage doors and openers, from picking the door to hauling off the old one. A 2017 reviewer wrote that Joel&rsquo;s team &ldquo;were diligent in removing and disposing of the old doors and cleaned up the site.&rdquo;</p>
  <div class="phbox"><p><span class="ph">Placeholder</span> Photo of a recent install in Wilmington. Joel&rsquo;s own job photos go here.</p></div></div>
 <div class="brands rv"><div class="brand"><span class="kicker">Doors</span><b>Amarr</b><span>One of the two major vendors the company carries.</span></div><div class="brand"><span class="kicker">Openers</span><b>LiftMaster</b><span>The other. Catalogs on request.</span></div><a class="btn btn--ox" href="contact.html">Start a new door quote</a></div>
</div></section>

<section class="voices on-dark" aria-labelledby="vo-h"><div class="wrap">
 {K('Google reviews')}<h2 id="vo-h" class="sr">What customers say</h2>
 <div class="rating rv"><b>4.9</b><span class="stars" aria-label="4.9 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</span><span>from 97 Google reviews</span></div>
 <blockquote class="rv"><p class="pull">&ldquo;Garage door stopped working on a Sunday. They were here Monday morning before noon. Got it fixed in 45 minutes.&rdquo;</p></blockquote>
 <p class="pull-cap rv">Google review, February 2026</p>
 <div class="strip">{rcard(REV[1])}{rcard(REV[2])}{rcard(REV[3])}</div>
 <a class="btn btn--line rv" href="reviews.html">Read more reviews</a>
</div></section>

<section class="area wrap" aria-labelledby="ar-h">
 <div class="rv">{K('Where')}<h2 id="ar-h">Wilmington and Southeastern NC.</h2><p>The company says it has satisfied customers all over Southeastern North Carolina. Not sure if they come out your way? Call and ask.</p><a class="btn btn--call" href="tel:{TEL}">Call {TEL_H}</a></div>
 <div class="phbox rv"><p><span class="ph">Placeholder</span> Service area map: towns Joel covers, confirmed by Joel.</p></div>
</section>
''', ld=[ORG, bc(('Home',''))])

# ---------- SERVICES ----------
SV = [('springs','Spring repair','We can service and replace just about any spring quickly and efficiently.',REV[0]),
 ('openers','Opener repair and install','Repairs on almost every make and model; new LiftMaster openers installed.',REV[2]),
 ('cables','Cable replacement','Cables should be checked at least once a year along with the rest of the door.',None),
 ('tracks','Track repair','Tracks are a major part of the door and require a smooth running surface.',None),
 ('rollers','Hinge and roller repair','Hinges and rollers take the brunt of the weight of the door. Keep them aligned and lubricated.',None),
 ('maintenance','Scheduled maintenance','Maintenance plans to fit your needs and keep the door rolling.',None),
 ('new-doors','New doors','Sales and installation of Amarr garage doors, with the old door removed and hauled off.',REV[5])]
def sv(i,s):
    k,n,d,r = s
    side = (f'<blockquote class="note"><p>{r[2][:220].rsplit(" ",1)[0]}&hellip;</p><footer class="fine">Google review, {r[1]}</footer></blockquote>' if r else
            '<p class="note"><span class="ph">Placeholder</span> A photo from this kind of job and one line from Joel on how he handles it.</p>')
    return f'<article id="{k}" class="svc-row rv"><span class="n">{i+1:02d}</span><div><h2>{n}</h2><p>{d}</p><a class="tl" href="tel:{TEL}">Call about {n.lower()}</a></div>{side}</article>'
page('services.html','Garage Door Springs, Openers and New Doors | Wilmington',
 'Spring repair, cables, tracks, rollers, opener repair and new Amarr doors with LiftMaster openers from The Garage Door Co. of Carolina in Wilmington. Call Joel.', f'''
<section class="sub on-dark"><div class="wrap">{K('Repairs and installs')}<h1>What Joel fixes and installs.</h1><p class="lede">Service descriptions are taken from the company&rsquo;s own site. Ask Joel what your door needs.</p>{SEAMS()}</div></section>
<section class="wrap svc">{''.join(sv(i,s) for i,s in enumerate(SV))}</section>
<section class="wrap band rv"><h2>Not sure what&rsquo;s wrong?</h2><p>Describe the noise or what the door is doing. Joel will tell you if it&rsquo;s a repair or a replacement.</p><a class="btn btn--call" href="tel:{TEL}">Call {TEL_H}</a></section>
''', ld=[ORG, SVC_LD, bc(('Home',''),('Repairs and installs','services.html'))])

# ---------- REVIEWS ----------
page('reviews.html','Reviews | The Garage Door Co. of Carolina, Wilmington NC',
 'Real Google reviews for The Garage Door Co. of Carolina, quoted word for word with dates. 4.9 stars from 97 reviews for garage door repair in Wilmington, NC.', f'''
<section class="sub on-dark"><div class="wrap">{K('Reviews')}<h1>4.9 stars from 97 Google reviews.</h1><p class="lede">Six of them, word for word, with the month each was posted.</p>{SEAMS()}</div></section>
<section class="rv-list">{''.join(rcard(r) for r in REV)}</section>
<section class="wrap"><p class="note rv"><span class="ph">Placeholder</span> On the real site, a live Google reviews feed or a set Joel picks. Source: Google listing data, checked 9 Oct 2026.</p></section>
''', ld=[ORG, bc(('Home',''),('Reviews','reviews.html'))])

# ---------- ABOUT ----------
page('about.html','About Joel Greco | The Garage Door Co. of Carolina, NC',
 'Joel Greco has installed garage doors and openers since 1996 and runs The Garage Door Co. of Carolina in Wilmington, NC. Deal with the owner. Call today.', f'''
<section class="sub on-dark"><div class="wrap">{K('About')}<h1>Joel Greco&rsquo;s company.</h1><p class="lede">Installing garage doors and openers since 1996, per the company&rsquo;s own site. Incorporated in North Carolina in 2016.</p>{SEAMS()}</div></section>
<section class="about">
 <div class="phbox rv"><p><span class="ph">Placeholder</span> Portrait of Joel. The current site has one; use it with his OK.</p></div>
 <div class="rv">
  <h2>You deal with the owner.</h2>
  <p>The company&rsquo;s own pitch is simple: &ldquo;Deal directly with the owner for fast response times and easy scheduling.&rdquo; Reviewers back that up. They name Joel, they mention he called ahead and showed up on time, and one wrote that he answered the first call and the fifteen after it.</p>
  <p>Some reviewers mention Joel&rsquo;s son and his crew on the job.</p>
  <p class="note"><span class="ph">Placeholder</span> A few sentences from Joel: how he started in 1996 and what he wants a customer to know before a repair.</p>
 </div>
</section>
<section class="wrap facts rv"><h2 class="sr">Company facts</h2><dl>
 <div><dt>Company</dt><dd>The Garage Door Co. of Carolina</dd></div>
 <div><dt>Installing since</dt><dd>1996</dd></div>
 <div><dt>Based in</dt><dd>Wilmington, NC</dd></div>
 <div><dt>Hours</dt><dd>Mon to Sat, 6am to 8pm</dd></div>
</dl></section>
''', ld=[ORG, bc(('Home',''),('About Joel','about.html'))])

# ---------- CONTACT ----------
page('contact.html','Garage Door Quote | The Garage Door Co. of Carolina, NC',
 'Get a garage door repair or new door quote from Joel Greco in Wilmington, NC. Call (910) 508-2108 or email the company. Open Monday to Saturday, 6am to 8pm.', f'''
<section class="sub on-dark"><div class="wrap">{K('Get a quote')}<h1>Calling is fastest.</h1><p class="lede">Joel picks up. The form below shows how a quote request could work.</p>{SEAMS()}</div></section>
<section class="contact">
 <div class="rv">
  <h2>Reach Joel</h2>
  <a class="c-big" href="tel:{TEL}">{TEL_H}</a><br>
  <a class="c-mail" href="mailto:{EMAIL}">{EMAIL}</a>
  <p>Wilmington, NC<br>Monday to Saturday, 6am to 8pm<br>Sunday closed</p>
  <p class="fine">Hours from the Google listing. Confirm with Joel.</p>
 </div>
 <form id="qform" class="form rv" novalidate>
  <p class="note"><span class="ph">Demo form</span> Nothing is sent. On a real site this would go to Joel.</p>
  <fieldset><legend class="sr">Your details</legend>
   <div class="two"><label>Name<input name="n" autocomplete="name"></label><label>Phone<input name="p" type="tel" autocomplete="tel"></label></div>
   <div class="two"><label>Neighborhood or town<input name="t"></label><label>What do you need?<select name="w"><option>Repair</option><option>New door</option><option>New opener</option><option>Maintenance</option></select></label></div>
   <label>What is the door doing?<textarea name="m"></textarea></label>
  </fieldset>
  <button class="btn btn--ox" type="submit">Send request</button>
  <p id="qmsg" role="status"></p>
 </form>
</section>
''', ld=[ORG, bc(('Home',''),('Get a quote','contact.html'))])

# ---------- 404 ----------
page('404.html','Page Not Found | The Garage Door Co. of Carolina, Wilmington',
 'That page is not here. Head back to The Garage Door Co. of Carolina home page, or call Joel at (910) 508-2108 for garage door repair and installs in Wilmington.', f'''
<section class="sub on-dark"><div class="wrap">{K('404')}<h1>Wrong door.</h1><p class="lede">That page is not here.</p><div class="cta"><a class="btn btn--call" href="tel:{TEL}">Call {TEL_H}</a><a class="btn btn--line" href="index.html">Home</a></div></div></section>
''')
print('built')
