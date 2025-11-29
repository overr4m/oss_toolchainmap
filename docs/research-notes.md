title: "AppSec Toolchain Map"
---

# AppSec Toolchain Map

<a href="#" class="show-tools-overlay">Показать карту инструментов</a>

<div id="tools-overlay" class="tools-overlay">
  <div class="tools-overlay__backdrop"></div>
  <div class="tools-overlay__content">
    <button class="tools-overlay__close" aria-label="Закрыть">✕</button>
    <div class="tools-overlay__table">
      {{ generate_html_table_from_config() }}
    </div>
  </div>
</div>

---

# Поиск по инструментам

<div id="tools-search">
  <input type="search" id="tools-search-input"
         placeholder="Поиск по названию, вендору, описанию..." />
  <ul id="tools-search-results"></ul>
</div>