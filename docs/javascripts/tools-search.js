// Предполагаем, что lunr уже загружен Material'ом
(function () {
  let index = null;
  let data = [];
  const input = document.getElementById("tools-search-input");
  const resultsList = document.getElementById("tools-search-results");

  if (!input || !resultsList) return;

  function renderResults(results) {
    resultsList.innerHTML = "";
    if (!results.length) {
      resultsList.innerHTML = "<li>Ничего не найдено</li>";
      return;
    }
    results.forEach(res => {
      const item = data.find(d => d.id === res.ref);
      if (!item) return;
      const li = document.createElement("li");
      li.innerHTML = `<strong>${item.name}</strong> — ${item.vendor} (${item.type}, ${item.tool_class})`;
      resultsList.appendChild(li);
    });
  }

  function init() {
    fetch("assets/search/tools.json")
      .then(r => r.json())
      .then(json => {
        data = json;
        index = lunr(function () {
          this.ref("id");
          this.field("name");
          this.field("vendor");
          this.field("type");
          this.field("tool_class");
          this.field("description");

          json.forEach(doc => this.add(doc), this);
        });
      })
      .catch(err => {
        console.error("Failed to load tools.json", err);
      });

    input.addEventListener("input", function () {
      const q = this.value.trim();
      if (!index || !q) {
        resultsList.innerHTML = "";
        return;
      }
      const results = index.search(q);
      renderResults(results);
    });
  }

  document.addEventListener("DOMContentLoaded", init);
})();
