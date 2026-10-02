# Khaled Fetooh – Portfolio (Static)

## قبل الرفع
1. حط صورتك في: `assets/profile.jpg`
2. حط الـCV في: `assets/Khaled_Fetooh_CV.pdf`
3. فورم التواصل: اعمل فورم على https://formspree.io وبدّل `YOUR_FORM_ID` في `index.html`

## الرفع على GitHub Pages
1. ارفع محتوى الفولدر (index.html, css, js, assets, .nojekyll) على repo.
2. Settings → Pages → Source: Deploy from a branch → `main` / `(root)`.

## التعديل
- المحتوى: عدّل `build_html.py` ثم `python3 build_html.py`
- أو عدّل `index.html` مباشرة.
- بعد أي تغيير في الكلاسات: `npm i` ثم `npx tailwindcss -i src.css -o css/style.css --minify`
