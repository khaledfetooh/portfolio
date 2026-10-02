from html import escape as e

SKILLS = [
 ("shield-alert","SOC & SIEM",["SOC Operations","Splunk","SPL","SIEM","Log Analysis","Security Monitoring","Alert Analysis","Incident Response"]),
 ("monitor","Windows Security",["Windows","Windows Event Logs","Event Viewer","Group Policy","GPO","Security Logs","Log Collection","Windows Administration","Troubleshooting"]),
 ("terminal","Linux Administration",["Red Hat Enterprise Linux","RHEL","System Administration I","System Administration II","Users & Groups","Storage","LVM","SELinux","Firewall","SSH","NFS","Autofs"]),
 ("network","Networking",["TCP/IP","OSI Model","VLAN","Routing","Switching","DHCP","DNS","Physical Routers","Physical Switches","Network Troubleshooting"]),
 ("lock-keyhole","Network Security",["Fortinet","Huawei Security","Firewall","AAA","Kerberos","DHCP Snooping","Dynamic ARP Inspection"]),
 ("code-2","Programming & Tools",["Python","Flask","SQL","SQLite","Scapy","Wireshark","VMware","pfSense"]),
]

# (title, subtitle, date, description, badge)
EXP = [
 ("DEPI","Cyber Security Incident Response Analyst","2026 – Present","Professional cybersecurity training focused on Incident Response, SOC Operations, Security Monitoring, Networking and practical security concepts.",None),
 ("CIB Egypt","Summer Internship – The Green Leap","2025","Internship experience covering banking environment, sustainability, AI ethics, cybersecurity concepts and professional development.",None),
 ("Fortinet Cybersecurity Training","NTI / DEPI","Oct – Dec 2025","120-hour cybersecurity training covering Fortinet security technologies, networking and security fundamentals.","Final Score: 98%"),
 ("Huawei HCIA-Security V4.0","NTI","2026","Security training covering network security concepts and Huawei security technologies.","Final Score: 98.5%"),
 ("Red Hat System Administration I","RH124","Certificate of Attendance","Red Hat Enterprise Linux administration training covering command-line administration, users and groups, permissions, networking, services and system management.",None),
 ("Red Hat System Administration II","RH134","Certificate of Attendance","Advanced Red Hat Enterprise Linux administration training covering storage, LVM, networking, services, security, SELinux and system administration.",None),
 ("Red Hat Linux Administration","National Telecommunication Institute (NTI)","Certificate / Training","Practical Linux administration training covering Red Hat Enterprise Linux, command-line administration, networking, storage and system management.",None),
 ("CCNA 200-301 Corporate Training","Practical Networking Training","","Hands-on networking training using physical routers and switches, covering routing, switching, VLANs, TCP/IP and network troubleshooting.",None),
 ("Windows Administration & Security","Practical System Administration","","Hands-on work with Windows administration, Group Policy, Windows Event Logs, Event Viewer, security logs, log collection and troubleshooting.",None),
]

# (icon, color, tag, title, desc, tags, footer)
PROJECTS = [
 ("shield-alert","cyan","SOC Project","Security Operating System (SOS)","SOC Monitoring & Incident Response Platform designed to collect security information, classify network activity and display security alerts through a centralized dashboard.",["Python","Flask","SQLite","Scapy","UDP","SOC"],"Security Agent → UDP JSON → Flask → SQLite → Dashboard"),
 ("scan-search","blue","Security Tool","CyberShield Analyzer","Flask-based security analysis project for URL scanning and classification using machine-learning techniques.",["Python","Flask","PostgreSQL","Machine Learning","Web Security"],"Reported model accuracy: 85.47%"),
 ("file-search","purple",None,"Windows Security Log Analysis","Practical work with Windows Security Logs, Event Viewer and Group Policy concepts for understanding authentication activity, security events and log collection used in SOC monitoring.",["Windows","Event Viewer","Security Logs","Group Policy","Log Analysis"],None),
 ("bar-chart-3","orange",None,"Splunk SIEM & Log Analysis","Hands-on experience with Splunk for searching and analyzing security events, working with logs and investigating suspicious activity within a SIEM workflow.",["Splunk","SIEM","SPL","Log Analysis","Security Monitoring"],None),
]

NAV = ["home","about","skills","experience","projects","education","contact"]

def head(num, label, title):
    return f'''<div class="text-center mb-14"><p class="text-cyan-400 font-mono text-sm">{num} / {label}</p>
<h2 class="text-3xl md:text-4xl font-black text-white mt-2">{title}</h2></div>'''

def chips(items):
    return "".join(f'<span class="skill">{e(i)}</span>' for i in items)

nav = "".join(f'<a href="#{n}" class="hover:text-cyan-400 transition">{n.title()}</a>' for n in NAV)

skills = "".join(f'''<div class="glass rounded-2xl p-6"><i data-lucide="{ic}" class="text-cyan-400 w-8 h-8 mb-5"></i>
<h3 class="text-lg font-bold text-white mb-4">{e(t)}</h3><div class="flex flex-wrap gap-2">{chips(items)}</div></div>''' for ic,t,items in SKILLS)

def exp_card(t,s,d,desc,b):
    date = f'<span class="text-sm text-slate-500">{e(d)}</span>' if d else ""
    badge = f'<div class="mt-4"><span class="inline-flex px-3 py-1 rounded-full bg-green-400/10 text-green-400 text-sm">{e(b)}</span></div>' if b else ""
    return f'''<div class="glass rounded-2xl p-7"><div class="flex flex-col md:flex-row md:justify-between gap-4">
<div><h3 class="text-xl font-bold text-white">{e(t)}</h3><p class="text-cyan-400 mt-1">{e(s)}</p></div>{date}</div>
<p class="text-slate-400 mt-5 leading-8">{e(desc)}</p>{badge}</div>'''
exp = "".join(exp_card(*x) for x in EXP)

def proj(ic,c,tag,t,desc,tags,foot):
    tagh = f'<span class="text-xs px-3 py-1 rounded-full bg-{c}-400/10 text-{c}-300">{e(tag)}</span>' if tag else ""
    footh = f'<div class="mt-6 text-sm text-slate-500">{e(foot)}</div>' if foot else ""
    return f'''<div class="glass rounded-2xl p-7 hover:border-cyan-400/30 transition">
<div class="flex items-start justify-between gap-4"><div class="p-3 rounded-xl bg-{c}-400/10"><i data-lucide="{ic}" class="text-{c}-400 w-7 h-7"></i></div>{tagh}</div>
<h3 class="text-2xl font-bold text-white mt-6">{e(t)}</h3><p class="text-slate-400 mt-4 leading-8">{e(desc)}</p>
<div class="mt-6 flex flex-wrap gap-2">{chips(tags)}</div>{footh}</div>'''
projects = "".join(proj(*x) for x in PROJECTS)

term_rows = [("whoami","Khaled Fetooh","text-green-400"),("role","Junior SOC Analyst","text-white"),
 ("tools","Splunk | Windows Logs | Linux","text-yellow-300"),("focus","SIEM / Monitoring / Incident Response","text-slate-300"),
 ("status","● Learning & Building","text-green-400")]
term = "".join(f'''<p class="{'mt-3' if i else ''}"><span class="text-cyan-400">khaled@soc</span>:<span class="text-blue-400">~</span>$ {c}</p><p class="{k}">{e(o)}</p>''' for i,(c,o,k) in enumerate(term_rows))

def field(label, inner):
    return f'<div><label class="block text-sm text-slate-400 mb-2">{label}</label>{inner}</div>'
INP = 'class="w-full px-4 py-3 rounded-xl bg-slate-950 border border-slate-700 focus:border-cyan-400 outline-none transition"'

def contact_item(href, icon, label, val, extra=""):
    return f'''<a href="{href}" {extra} class="flex items-center gap-4 group"><div class="p-3 rounded-xl bg-cyan-400/10"><i data-lucide="{icon}" class="text-cyan-400"></i></div>
<div><p class="text-xs text-slate-500">{label}</p><p class="text-slate-200 group-hover:text-cyan-400 transition">{val}</p></div></a>'''

HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Khaled Fetooh | Junior SOC Analyst</title>
<meta name="description" content="Khaled Fetooh - Junior SOC Analyst | IT &amp; Cybersecurity">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%9B%A1%EF%B8%8F%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="css/style.css">
</head>
<body class="text-slate-200">

<header class="fixed top-0 left-0 right-0 z-50"><nav class="glass">
<div class="max-w-7xl mx-auto px-5 py-4 flex items-center justify-between">
<a href="#home" class="font-black text-xl tracking-wide text-white">K<span class="text-cyan-400">.</span>F</a>
<div class="hidden lg:flex items-center gap-6 text-sm">{nav}</div>
<a href="assets/Khaled_Fetooh_CV.pdf" download="Khaled_Fetooh_CV.pdf" class="px-4 py-2 rounded-lg bg-cyan-500 text-slate-950 font-bold text-sm hover:bg-cyan-400 transition flex items-center gap-2"><i data-lucide="download" class="w-4 h-4"></i>Download CV</a>
</div></nav></header>

<section id="home" class="min-h-screen flex items-center relative overflow-hidden grid-bg">
<div class="absolute w-72 h-72 bg-cyan-500/10 rounded-full blur-3xl top-20 left-10"></div>
<div class="absolute w-96 h-96 bg-blue-500/10 rounded-full blur-3xl bottom-10 right-10"></div>
<div class="max-w-7xl mx-auto px-5 pt-28 pb-16 relative z-10 w-full">
<div class="grid lg:grid-cols-2 gap-14 items-center">
<div>
<div class="inline-flex items-center gap-2 px-3 py-2 rounded-full border border-cyan-400/20 bg-cyan-400/5 text-cyan-300 text-sm mb-6"><span class="w-2 h-2 bg-cyan-400 rounded-full animate-pulse"></span>Junior SOC Analyst</div>
<p class="text-cyan-400 font-mono text-sm mb-3">HELLO, I'M</p>
<h1 class="text-4xl md:text-6xl font-black leading-tight text-white">KHALED <span class="text-cyan-400">FETOOH</span></h1>
<h2 class="mt-5 text-xl md:text-2xl font-semibold text-slate-300">Junior SOC Analyst <span class="text-cyan-400">|</span> IT &amp; Cybersecurity</h2>
<p class="mt-6 text-slate-400 max-w-2xl leading-8">Junior cybersecurity professional focused on Security Operations, SIEM, Log Analysis, Incident Response, Windows Security, Linux Administration and Network Security.</p>
<div class="mt-8 flex flex-wrap gap-4">
<a href="#projects" class="px-6 py-3 rounded-xl bg-cyan-500 text-slate-950 font-bold hover:bg-cyan-400 transition flex items-center gap-2"><i data-lucide="shield-check" class="w-5 h-5"></i>View Projects</a>
<a href="#contact" class="px-6 py-3 rounded-xl border border-slate-700 hover:border-cyan-400 hover:text-cyan-400 transition flex items-center gap-2"><i data-lucide="mail" class="w-5 h-5"></i>Contact Me</a>
</div>
<div class="mt-8 flex flex-wrap gap-5 text-sm text-slate-400">
<span class="flex items-center gap-2"><i data-lucide="map-pin" class="w-4 h-4 text-cyan-400"></i>Egypt</span>
<span class="flex items-center gap-2"><i data-lucide="mail" class="w-4 h-4 text-cyan-400"></i>khaledfetoh266@gmail.com</span>
</div></div>
<div class="flex flex-col items-center lg:items-end">
<div class="profile-ring rounded-full w-60 h-60 md:w-72 md:h-72 glow mb-8"><div class="w-full h-full rounded-full overflow-hidden bg-slate-900">
<img src="assets/profile.jpg" alt="Khaled Fetooh" class="profile-image w-full h-full"></div></div>
<div class="glass rounded-2xl overflow-hidden glow w-full max-w-xl">
<div class="flex items-center gap-2 px-5 py-3 border-b border-slate-700/50"><span class="w-3 h-3 rounded-full bg-red-400"></span><span class="w-3 h-3 rounded-full bg-yellow-400"></span><span class="w-3 h-3 rounded-full bg-green-400"></span><span class="ml-3 text-xs text-slate-500 terminal">khaled@soc:~</span></div>
<div class="p-6 terminal text-sm leading-8">{term}</div>
</div></div></div></div></section>

<section id="about" class="py-24"><div class="max-w-6xl mx-auto px-5">{head("01","ABOUT","About Me")}
<div class="grid md:grid-cols-2 gap-8">
<div class="glass rounded-2xl p-7"><div class="flex items-center gap-3 mb-5"><div class="p-3 rounded-xl bg-cyan-400/10"><i data-lucide="shield" class="text-cyan-400"></i></div><h3 class="text-xl font-bold text-white">Cybersecurity Focus</h3></div>
<p class="text-slate-400 leading-8">I am a Junior SOC Analyst focused on Security Monitoring, SIEM, Log Analysis, Incident Response, Windows Security and Linux Administration.</p></div>
<div class="glass rounded-2xl p-7"><div class="flex items-center gap-3 mb-5"><div class="p-3 rounded-xl bg-blue-400/10"><i data-lucide="monitor-search" class="text-blue-400"></i></div><h3 class="text-xl font-bold text-white">SOC &amp; Systems</h3></div>
<p class="text-slate-400 leading-8">Practical experience with Splunk, Windows Event Logs, Event Viewer, Group Policy, log collection, Windows administration and Red Hat Linux.</p></div>
</div></div></section>

<section id="skills" class="py-24 bg-slate-950/50"><div class="max-w-6xl mx-auto px-5">{head("02","SKILLS","Technical Skills")}
<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">{skills}</div></div></section>

<section id="experience" class="py-24"><div class="max-w-6xl mx-auto px-5">{head("03","EXPERIENCE","Experience &amp; Training")}
<div class="space-y-6">{exp}</div></div></section>

<section id="projects" class="py-24 bg-slate-950/50"><div class="max-w-6xl mx-auto px-5">{head("04","PROJECTS","Security Projects")}
<div class="grid md:grid-cols-2 gap-7">{projects}</div></div></section>

<section id="education" class="py-24"><div class="max-w-6xl mx-auto px-5">{head("05","EDUCATION","Education")}
<div class="glass rounded-2xl p-8"><div class="flex flex-col md:flex-row gap-6">
<div class="p-4 rounded-2xl bg-cyan-400/10 h-fit"><i data-lucide="graduation-cap" class="w-9 h-9 text-cyan-400"></i></div>
<div class="flex-1"><div class="flex flex-col md:flex-row md:justify-between gap-3">
<div><h3 class="text-2xl font-bold text-white">Bachelor of Artificial Intelligence</h3><p class="text-cyan-400 mt-1">Delta University for Science &amp; Technology</p></div>
<span class="text-sm text-slate-500">2023 – 2027</span></div>
<p class="text-slate-400 mt-5 leading-8">Academic background in Artificial Intelligence with a professional focus on cybersecurity, networking, systems and Security Operations.</p>
<div class="mt-5"><span class="inline-flex px-3 py-1 rounded-full bg-slate-800 text-slate-300 text-sm">GPA: 2.74</span></div>
</div></div></div></div></section>

<section id="contact" class="py-24 bg-slate-950/50"><div class="max-w-5xl mx-auto px-5">
<div class="text-center mb-14"><p class="text-cyan-400 font-mono text-sm">06 / CONTACT</p>
<h2 class="text-3xl md:text-4xl font-black text-white mt-2">Let's Connect</h2>
<p class="text-slate-400 mt-4">Interested in cybersecurity, SOC operations or collaboration?</p></div>
<div class="grid md:grid-cols-2 gap-7">
<div class="glass rounded-2xl p-7"><h3 class="text-xl font-bold text-white mb-7">Contact Information</h3><div class="space-y-6">
{contact_item("mailto:khaledfetoh266@gmail.com","mail","Email","khaledfetoh266@gmail.com")}
{contact_item("tel:+201005059033","phone","Phone","+20 100 505 9033")}
{contact_item("https://linkedin.com/in/khaled-fetooh-6312852bb","linkedin","LinkedIn","Khaled Fetooh",'target="_blank" rel="noopener noreferrer"')}
</div></div>
<div class="glass rounded-2xl p-7"><h3 class="text-xl font-bold text-white mb-6">Send a Message</h3>
<!-- استبدل YOUR_FORM_ID بالـ ID بتاعك من https://formspree.io -->
<form id="contact-form" method="POST" action="https://formspree.io/f/YOUR_FORM_ID" class="space-y-5">
{field("Name", f'<input type="text" name="name" required {INP} placeholder="Your name">')}
{field("Email", f'<input type="email" name="email" required {INP} placeholder="you@example.com">')}
{field("Message", f'<textarea name="message" rows="5" required {INP.replace('class="','class="resize-none ')} placeholder="Write your message..."></textarea>')}
<button type="submit" class="w-full py-3 rounded-xl bg-cyan-500 text-slate-950 font-bold hover:bg-cyan-400 transition flex justify-center items-center gap-2"><i data-lucide="send" class="w-5 h-5"></i><span id="send-label">Send Message</span></button>
<p id="form-status" class="text-sm text-center hidden"></p>
</form></div>
</div></div></section>

<footer class="border-t border-slate-800"><div class="max-w-6xl mx-auto px-5 py-8 flex flex-col md:flex-row justify-between items-center gap-4">
<p class="text-sm text-slate-500">© 2026 Khaled Fetooh. All rights reserved.</p>
<p class="text-sm text-slate-600 terminal">Static site · GitHub Pages</p></div></footer>

<script src="js/lucide.min.js"></script>
<script src="js/main.js"></script>
</body>
</html>
'''
open("index.html","w",encoding="utf-8").write(HTML)
print(len(HTML))
