(function () {
  const input = document.getElementById("tools-search-input");
  const resultsList = document.getElementById("tools-search-results");

  if (!input || !resultsList) {
    return;
  }

  let tools = [];

  const basePath = "/oss_toolchainmap";

  fetch(basePath + "/assets/search/tools.json")
    .then(function (r) {
      return r.json();
    })
    .then(function (data) {
      if (!Array.isArray(data)) {
        console.error("[tools-search] tools.json is not an array");
        return;
      }
      tools = data;
      console.log("[tools-search] loaded", tools.length, "records");
    })
    .catch(function (err) {
      console.error("[tools-search] failed to load tools.json", err);
    });

  function renderResults(items) {
    resultsList.innerHTML = "";
    if (!items.length) {
      return;
    }

    items.slice(0, 50).forEach(function (tool) {
      const li = document.createElement("li");
      li.className = "tool-item";

      const title = document.createElement("div");
      title.className = "tool-title";
      title.textContent = tool.name || "Без названия";

      const meta = document.createElement("div");
      meta.className = "tool-meta";
      meta.textContent = [
        tool.vendor,
        tool.division,
        tool.type,
        tool.tool_class,
        tool.kind === "OSS" ? "OSS" : "PS"
      ]
        .filter(Boolean)
        .join(" · ");

      const desc = document.createElement("div");
      desc.className = "tool-desc";
      desc.textContent = tool.description || "";

      if (tool.link_URL) {
        const url = (tool.link_URL || "").split(",")[0].trim();
        const link = document.createElement("a");
        link.href = url;
        link.target = "_blank";
        link.rel = "noopener";
        link.textContent = "Сайт";
        link.className = "tool-link";
        desc.appendChild(document.createTextNode(" "));
        desc.appendChild(link);
      }

      li.appendChild(title);
      if (meta.textContent) li.appendChild(meta);
      if (desc.textContent) li.appendChild(desc);

      resultsList.appendChild(li);
    });
  }

  function onSearch() {
    const q = input.value.trim().toLowerCase();
    if (!q || !tools.length) {
      resultsList.innerHTML = "";
      return;
    }

    const filtered = tools.filter(function (t) {
      const haystack = [
        t.name,
        t.vendor,
        t.description,
        t.division,
        t.type,
        t.tool_class,
        t.kind,
        t.lic
      ]
        .filter(Boolean)
        .join(" ")
        .toLowerCase();

      return haystack.includes(q);
    });

    renderResults(filtered);
  }

  input.addEventListener("input", onSearch);
})();
