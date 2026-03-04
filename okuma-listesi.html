<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Okuma Listesi — Bu Muydu?</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root {
  --ink: #0a0804;
  --parchment: #f5f0e8;
  --gold: #c9a84c;
  --rust: #8b3a2a;
  --ash: #2a2520;
  --smoke: #6b6560;
  --cream: #ede8de;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  background-color: var(--ink);
  color: var(--parchment);
  font-family: 'Crimson Text', Georgia, serif;
  font-size: 18px;
  line-height: 1.7;
  overflow-x: hidden;
}
nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
  padding: 1.5rem 4rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: linear-gradient(to bottom, rgba(10,8,4,0.97), transparent);
}
.nav-logo {
  font-family: 'Playfair Display', serif;
  font-size: 1.4rem;
  font-weight: 900;
  color: var(--gold);
  text-decoration: none;
}
.nav-links { display: flex; gap: 2rem; list-style: none; }
.nav-links a {
  font-family: 'Space Mono', monospace;
  font-size: 0.7rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--smoke);
  text-decoration: none;
  transition: color 0.3s;
}
.nav-links a:hover { color: var(--gold); }

.page-header {
  padding: 10rem 4rem 4rem;
  border-bottom: 1px solid rgba(201,168,76,0.1);
}
.eyebrow {
  font-family: 'Space Mono', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 1.5rem;
}
.page-header h1 {
  font-family: 'Playfair Display', serif;
  font-size: clamp(3rem, 6vw, 6rem);
  font-weight: 900;
  line-height: 1.05;
}
.page-header h1 em { font-style: italic; color: var(--gold); }
.page-header p {
  font-size: 1.2rem;
  color: var(--smoke);
  font-style: italic;
  margin-top: 1.5rem;
  max-width: 500px;
}

.filter-bar {
  padding: 1.5rem 4rem;
  background: var(--ash);
  display: flex;
  gap: 0.8rem;
  flex-wrap: wrap;
  border-bottom: 1px solid rgba(201,168,76,0.1);
}
.filter-btn {
  font-family: 'Space Mono', monospace;
  font-size: 0.6rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  padding: 0.5rem 1.2rem;
  border: 1px solid rgba(201,168,76,0.25);
  background: transparent;
  color: var(--smoke);
  cursor: pointer;
  transition: all 0.3s;
}
.filter-btn:hover, .filter-btn.active {
  border-color: var(--gold);
  color: var(--gold);
  background: rgba(201,168,76,0.05);
}

.books-section { padding: 4rem; }

.books-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2px;
  background: rgba(201,168,76,0.1);
}

.book-card {
  background: var(--ash);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transition: transform 0.3s ease;
  position: relative;
}
.book-card:hover { transform: scale(1.01); z-index: 2; }
.book-card::after {
  content: '';
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--gold), var(--rust));
  transform: scaleX(0);
  transition: transform 0.4s ease;
  transform-origin: left;
}
.book-card:hover::after { transform: scaleX(1); }

.book-cover {
  width: 100%;
  aspect-ratio: 3/2;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}
.book-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease;
}
.book-card:hover .book-cover img { transform: scale(1.05); }

.book-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
  padding: 2rem;
  text-align: center;
}
.book-placeholder .p-title {
  font-family: 'Playfair Display', serif;
  font-size: 1rem;
  color: var(--gold);
  font-weight: 700;
}
.book-placeholder .p-author {
  font-family: 'Crimson Text', serif;
  font-size: 0.9rem;
  color: var(--smoke);
  font-style: italic;
}

.book-badge {
  position: absolute;
  top: 1rem; right: 1rem;
  font-family: 'Space Mono', monospace;
  font-size: 0.5rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  padding: 0.3rem 0.8rem;
  background: rgba(10,8,4,0.85);
  border: 1px solid rgba(201,168,76,0.5);
  color: var(--gold);
}
.book-badge.reading { border-color: rgba(200,100,50,0.6); color: #e07050; }
.book-badge.upcoming { border-color: rgba(107,101,96,0.4); color: var(--smoke); }

.book-info { padding: 1.5rem 1.8rem; flex: 1; display: flex; flex-direction: column; }
.book-genre {
  font-family: 'Space Mono', monospace;
  font-size: 0.55rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 0.4rem;
}
.book-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--cream);
  margin-bottom: 0.2rem;
  line-height: 1.2;
}
.book-author {
  font-style: italic;
  color: var(--smoke);
  font-size: 0.95rem;
  margin-bottom: 1rem;
}
.book-review {
  font-size: 1rem;
  color: rgba(245,240,232,0.8);
  line-height: 1.6;
  border-left: 2px solid rgba(201,168,76,0.3);
  padding-left: 1rem;
  flex: 1;
}
.book-stars { margin-top: 1rem; color: var(--gold); font-size: 0.9rem; letter-spacing: 2px; }
.book-stars .empty { color: rgba(201,168,76,0.2); }

.quote-block {
  background: var(--ash);
  padding: 5rem 4rem;
  text-align: center;
  border-top: 1px solid rgba(201,168,76,0.1);
}
.quote-block blockquote {
  font-family: 'Playfair Display', serif;
  font-size: clamp(1.4rem, 2.5vw, 2.2rem);
  font-style: italic;
  color: var(--cream);
  max-width: 700px;
  margin: 0 auto 1rem;
  line-height: 1.4;
}
.quote-block cite {
  font-family: 'Space Mono', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold);
}

footer {
  background: #050403;
  padding: 2.5rem 4rem;
  border-top: 1px solid rgba(201,168,76,0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}
footer p {
  font-family: 'Space Mono', monospace;
  font-size: 0.6rem;
  color: var(--smoke);
  opacity: 0.5;
}
.footer-links { display: flex; gap: 2rem; }
.footer-links a {
  font-family: 'Space Mono', monospace;
  font-size: 0.6rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--smoke);
  text-decoration: none;
  transition: color 0.3s;
}
.footer-links a:hover { color: var(--gold); }

@media (max-width: 900px) {
  nav { padding: 1.2rem 1.5rem; }
  .nav-links { display: none; }
  .page-header { padding: 8rem 1.5rem 3rem; }
  .filter-bar { padding: 1.5rem; }
  .books-section { padding: 2rem 1.5rem; }
  .books-grid { grid-template-columns: 1fr; }
  .quote-block { padding: 4rem 1.5rem; }
  footer { padding: 2rem 1.5rem; flex-direction: column; }
}
</style>
</head>
<body>

<nav>
  <a href="index.html" class="nav-logo">Bu Muydu?</a>
  <ul class="nav-links">
    <li><a href="index.html#videos">Videolar</a></li>
    <li><a href="index.html#blog">Yazılar</a></li>
    <li><a href="index.html#topics">Konular</a></li>
    <li><a href="index.html#destek">Destek</a></li>
  </ul>
</nav>

<div class="page-header">
  <p class="eyebrow">Kütüphane</p>
  <h1>Okuma<br><em>Listesi</em></h1>
  <p>Her kitap bir soru işaretiyle biter. İşte beni şekillendiren kitaplar.</p>
</div>

<div class="filter-bar">
  <button class="filter-btn active" onclick="filterBooks('all',this)">Tümü</button>
  <button class="filter-btn" onclick="filterBooks('okundu',this)">Okundu</button>
  <button class="filter-btn" onclick="filterBooks('okunuyor',this)">Okunuyor</button>
  <button class="filter-btn" onclick="filterBooks('okunacak',this)">Okunacak</button>
</div>

<section class="books-section">
  <div class="books-grid">

    <div class="book-card" data-status="okundu">
      <div class="book-cover" style="background:linear-gradient(135deg,#2a1a0a,#1a0f05);">
        <img src="https://covers.openlibrary.org/b/title/Kuslarda+Uctu-L.jpg" alt="Kuşlarda Uçtu"
          onerror="this.style.display='none'">
        <div class="book-placeholder" style="position:absolute;inset:0;background:linear-gradient(135deg,#2a1a0a,#1a0f05);">
          <span style="font-size:2.5rem;">📖</span>
          <span class="p-title">Kuşlarda Uçtu</span>
          <span class="p-author">Yaşar Kemal</span>
        </div>
        <span class="book-badge">Okundu</span>
      </div>
      <div class="book-info">
        <div class="book-genre">Roman · Türk Edebiyatı</div>
        <div class="book-title">Kuşlarda Uçtu</div>
        <div class="book-author">Yaşar Kemal</div>
        <p class="book-review">Yaşar Kemal'in kalemi Anadolu toprağından damlar gibi akar. İnsanı, doğayı ve kaderi birbirinden ayırt edemezsiniz — hepsi iç içe geçmiş, hepsi birbirini taşıyor.</p>
        <div class="book-stars">★★★★★</div>
      </div>
    </div>

    <div class="book-card" data-status="okundu">
      <div class="book-cover" style="background:linear-gradient(135deg,#1a0a0a,#2a1010);">
        <img src="https://covers.openlibrary.org/b/title/Murtaza-L.jpg" alt="Murtaza"
          onerror="this.style.display='none'">
        <div class="book-placeholder" style="position:absolute;inset:0;background:linear-gradient(135deg,#1a0a0a,#2a1010);">
          <span style="font-size:2.5rem;">📖</span>
          <span class="p-title">Murtaza</span>
          <span class="p-author">Orhan Kemal</span>
        </div>
        <span class="book-badge">Okundu</span>
      </div>
      <div class="book-info">
        <div class="book-genre">Roman · Türk Edebiyatı</div>
        <div class="book-title">Murtaza</div>
        <div class="book-author">Orhan Kemal</div>
        <p class="book-review">Murtaza bir karakter değil, bir hastalık. Kurallara körce bağlılık, insan sevgisinden yoksun bir disiplin... Orhan Kemal bu tipi o kadar gerçek çizmiş ki rahatsız ediyor.</p>
        <div class="book-stars">★★★★★</div>
      </div>
    </div>

    <div class="book-card" data-status="okundu">
      <div class="book-cover" style="background:linear-gradient(135deg,#0a0a1a,#101025);">
        <img src="https://covers.openlibrary.org/b/isbn/9780140449136-L.jpg" alt="Suç ve Ceza"
          onerror="this.style.display='none'">
        <div class="book-placeholder" style="position:absolute;inset:0;background:linear-gradient(135deg,#0a0a1a,#101025);">
          <span style="font-size:2.5rem;">📖</span>
          <span class="p-title">Suç ve Ceza</span>
          <span class="p-author">Dostoyevski</span>
        </div>
        <span class="book-badge">Okundu</span>
      </div>
      <div class="book-info">
        <div class="book-genre">Roman · Rus Edebiyatı</div>
        <div class="book-title">Suç ve Ceza</div>
        <div class="book-author">Fyodor Dostoyevski</div>
        <p class="book-review">Raskolnikov'un zihnine girmek en büyük cezaydı. Dostoyevski suçu dışarıda değil, insanın içinde araştırıyor. Vicdan denen şey bu kitapta bir hapishaneye dönüşüyor.</p>
        <div class="book-stars">★★★★★</div>
      </div>
    </div>

    <div class="book-card" data-status="okundu">
      <div class="book-cover" style="background:linear-gradient(135deg,#1a1505,#2a2010);">
        <img src="https://covers.openlibrary.org/b/isbn/9780060934347-L.jpg" alt="Don Kişot"
          onerror="this.style.display='none'">
        <div class="book-placeholder" style="position:absolute;inset:0;background:linear-gradient(135deg,#1a1505,#2a2010);">
          <span style="font-size:2.5rem;">📖</span>
          <span class="p-title">Don Kişot</span>
          <span class="p-author">Cervantes</span>
        </div>
        <span class="book-badge">Okundu</span>
      </div>
      <div class="book-info">
        <div class="book-genre">Roman · Klasik</div>
        <div class="book-title">Don Kişot</div>
        <div class="book-author">Miguel de Cervantes</div>
        <p class="book-review">Dünyayı olduğu gibi mi görmeli, yoksa olmasını istediğimiz gibi mi? Don Kişot bu soruyu deli saçması gibi sorar, ama cevap son derece ciddidir.</p>
        <div class="book-stars">★★★★<span class="empty">★</span></div>
      </div>
    </div>

    <div class="book-card" data-status="okundu">
      <div class="book-cover" style="background:linear-gradient(135deg,#0a1010,#051515);">
        <img src="https://covers.openlibrary.org/b/isbn/9780141439471-L.jpg" alt="Frankenstein"
          onerror="this.style.display='none'">
        <div class="book-placeholder" style="position:absolute;inset:0;background:linear-gradient(135deg,#0a1010,#051515);">
          <span style="font-size:2.5rem;">📖</span>
          <span class="p-title">Frankenstein</span>
          <span class="p-author">Mary Shelley</span>
        </div>
        <span class="book-badge">Okundu</span>
      </div>
      <div class="book-info">
        <div class="book-genre">Roman · Gotik</div>
        <div class="book-title">Frankenstein</div>
        <div class="book-author">Mary Shelley</div>
        <p class="book-review">Yapay zeka çağında Frankenstein okumak bambaşka bir his. Shelley 1818'de yazmış ama asıl mesele bugün: yarattığımızdan biz mi sorumluyuz?</p>
        <div class="book-stars">★★★★★</div>
      </div>
    </div>

  </div>
</section>

<div class="quote-block">
  <blockquote>"Bir kitap bizi ısırmayan ya da sokmayan bir kitapsa, neden okuyalım ki?"</blockquote>
  <cite>— Franz Kafka</cite>
</div>

<footer>
  <p>© 2025 Bu Muydu? — Tüm hakları saklıdır.</p>
  <div class="footer-links">
    <a href="index.html">Ana Sayfa</a>
    <a href="https://www.youtube.com/@bumuydu" target="_blank">YouTube</a>
    <a href="mailto:bumuydu@gmail.com">İletişim</a>
  </div>
</footer>

<script>
function filterBooks(status, btn) {
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('.book-card').forEach(card => {
    card.style.display = (status === 'all' || card.dataset.status === status) ? 'flex' : 'none';
  });
}
</script>
</body>
</html>
